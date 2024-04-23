# Log Monitor

Log Monitor is a Python script that allows you to monitor Apache log files and perform basic log analysis.

## Features

- Real-time monitoring of Apache log files.
- Analysis of HTTP status codes and error messages.
- Summary reports displaying top HTTP status codes and repeated error messages.

## Requirements

- Python 3.x

## Usage

```
python log-monitor.py <log_file> --framework apache
```

- `<log_file>`: Path to the Apache log file you want to monitor.
- `--framework apache`: Flag to specify the log framework (currently only supports Apache logs).

## Example

```
python log-monitor.py access.log --framework apache
```

## Output

The script will continuously monitor the specified Apache log file and display new log entries in real-time. It will also analyze the log entries to count occurrences of HTTP status codes and error messages. Summary reports will be generated and displayed, showing the top HTTP status codes and repeated error messages.

An example from my terminal for one of my project:
```bash
$ python3 log-monitor.py ../../../public_html/feedback-backend/apache_logs/access.log --framework apache
172.19.0.1 - - [23/Apr/2024:20:14:07 +0000] "GET /module.php?to=Signup.getBranches&coursetype=ug HTTP/1.1" 200 644 "-" "PostmanRuntime/7.32.1"
172.19.0.1 - - [23/Apr/2024:20:14:10 +0000] "GET /module.php?to=Signup.getBranches&coursetype=ug HTTP/1.1" 200 643 "-" "PostmanRuntime/7.32.1"
172.19.0.1 - - [23/Apr/2024:20:14:19 +0000] "GET /module.php?to=Siup.getBranches&coursetype=ug HTTP/1.1" 404 328 "-" "PostmanRuntime/7.32.1"
172.19.0.1 - - [23/Apr/2024:20:14:26 +0000] "GET /moule.php?to=Siup.getBranches&coursetype=ug HTTP/1.1" 404 488 "-" "PostmanRuntime/7.32.1"
^C
Stopping log monitoring...

Summary Report:
Top HTTP Status Codes:
HTTP 200: 2 occurrences
HTTP 404: 2 occurrences

Top Repeated Error Messages:
```

## Notes

- Only Apache log framework is supported currently. Support for other log frameworks may be added in future versions.
