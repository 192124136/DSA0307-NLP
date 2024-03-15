from nltk.corpus import wordnet

def explore_word_meanings(word):
    # Retrieve synsets for the word
    synsets = wordnet.synsets(word)
    
    if synsets:
        print(f"Synsets for '{word}':")
        for synset in synsets:
            print(f" - {synset.name()}: {synset.definition()}")
            print(f"   Examples: {synset.examples()}")
            print()
    else:
        print(f"No synsets found for '{word}'")

# Example usage
word = "book"
explore_word_meanings(word)
