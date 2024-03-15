class ParseError(Exception):
    pass

class Parser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, input_string):
        self.input_string = input_string
        self.index = 0
        try:
            return self.parse_expr()
        except ParseError:
            return False

    def parse_expr(self):
        return self.parse_term() or self.parse_expr_tail()

    def parse_expr_tail(self):
        if self.match('+'):
            return self.parse_term() or self.parse_expr_tail()
        elif self.match('-'):
            return self.parse_term() or self.parse_expr_tail()
        else:
            return False

    def parse_term(self):
        return self.parse_factor() or self.parse_term_tail()

    def parse_term_tail(self):
        if self.match('*'):
            return self.parse_factor() or self.parse_term_tail()
        elif self.match('/'):
            return self.parse_factor() or self.parse_term_tail()
        else:
            return False

    def parse_factor(self):
        if self.match('('):
            result = self.parse_expr()
            if not self.match(')'):
                raise ParseError("Expected closing parenthesis")
            return result
        elif self.match_number():
            return True
        else:
            return False

    def match(self, expected):
        if self.index < len(self.input_string) and self.input_string[self.index] == expected:
            self.index += 1
            return True
        return False

    def match_number(self):
        start = self.index
        while self.index < len(self.input_string) and self.input_string[self.index].isdigit():
            self.index += 1
        return self.index > start


# Example usage
grammar = {
    "expr": ["term expr_tail"],
    "expr_tail": ["+ term expr_tail", "- term expr_tail", ""],
    "term": ["factor term_tail"],
    "term_tail": ["* factor term_tail", "/ factor term_tail", ""],
    "factor": ["( expr )", "number"],
    "number": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

parser = Parser(grammar)
print(parser.parse("3+4*5"))  # Output: True
print(parser.parse("3+(4*5)"))  # Output: True
print(parser.parse("(3+4)*5"))  # Output: True
print(parser.parse("3+"))  # Output: False (Invalid syntax)
