class FSA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.accept_state = 'q2'
        self.start_state = 'q0'
        self.current_state = self.start_state

    def transition(self, input_char):
        if self.current_state == 'q0' and input_char == 'a':
            self.current_state = 'q1'
        elif self.current_state == 'q1' and input_char == 'b':
            self.current_state = 'q2'
        else:
            self.current_state = None

    def is_accepted(self):
        return self.current_state == self.accept_state

    def process_input(self, input_string):
        for char in input_string:
            self.transition(char)
            if self.current_state is None:
                return False
        return self.is_accepted()


def main():
    fsa = FSA()

    # Test cases
    test_strings = ['ab', 'aab', 'abb', 'acab', 'b', 'abab']

    for test_string in test_strings:
        if fsa.process_input(test_string):
            print(f"'{test_string}' is accepted")
        else:
            print(f"'{test_string}' is not accepted")


if __name__ == "__main__":
    main()
