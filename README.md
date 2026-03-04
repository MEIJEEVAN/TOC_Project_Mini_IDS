# Project Documentation for Mini IDS

## Project Name
Mini Intrusion Detection System (Mini IDS)

## Course Information
Course Name: Cybersecurity 101
Instructor: Dr. Jane Doe

## Contributors
- John Smith
- Alice Johnson
- MEIJEEVAN

## Automata Types
- Finite State Machine (FSM)
- Pushdown Automata (PDA)

## Technology Stack
- Language: Python
- Framework: Flask
- Database: SQLite
- Tools: Git, Docker

## Project Overview
This Mini IDS aims to detect various intrusion patterns by monitoring network traffic using a set of predefined rules and behavior analysis. The system will provide real-time alerts when suspicious activity is identified.

## Project Structure
```
Mini_IDS/
│   README.md
│   app.py
│   requirements.txt
│
├───config/
│       config.yaml
│
├───detectors/
│       __init__.py
│       detector.py
│
├───models/
│       __init__.py
│       model.py
│
├───tests/
│       test_detector.py
│       test_model.py
│
└───utils/
        __init__.py
        helpers.py
```

## Attack Patterns Detected
- Port Scanning
- DDoS Attacks
- SQL Injection
- Phishing Attempts
- Malware Distribution
