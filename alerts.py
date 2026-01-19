from dfa import DFA

ATTACKS = {
    "SQL Injection (UNION)": DFA("union select"),
    "SQL Injection (OR)": DFA("' or 1=1"),
    "SQL Injection (OR 1=1)": DFA(" or 1=1"),
    "SQL Injection (AND 1=1)": DFA(" and 1=1"),
    "SQL Injection (Tautology OR)": DFA(" or '"),
    "SQL Injection (Tautology AND)": DFA(" and '"),
    "SQL Injection (LIKE)": DFA(" like "),
    "XSS": DFA("<script"),
    "Directory Traversal": DFA("../"),
}


def detect_attack(payload):
    payload = payload.lower()
    for name, dfa in ATTACKS.items():
        if dfa.match(payload):
            return name
    return None
