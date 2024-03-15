import nltk
from nltk.tokenize import word_tokenize

# Sample text
text = "NLTK is a leading platform for building Python programs to work with human language data."

# Tokenize the text into words
words = word_tokenize(text)

# Perform part-of-speech tagging
tagged_words = nltk.pos_tag(words)

# Print the tagged words
print("Part-of-Speech Tagging Result:")
print(tagged_words)
