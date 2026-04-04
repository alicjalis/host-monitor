# host-monitor
Host monitoring tool written in Python.

Checks host availability via ping, open ports and TLS/SSL certificate validity.

## Features
- ICMP ping check
- TCP port connectivity check  
- TLS/SSL certificate validation
- JSON-configurable host list
- File-based logging

## Requirements
- Python 3.10+
- pytest

## Usage
Add hosts to `hosts.json` and run:
```bash
python main.py
```

## Running tests
```bash
pytest
```

## Tech stack
Python, sockets, subprocess, SSL, pytest