# port_scanner.py
Title: Network Port Scanner
What it does: A Python script that scans a target host for open TCP ports within a given range and reports which ports are open.
Why I built it: To understand network reconnaissance — the first step in security assessments — and how open ports can indicate running services that may be vulnerable.
What I learned: Port 22 (SSH) and Port 80 (HTTP) being open means those services are reachable — in a real assessment, you'd then check if those services have known vulnerabilities.
Note: Tested only on scanme.nmap.org, a server specifically authorized for scanning practice (important to mention — shows you understand ethics/legality).

## Sample Output

Scanning target: scanme.nmap.org
----------------------------------------
Port 22: OPEN
Port 80: OPEN
----------------------------------------
Open ports found: [22, 80]
