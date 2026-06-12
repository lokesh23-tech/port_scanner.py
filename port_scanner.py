import socket
from datetime import datetime

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except:
        return False

def port_scanner(target, start_port, end_port):
    print(f"Scanning target: {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 40)
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            open_ports.append(port)
            print(f"Port {port}: OPEN")
    
    print("-" * 40)
    print(f"Scan completed: {datetime.now()}")
    print(f"Open ports found: {open_ports if open_ports else 'None'}")

# Use scanme.nmap.org - a server set up by Nmap project for testing
target = "scanme.nmap.org"
port_scanner(target, 20, 100)
