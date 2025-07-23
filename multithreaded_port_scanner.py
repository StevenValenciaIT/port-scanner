# Importing necessary modules
import socket              # For network communication
from datetime import datetime  # For timestamping results
import threading           # To scan ports in parallel (faster)

# ---------- SETTINGS ----------

target_ip = "127.0.0.1"     # Target IP address to scan
start_port = 1              # Start of port range
end_port = 1024             # End of port range
timeout = 0.5               # Timeout for socket connection (in seconds)
log_file = "scan_results_threaded.txt"  # Log file name

# ---------- PORT SCAN FUNCTION ----------

def scan_port(ip, port):
    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout so it doesn't hang
            s.settimeout(timeout)
            # Attempt to connect to the IP and port
            result = s.connect_ex((ip, port))
            # If result is 0, the port is open
            if result == 0:
                message = f"[+] {ip}:{port} is OPEN"
                
                # Print to console
                print(message)
                
                # Append result to log file
                with open(log_file, "a") as f:
                    f.write(message + "\n")
    except Exception as e:
        print(f"[!] Error on {ip}:{port} - {e}")

# ---------- LOG FILE SETUP ----------

# Clear old log and write a fresh timestamp
with open(log_file, "w") as f:
    f.write(f"Threaded Port Scan Results ({datetime.now()}):\n\n")

# ---------- RUNNING SCAN ----------

print(f"\nStarting threaded scan on {target_ip}...\n")

# Loop through each port in the range
for port in range(start_port, end_port + 1):
    # For each port, create and start a new thread
    t = threading.Thread(target=scan_port, args=(target_ip, port))
    t.start()
