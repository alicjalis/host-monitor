# host-monitor

A lightweight host monitoring tool written in Python.
Checks host availability via ping, open ports and TLS/SSL certificate validity.
Exposes results via a REST API and a web dashboard.

## Features
- ICMP ping check
- TCP port connectivity check
- TLS/SSL certificate validation with expiry warning (< 30 days)
- JSON-configurable host list
- REST API (`/api/hosts`)
- Web dashboard with auto-refresh
- File-based logging
- Unit tests with mocking (pytest)


## Requirements
- Python 3.10+
- Docker (optional)

## Usage

### CLI mode
Add hosts to `hosts.json` and run:
```bash
python main.py
```

### Flask dashboard
```bash
python app.py
```
Then open http://localhost:5000 in your browser.

### API
```
GET /api/hosts
```
Returns JSON list of hosts with status, last checked time and TLS certificate expiry.

## Running with Docker
```bash
docker build -t host-monitor .
docker run --cap-add=NET_RAW -p 5000:5000 host-monitor
```
> Note: ICMP ping checks may not work in all container environments due to raw socket restrictions.

## Running tests
```bash
pytest
```

## Tech stack
Python, sockets, subprocess, SSL, Flask, pytest, Docker