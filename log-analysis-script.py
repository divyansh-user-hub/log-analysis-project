import subprocess
import signal
import sys
import logging

# Configure logging
logging.basicConfig(filename='log-monitor.py', level=logging.INFO, format='%(asc_time)s - %(level_name)s: %(message)s')

# Function to handle Ctrl+C and exit gracefully
def signal_handler(sig, frame):
    logging.info("Monitoring stopped.")
    sys.exit(0)

# Function to monitor log file and perform analysis
def monitor_log(log_file):
    # global tail_process
    global tail_process
    try:
        # Start monitoring the log file
        tail_process = subprocess.Popen(['tail', '-F', log_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Initialize dictionary to store keyword counts
        keyword_counts = {}

        logging.info("Monitoring log file for new entries. Press Ctrl+C to stop.")
        logging.info("Now Analyzing log entries...")

        # for Loop to read new log entries in real-time
        for i in iter(tail_process.stdout.readline, b''):
            i = i.decode('utf-8').strip()

            # Count occurrences of 'error'
            if 'error' in i.lower():
                keyword_counts['error'] = keyword_counts.get('error', 0) + 1

            # Count occurrences of 'HTTP status code'
            if 'HTTP' in i:
                http_code = i.split()[8]  # Assuming HTTP status code is at the 9th position
                keyword_counts[http_code] = keyword_counts.get(http_code, 0) + 1

            print(i)

            # if Ctrl+C is pressed to stop monitoring
            if stop_monitoring:
                break

        # Print summary report
        logging.info("Summary Report:")
        for keyword, count in keyword_counts.items():
            logging.info("%s: %s", keyword, count)

    except KeyboardInterrupt:
        logging.info("Monitoring stopped.")
    except Exception as e:
        logging.error("An error occurred: %s", e)
    finally:
        tail_process.kill()

if __name__ == "__main__":
    stop_monitoring = False
    signal.signal(signal.SIGINT, signal_handler)

    # Specify the log file to monitor
    log_file_path = "<Path_of_log_file>"

    monitor_log(log_file_path)

