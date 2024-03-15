import nltk
from nltk.corpus import brown
import random

# Train the POS tagger using Brown corpus
brown_tagged_sents = brown.tagged_sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)

# Simple stochastic POS tagging function
def stochastic_pos_tagging(sentence):
    tagged_sentence = []
    for word in sentence:
        # Use unigram tagger to get tag probabilities
        tag_probabilities = unigram_tagger.tag([word])
        if tag_probabilities[0][1]:
            # Randomly select a tag based on probabilities
            selected_tag = random.choice(tag_probabilities)[1]
            tagged_sentence.append((word, selected_tag))
        else:
            tagged_sentence.append((word, 'UNKNOWN'))
    return tagged_sentence

# Example sentence
sentence = "The quick brown fox jumps over the lazy dog"
tokenized_sentence = nltk.word_tokenize(sentence)

# Perform stochastic POS tagging
tagged_sentence = stochastic_pos_tagging(tokenized_sentence)
print("Stochastic POS Tagging Result:")
print(tagged_sentence)
