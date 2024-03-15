class ParseTreeNode:
    def __init__(self, symbol, children=None):
        self.symbol = symbol
        self.children = children if children else []

    def add_child(self, child):
        self.children.append(child)


class ParseTreeGenerator:
    def __init__(self, grammar):
        self.grammar = grammar

    def generate_parse_tree(self, sentence):
        tokens = sentence.split()
        start_symbol = list(self.grammar.keys())[0]
        parse_tree = self._generate_parse_tree_recursive(tokens, start_symbol)
        return parse_tree

    def _generate_parse_tree_recursive(self, tokens, symbol):
        if symbol in self.grammar:
            for production in self.grammar[symbol]:
                children = []
                remaining_tokens = tokens.copy()
                for part in production.split():
                    if part in self.grammar:
                        child, remaining_tokens = self._generate_parse_tree_recursive(remaining_tokens, part)
                        children.append(child)
                    elif remaining_tokens and part == remaining_tokens[0]:
                        children.append(ParseTreeNode(part))
                        remaining_tokens.pop(0)
                    else:
                        break
                else:
                    if not remaining_tokens:  # All tokens are consumed
                        return ParseTreeNode(symbol, children), remaining_tokens
        return None, tokens


# Example usage
grammar = {
    "S": ["NP VP"],
    "NP": ["Det N", "Det N PP"],
    "VP": ["V", "V NP"],
    "Det": ["the", "a"],
    "N": ["man", "woman", "dog", "cat"],
    "V": ["saw", "chased", "bit", "kissed"],
    "PP": ["P NP"]
}

parser = ParseTreeGenerator(grammar)
parse_tree = parser.generate_parse_tree("the man saw a dog")
print("Parse Tree:")
def print_tree(node, depth=0):
    print("  " * depth + node.symbol)
    for child in node.children:
        print_tree(child, depth + 1)

print_tree(parse_tree[0])
