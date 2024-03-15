import re

class FOPCParser:
    def __init__(self):
        self.variables = set()
        self.constants = set()
        self.predicates = set()

    def parse_expression(self, expression):
        expression = expression.strip()
        if self.is_atomic_expression(expression):
            self.parse_atomic_expression(expression)
        else:
            match = re.match(r'([^\(]+)\((.*)\)', expression)
            if match:
                predicate = match.group(1).strip()
                arguments = match.group(2).split(',')
                self.predicates.add(predicate)
                for arg in arguments:
                    self.parse_expression(arg)

    def is_atomic_expression(self, expression):
        return re.match(r'[a-zA-Z]+', expression)

    def parse_atomic_expression(self, expression):
        if expression.islower():
            self.variables.add(expression)
        else:
            self.constants.add(expression)

    def get_variables(self):
        return self.variables

    def get_constants(self):
        return self.constants

    def get_predicates(self):
        return self.predicates


# Example usage
parser = FOPCParser()
parser.parse_expression("P(x, y)")
parser.parse_expression("Q(a)")
parser.parse_expression("R(x)")

print("Variables:", parser.get_variables())
print("Constants:", parser.get_constants())
print("Predicates:", parser.get_predicates())
