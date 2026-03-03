# 🛡️ Mini IDS — Theory of Computation Project

A lightweight **Intrusion Detection System (IDS)** built using concepts from Theory of Computation (TOC). This project models network/web attack patterns as **finite automata**, enabling real-time detection of suspicious behavior through state-based pattern recognition.

---

## 🔍 Overview

This Mini IDS simulates detection of common web and network attacks by running incoming inputs through automata-based detectors. Each attack type is modeled as a **Deterministic Finite Automaton (DFA)** or **Nondeterministic Finite Automaton (NFA)**, where transitions represent sequences of suspicious activity leading to an "alert" state.

A **meta-controller** and **supervisor** coordinate all detectors, aggregating results and deciding whether to raise an alert.

---

## ⚠️ Detected Attack Types

| Attack | File | Description |
|---|---|---|
| Brute Force | `bruteforce.py` | Repeated failed login attempts |
| Command Injection | `command_injection.py` | Malicious shell commands in inputs |
| Login Bypass | `login_bypass.py` | SQL/logic-based authentication bypass |
| Path Traversal | `path_traversal.py` | Directory traversal (`../`) attempts |
| Port Scan | `port_scan.py` | Sequential port probing behavior |
| Session Hijacking | `session_behavior.py` | Anomalous session token/cookie behavior |

---

## 🏗️ Architecture

```
User Input / HTTP Request
        │
        ▼
   [ app.py ]  ←── Flask Web Interface
        │
        ▼
  [ main.py ]  ←── Entry point / orchestrator
        │
        ▼
[ meta_controller.py ] ←── Coordinates all detectors
        │
        ▼
[ supervisor.py ] ←── Final alert decision logic
        │
   ┌────┴─────┬──────────┬────────────┐
   ▼          ▼          ▼            ▼
bruteforce  cmd_inj  path_trav   (etc.)
        │
        ▼
  [ automata/ ] ←── DFA/NFA definitions
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/MEIJEEVAN/TOC_Project_Mini_IDS.git
cd TOC_Project_Mini_IDS
pip install -r requirements.txt
```

### Running the Web App

```bash
python app.py
```

Then open your browser and navigate to `http://localhost:5000`.

### Running Detectors Directly

```bash
python main.py
```

---

## 📁 Project Structure

```
TOC_Project_Mini_IDS/
├── automata/               # Automata (DFA/NFA) definitions for each attack
├── detectors/              # Individual attack detector modules
├── templates/              # HTML templates for the Flask web UI
├── unused/                 # Experimental or deprecated code
├── app.py                  # Flask web application
├── main.py                 # Main entry point
├── meta_controller.py      # Coordinates multiple detectors
├── supervisor.py           # Aggregates alerts and makes final decisions
├── bruteforce.py           # Brute force attack detector
├── command_injection.py    # Command injection detector
├── login_bypass.py         # Login bypass detector
├── path_traversal.py       # Path traversal detector
├── port_scan.py            # Port scan detector
├── session_behavior.py     # Session anomaly detector
└── requirements.txt
```

---

## 🧠 TOC Concepts Applied

- **Finite Automata (DFA/NFA)** — each detector models attack patterns as state machines
- **Regular Languages** — attack signatures expressed as regular expressions / automata transitions
- **Formal Language Theory** — inputs are treated as strings over an alphabet, accepted or rejected by automata

---

## 📚 Built With

- **Python** — core logic and detectors
- **Flask** — web interface
- **HTML/CSS** — frontend templates

---

## 👥 Contributors

- [MEIJEEVAN](https://github.com/MEIJEEVAN)

---

## 📄 License

This project was developed as an academic project for a Theory of Computation course. Feel free to use it for learning purposes.
