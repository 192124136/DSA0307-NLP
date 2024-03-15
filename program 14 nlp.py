class AgreementChecker:
    def __init__(self, grammar):
        self.grammar = grammar

    def check_agreement(self, sentence):
        tokens = sentence.split()
        if len(tokens) < 3:
            return False

        subject = tokens[0]
        verb = tokens[1]

        if verb not in self.grammar["Verb"]:
            return False

        if subject in self.grammar["Singular"]:
            return verb in self.grammar["SingularVerb"]
        elif subject in self.grammar["Plural"]:
            return verb in self.grammar["PluralVerb"]
        else:
            return False


# Example usage
grammar = {
    "Singular": ["he", "she", "it"],
    "Plural": ["they", "we", "you", "I"],
    "Verb": ["is", "am", "are", "was", "were"],
    "SingularVerb": ["is", "am", "was"],
    "PluralVerb": ["are", "were"]
}

checker = AgreementChecker(grammar)
print(checker.check_agreement("he is"))  # Output: True
print(checker.check_agreement("they is"))  # Output: False
print(checker.check_agreement("we are"))  # Output: True
print(checker.check_agreement("she were"))  # Output: False
