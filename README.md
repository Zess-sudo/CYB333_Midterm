# CYB 333 Midterm Exam - Port Scanning Project

This repository contains programming scripts for CYB 333. The project demonstrates proficiency in socket programming and basic network scanning using Python.

## Table of Contents

- [Purpose](#purpose)
- [Project Contents](#project-contents)
- [Prerequisites](#prerequisites)
- [How to Run the Scripts](#how-to-run-the-scripts)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

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

---

## How to Run the Scripts

### 1. Server and Client (socket connection)

**A.** Run `python socket_server.py` in a dedicated terminal.  
_Example output:_  
`Server listening on 127.0.0.1:65432 (host:port)`

**B.** Run `python socket_client.py` in a separate terminal.  
_Example output:_  
`Connected to server at 127.0.0.1:65432
Sent: Hello, server!
Received: Message received!`
