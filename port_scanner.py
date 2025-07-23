# Importing the socket module to create network connections
import socket
# Importing the datetime to timestamp the scan results
from datetime import datetime

# ---------- SETTINGS ----------

# The IP address you want to scan (localhost in this case)
target_ip = "127.0.0.1"
# Range of ports to scan: 1 to 1024 (inclusive)
ports = range(1, 1025)
# How long to wait before timing out a connection (in seconds)
timeout = 0.5
# The name of the file where results will be saved
log_file = "scan_results.txt"

# ---------- FUNCTION TO SCAN A SINGLE PORT ----------

# Define the port scanning function
def scan_port(ip, port):
    try:
				# Create a TCP socket (AF_INET for IPv4, SOCK_STREAM for TCP)    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		        # Set the socket timeout to avoid hanging on dead ports
            s.settimeout(timeout)
            # Try to connect to the given IP and port
            result = s.connect_ex((ip, port))
            # If result is 0, the port is open
            if result == 0:
                message = f"[+] {ip}:{port} is OPEN"
                
                # Print the result to the terminal
                print(message)
                
                # Save the result to the log file
                with open(log_file, "a") as f:
                    f.write(message + "\n")
    # If there's an error (e.g., connection refused, etc.) print it
    except Exception as e:
        print(f"[!] Error scanning {ip}:{port} - {e}")

# ---------- LOG FILE SETUP ----------

# Clear old log file and add new timestamp
with open(log_file, "w") as f:
    f.write(f"Scan Results for {target_ip} ({datetime.now()}):\n\n")
    
# ---------- PORT SCAN ----------    

# Show user what target is being scanned
print(f"\nScanning {target_ip} from ports 1-1024...\n")

# Loop through each port in the list and call ther scan function
for port in ports:
    scan_port(target_ip, port)