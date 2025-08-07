#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import threading
import argparse
from datetime import datetime

# Function to scan a specific port
def scan_port(host, port, timeout):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)  # Set a timeout to avoid blocking
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        else:
            print(f"[-] Port {port} is closed")
        s.close()
    except socket.error as e:
        print(f"[!] Error scanning port {port}: {e}")

# Function to scan all specified ports
def scan_all_ports(host, ports, timeout):
    print(f"Starting port scan on {host}...")
    start_time = datetime.now()

    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(host, port, timeout))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"\nScan completed in {total_time}")

# Main function to handle command-line arguments and initiate the scan
def main():
    parser = argparse.ArgumentParser(description="Basic Port Scanner")
    parser.add_argument("host", help="IP address of the host to scan")
    parser.add_argument("-p", "--ports", type=str, default="1-1024", 
                        help="Range of ports to scan (default 1-1024)")
    parser.add_argument("-t", "--timeout", type=int, default=1, 
                        help="Timeout in seconds per port (default 1s)")
    
    args = parser.parse_args()

    # Validate the IP address
    try:
        socket.inet_aton(args.host)
    except socket.error:
        print("[!] Invalid IP address")
        return

    # Process the port range
    port_range = args.ports.split('-')
    if len(port_range) == 2:
        try:
            start_port = int(port_range[0])
            end_port = int(port_range[1])
            if start_port > end_port:
                print("[!] Start port cannot be greater than the end port.")
                return
        except ValueError:
            print("[!] Invalid port range.")
            return
    else:
        print("[!] Invalid port range format. Example: 1-1024")
        return

    # Start the port scan
    ports = range(start_port, end_port + 1)
    scan_all_ports(args.host, ports, args.timeout)

if __name__ == "__main__":
    main()
