# Cybersecurity Log Correlation & Alert System

A Python-based security tool that analyzes authentication logs, identifies repeated failed login activity, and generates simple security alerts.

## Features

- Parses security event logs
- Detects failed login attempts
- Tracks activity by source IP
- Flags repeated activity from the same IP
- Generates easy-to-read security alerts
- Uses a sample log dataset for testing

## Technologies

- Python 3
- File handling
- Collections
- Datetime

## Project Structure

```text
security-log-alert-system/
├── log_analyzer.py
├── sample_security.log
├── README.md
└── .gitignore
