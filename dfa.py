class DFA:
    def __init__(self, pattern):
        self.pattern = pattern
        self.m = len(pattern)
        self.alphabet = set(pattern)
        self.transition = self._build_dfa()

    def _build_dfa(self):
        """
        Builds a DFA transition table.
        transition[state][char] = next_state
        """
        transition = [{} for _ in range(self.m + 1)]

        for state in range(self.m + 1):
            for char in self.alphabet:
                k = min(self.m, state + 1)
                while k > 0:
                    if self.pattern[:k] == (self.pattern[:state] + char)[-k:]:
                        break
                    k -= 1
                transition[state][char] = k

        return transition

    def match(self, text):
        state = 0
        for char in text:
            if char in self.transition[state]:
                state = self.transition[state][char]
            else:
                state = 0

            if state == self.m:
                return True
        return False

