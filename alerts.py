from dfa import DFA

ATTACKS = {
    "SQL Injection (UNION)": DFA("UNION SELECT"),
    "SQL Injection (OR)": DFA("' OR 1=1"),
    "XSS": DFA("<script>alert"),
    "Directory Traversal": DFA("../"),
}


def detect_attack(payload):
    for name, dfa in ATTACKS.items():
        if dfa.match(payload):
            return name
    return None
