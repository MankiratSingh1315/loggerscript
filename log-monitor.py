import logging
import signal
import sys
import time
from collections import Counter
import re

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the root logger level to DEBUG
# Create a logger
logger = logging.getLogger(__name__)
# Define log message formats
formats = {
    logging.INFO: "INFO message",
    logging.DEBUG: "DEBUG message",
    logging.ERROR: "ERROR message"
}
# Define log levels to cycle through
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR]

# Function to handle Ctrl+C signal
def signal_handler(sig, frame):
    print("\nStopping log monitoring...")
    print_summary()  # Print summary before exiting
    sys.exit(0)

# Function to monitor log file
def monitor_log(log_file):
    try:
        with open(log_file, 'r') as file:
            file.seek(0, 2)  # Move the cursor to the end of the file
            while True:
                line = file.readline()
                if line:
                    print(line.strip())  # Display the new log entry
                    analyze_log(line)  # Analyze the log entry
                time.sleep(0.1)  # Adjust the sleep time as needed
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
        sys.exit(1)

# Function to analyze log entries
def analyze_log(log_entry):
    # Here you can perform your log analysis, such as counting occurrences of specific keywords or patterns
    global error_counter
    global status_code_counter
    
    # Extract HTTP status code using a more robust regular expression pattern
    http_status_match = re.search(r'HTTP/\d+\.\d+" (\d{3})', log_entry)
    if http_status_match:
        status_code = http_status_match.group(1)
        status_code_counter.update([status_code])
    
    # Count occurrences of 'ERROR' keyword
    if 'ERROR' in log_entry:
        error_counter['ERROR'] += 1

# Function to print summary report
def print_summary():
    print("\nSummary Report:")
    print("Top HTTP Status Codes:")
    for code, count in status_code_counter.most_common(5):
        print(f"HTTP {code}: {count} occurrences")
        
    print("\nTop Repeated Error Messages:")
    for error, count in error_counter.most_common(5):
        print(f"{error}: {count} occurrences")

if __name__ == "__main__":
    if len(sys.argv) < 4 or sys.argv[2] != "--framework" or not sys.argv[3]:
        print("Usage: python log-monitor.py <log_file> --framework apache")
        print("Framework is required.")
        sys.exit(1)

    global error_counter
    global status_code_counter
    error_counter = Counter()  # Counter to store error occurrences
    status_code_counter = Counter()  # Counter to store HTTP status code occurrences

    log_file = sys.argv[1]

    # Check if framework flag is provided and valid
    if sys.argv[3] == "apache":
        # Register signal handler for Ctrl+C
        signal.signal(signal.SIGINT, signal_handler)

        # Monitor the log file
        monitor_log(log_file)
    else:
        print("Under Construction: Only Apache log framework is supported currently.")
