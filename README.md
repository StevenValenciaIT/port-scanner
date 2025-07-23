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

## Run the script

```bash
python port_scanner.py
```

Then follow the prompts: 
- Enter the targer IP address
- Enter the port range to scan

## Example Output
``` pgsqql
Enter the IP address to scan: 192.168.1.1
Enter the starting port: 20
Enter the ending port: 25

[+] Scanning 192.168.1.1 from port 20 to 25...
[+] Port 22 is OPEN
[+] Port 23 is OPEN
[-] Port 24 is CLOSED
[-] Port 25 is CLOSED
```

