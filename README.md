# Simple Port Scanner

## Overview
This is a simple port scanner written in Python. It allows users to scan single ports, multiple ports, or a range of ports to determine their status (open or closed). The goal of this project is to learn more about network security and improve my Python skills

## Features
- Scan single ports
- scan multiple ports
- scan a range of ports
- exception handling for errors
- simultaneous scanning with concurrent.futures

 ## Upcoming Features
  - Banner grabbing for service identificaiton
 
 ## Installation
`git clone https://github.com/0xBash1127/Simple-Port-Scanner`

## Usage
- Single port scan: `python3 portScanner.py <ip_address> <port>`
- Multiple port scan: `python3 portScanner.py <ip_address> <port1,port2,port3>`
- Port range scan: `python3 portScanner.py <ip_address> <port1-port2>`
