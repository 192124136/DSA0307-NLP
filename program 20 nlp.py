from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def lesk(word, sentence):
    best_sense = None
    max_overlap = 0
    word_synsets = wordnet.synsets(word)
    if not word_synsets:
        return None
    
    sentence = set(word_tokenize(sentence))
    sentence = sentence.difference(set(stopwords.words('english')))
    for sense in word_synsets:
        definition = set(word_tokenize(sense.definition()))
        overlap = len(sentence.intersection(definition))
        for example in sense.examples():
            example = set(word_tokenize(example))
            overlap += len(sentence.intersection(example))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense
    
    return best_sense

# Example usage
word = "bank"
sentence = "He sat by the river bank and watched the fish swim."
sense = lesk(word, sentence)
if sense:
    print("Word:", word)
    print("Sentence:", sentence)
    print("Best sense:", sense.name())
    print("Definition:", sense.definition())
else:
    print("No suitable sense found for the word:", word)
