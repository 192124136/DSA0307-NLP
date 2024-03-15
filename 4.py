class PluralFiniteStateMachine:
    def __init__(self):
        # Define states and transitions
        self.transitions = {
            'q0': {'s': 'q1', 'x': 'q2', 'y': 'q3'},
            'q1': {'': 'q4'},  # plural forms ending in 's'
            'q2': {'': 'q5'},  # plural forms ending in 'x'
            'q3': {'': 'q6'},  # plural forms ending in 'y'
        }
        self.accept_states = {'q4', 'q5', 'q6'}
        self.start_state = 'q0'

    def generate_plural(self, noun):
        current_state = self.start_state
        for char in reversed(noun):  # Start from the end of the noun
            if char in self.transitions[current_state]:
                current_state = self.transitions[current_state][char]
            else:
                return None  # Invalid character encountered
        if current_state in self.accept_states:
            return noun + 'es'  # Add 'es' for plural
        else:
            return noun + 's'  # Add 's' for plural if not handled by the machine


def main():
    fsm = PluralFiniteStateMachine()

    # Test cases
    nouns = ['cat', 'box', 'lady', 'city', 'baby', 'fox']

    for noun in nouns:
        plural = fsm.generate_plural(noun)
        print(f"The plural of '{noun}' is '{plural}'")


if __name__ == "__main__":
    main()
