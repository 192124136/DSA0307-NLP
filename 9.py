import re

# Rule-based POS tagging using regular expressions
def rule_based_pos_tagging(sentence):
    tagged_sentence = []
    for word in sentence:
        # Define rules based on word patterns
        if re.match(r'^[A-Z][a-z]+$', word):
            tagged_sentence.append((word, 'NNP'))  # Proper noun
        elif re.match(r'^[0-9]+(\.[0-9]*)?$', word):
            tagged_sentence.append((word, 'CD'))   # Cardinal number
        elif re.match(r'.*ly$', word):
            tagged_sentence.append((word, 'RB'))   # Adverb
        else:
            tagged_sentence.append((word, 'UNKNOWN'))
    return tagged_sentence

# Example sentence
sentence = "The quick brown fox jumps over the lazy dog"
tokenized_sentence = nltk.word_tokenize(sentence)

# Perform rule-based POS tagging
tagged_sentence = rule_based_pos_tagging(tokenized_sentence)
print("Rule-based POS Tagging Result:")
print(tagged_sentence)
