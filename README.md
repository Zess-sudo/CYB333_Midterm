# CYB 333 Midterm Exam - Port Scanning Project

This repository contains programming scripts for CYB 333. The project demonstrates proficiency in socket programming and basic network scanning using Python.

## Table of Contents

- [Purpose](#purpose)
- [Project Contents](#project-contents)
- [Prerequisites](#prerequisites)
- [How to Run the Scripts](#how-to-run-the-scripts)

## Purpose

This repository serves as a demonstration of socket programming and network scanning techniques, developed as part of the CYB 333 coursework.

## Project Contents

- **socket_server.py** – A basic socket server that listens for client connections and handles message exchanges.
- **socket_client.py** – A Python client that connects to the server, sends messages, and handles server responses.
- **port_scanner.py** – A Python-based port scanner capable of scanning specified port ranges on allowed hosts (localhost and scanme.nmap.org).

---

## Prerequisites

- Python 3.x installed  
- No additional libraries required (uses Python standard library)
- Ensure explicit authorization from the target system before performing any scans.

---

## How to Run the Scripts

### 1. Server and Client (socket connection)

**A.** Run `python socket_server.py` in a dedicated terminal.  
_Example output:_  
`Server listening on 127.0.0.1:65432 (host:port)`

**B.** Run `python socket_client.py` in a separate terminal.  
_Example output:_  
`Connected to server at 127.0.0.1:65432`  
`Sent: Hello, server!`    
`Received: Message received!`  
  
**C.** Run `python port_scanner.py`  
_Example output:_  
`Simple TCP Port Scanner`  
`Enter target host (default: 127.0.0.1): scanme.nmap.org`  
`Enter start port (default: 65432): 20`  
`Enter end port (default: 65432): 30`  
  
`Scanning scanme.nmap.org from port 20 to 30...`  
  
`[CLOSED] Port 20`  
`[CLOSED] Port 21`  
`[OPEN ] Port 22`  
`[CLOSED] Port 23`  
`[CLOSED] Port 24`  
`[CLOSED] Port 25`  
`[CLOSED] Port 26`  
`[CLOSED] Port 27`  
`[CLOSED] Port 28`  
`[CLOSED] Port 29`  
`[CLOSED] Port 30`  
  
`Scan complete.`  
`Open ports: [22]`  
`Closed ports: [20, 21, 23, 24, 25, 26, 27, 28, 29, 30]`  

