import nltk
from nltk.stem import PorterStemmer

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')

# Initialize the Porter Stemmer
porter_stemmer = PorterStemmer()

# List of words to be stemmed
words = ["cats", "running", "better", "saw", "mice", "was", "cities"]

# Stem each word in the list
stemmed_words = [porter_stemmer.stem(word) for word in words]

# Print the original words and their stemmed versions
for original, stemmed in zip(words, stemmed_words):
    print(f"{original} -> {stemmed}")
