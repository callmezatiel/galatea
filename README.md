# Galatea

argparse: This library handles the command-line arguments for better flexibility and control. It allows you to specify the target IP address, port range, and timeout for each port scan.

Multithreading with threading: Threads are used to scan multiple ports simultaneously. This reduces the time needed for a large number of port checks, especially when scanning many ports.

Exception Handling: There are try-except blocks to catch any network-related errors during the port scan (e.g., timeout errors or invalid connections).

Timeout Handling: Each port scan is given a timeout, preventing the script from hanging indefinitely if a port doesn't respond in time.

User-Friendly Output: The script outputs whether a port is open or closed, and it reports any errors in a clear format.


Usage:

To scan a host with a specific range of ports (e.g., 1-1024):
```
python galatea.py 192.168.1.1 -p 1-1024
```
To set a custom timeout (e.g., 2 seconds per port):
```
python galatea.py 192.168.1.1 -p 1-1024 -t 2
```
