import socket
import sys
from datetime import datetime

def scan_target(target, ports):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n[!] Hostname could not be resolved.")
        sys.exit()

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 port_scanner.py <target_ip_or_domain>")
        sys.exit()

    target_host = sys.argv[1]
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]
    scan_target(target_host, common_ports)