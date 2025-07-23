# Python Port Scanner

A simple TCP Port Scanner built using Python's `socket` module. Created as part of my Cybersecurity learning journey and CompTIA Security+ preparation.

## Purpose

This tool helps understand how basic network scanning works and how open ports can be identified on a target system — a useful concept for Blue Team and Red Team awareness.

## Features

- Scan single IP addresses
- Check specified port ranges (e.g. 1–1024)
- Built using Python 3
- CLI-based with clean output

## How to Use

### 1. Clone the repo

```bash
git clone https://github.com/StevenValenciaIT/port-scanner.git
cd port-scanner
```

### 2. Run the script

```bash
python port_scanner.py
```

### 3. The default scan targets 127.0.0.1 (localhost) and ports 1 through 1024. You can modify the script to scan other IP addresses or port ranges.

## Example Output
``` console
Scanning 127.0.0.1 from ports 1-1024...

[+] 127.0.0.1:22 is OPEN
[+] 127.0.0.1:80 is OPEN
...
Scan results saved to scan_results.txt
```
## What I Learned
Using Python's socket module for network programming

- How TCP port scanning works

- Writing and managing log files

- Best practices for resource management using context managers (with statements)

## Disclaimer
This tool is for educational purposes only. Do not scan networks or systems without proper authorization.

## Future Improvements
- Add multithreading for faster scanning

- Add command-line arguments for IP and port range input

- Implement banner grabbing to identify services
