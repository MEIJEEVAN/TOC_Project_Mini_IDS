from dfa import DFA

ATTACKS = {
    "SQL Injection (UNION)": DFA("union select"),
    "SQL Injection (OR)": DFA("' or 1=1"),
    "XSS": DFA("<script"),
    "Directory Traversal": DFA("../"),
}


def detect_attack(payload):
    payload = payload.lower()
    for name, dfa in ATTACKS.items():
        if dfa.match(payload):
            return name
    return None
