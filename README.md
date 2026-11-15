# Python Port Scanner 🛡️

A simple, multi-threaded network port scanner built in Python for authorized reconnaissance and educational security assessments.

## Features 🚀
* **TCP Connect Scanning:** Quickly checks target ports using standard socket connections.
* **Common Port Profiling:** Pre-configured to scan high-priority ports (HTTP, HTTPS, SSH, FTP, MySQL, RDP, etc.).
* **Error Handling:** Gracefully handles DNS resolution failures and unreachable hosts.

## Requirements 📋
* Python 3.x
* Kali Linux or any Windows/Linux environment

## Usage 💻
Run the script from your terminal by passing the target IP address or domain:

```bash
python3 port_scanner.py <target_ip>
