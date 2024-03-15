class State:
    def __init__(self, rule, dot_position, start_position):
        self.rule = rule
        self.dot_position = dot_position
        self.start_position = start_position

    def __eq__(self, other):
        return self.rule == other.rule and self.dot_position == other.dot_position and self.start_position == other.start_position

    def __repr__(self):
        return f"State({self.rule}, {self.dot_position}, {self.start_position})"


def earley_parse(grammar, input_string):
    chart = [[] for _ in range(len(input_string) + 1)]

    # Add initial state to chart[0]
    for rule in grammar["S"]:
        chart[0].append(State(rule, 0, 0))

    for i in range(len(input_string) + 1):
        while True:
            chart_size = len(chart[i])
            for state in chart[i]:
                if not state_completed(state):
                    next_symbol = state.rule[state.dot_position]
                    if next_symbol in grammar:
                        predict(grammar, next_symbol, i, chart)
                    else:
                        scan(next_symbol, state, i, input_string, chart)
                else:
                    complete(state, i, chart)

            if chart_size == len(chart[i]):
                break

    return chart


def predict(grammar, symbol, position, chart):
    for rule in grammar[symbol]:
        new_state = State(rule, 0, position)
        if new_state not in chart[position]:
            chart[position].append(new_state)


def scan(symbol, state, position, input_string, chart):
    if position < len(input_string) and input_string[position] == symbol:
        new_state = State(state.rule, state.dot_position + 1, state.start_position)
        if new_state not in chart[position + 1]:
            chart[position + 1].append(new_state)


def complete(state, position, chart):
    for st in chart[state.start_position]:
        if not state_completed(st) and st.rule[st.dot_position] == state.rule[0]:
            new_state = State(st.rule, st.dot_position + 1, st.start_position)
            if new_state not in chart[position]:
                chart[position].append(new_state)


def state_completed(state):
    return state.dot_position == len(state.rule)


# Example usage
grammar = {
    "S": [
        ["NP", "VP"]
    ],
    "NP": [
        ["Det", "N"],
        ["NP", "PP"]
    ],
    "VP": [
        ["V", "NP"],
        ["VP", "PP"]
    ],
    "PP": [
        ["P", "NP"]
    ],
    "Det": ["the", "a"],
    "N": ["man", "woman", "park", "dog"],
    "V": ["saw", "ate", "walked"],
    "P": ["in", "on", "by", "with"]
}

input_string = "the man saw a dog in the park"

chart = earley_parse(grammar, input_string.split())

for i, states in enumerate(chart):
    print(f"Chart[{i}]:")
    for state in states:
        print(state)
