class DFA:
    def __init__(self, pattern):
        self.pattern = pattern

    def match(self, text):
        state = 0
        for char in text:
            if char == self.pattern[state]:
                state += 1
                if state == len(self.pattern):
                    return True
            else:
                state = 0
        return False
