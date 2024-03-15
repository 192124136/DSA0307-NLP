import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('wordnet')

# Sample text
text = "He walked to the store. The cats are playing in the garden."

# Tokenize the text into words
words = word_tokenize(text)

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("Word\t\tStem\t\tLemma")
print("---------------------------------------------")
for word in words:
    # Stem the word
    stemmed_word = stemmer.stem(word)
    
    # Lemmatize the word
    lemmatized_word = lemmatizer.lemmatize(word)
    
    print(f"{word}\t\t{stemmed_word}\t\t{lemmatized_word}")
