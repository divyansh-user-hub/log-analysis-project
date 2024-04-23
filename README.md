**Log Analysis and Monitoring Script**

**Objective**

This script is designed to automate the analysis and monitoring of log files using Python scripting. It provides functionalities for real-time monitoring of log files and basic log analysis.

**Requirements**

Python 3.10

subprocess module

signal module

sys module

logging module


**Features**

Continuous monitoring of a specified log file for new entries
Real-time display of new log entries
Basic analysis of log entries:
Count occurrences of specific keywords or patterns (e.g., "error", "HTTP status codes")
Graceful exit using Ctrl+C

**Usage**

Clone this repository or download the script log_monitor.py.
Open a terminal and navigate to the directory containing log_monitor.py.
Replace **<Path_of_log_file>** with the actual path of the log file you want to monitor.
Press Ctrl+C to stop monitoring the log file.

**Configuration**

The script is configured to log information to a file named **log-monitor.py** in the same directory as the script itself. You can modify this behavior by changing the filename parameter in the basicConfig function call within the script.
