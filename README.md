#CYB 333 Midterm Exam - Port Scanning Project
Thie repository contains the completed programming scripts for CYB 333. The project demonstrates proficiency in socket programming and basic network scanning using Python.
## Project Contents:
- socket_server.py - A basic socket server that listens for client connection and handles message exchanges.
- socket_client.py - A Python client that connects to the server, sends messages, and handles server responses.
- port_scanner.py - A Python-based port scanner capable of scanning specified port ranges on allowed hosts (localhost and scanme.nmap.org).

---
## How to Run the Scripts:

### 1. Server and Client (socket connection)
A. run, python socket_server.py in a dedicated terminal. 
output: Server listening on 127.0.0.1:65432 (host:port)

B. run, python socket_client.py in a dedicated terminal. 
output:
Connected to server at 127.0.0.1:65432
Sent: Hello, server!
Received: Message received!

C. 
