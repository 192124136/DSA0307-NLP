import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.chunk import ne_chunk

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_noun_phrases(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    chunked_sentence = ne_chunk(tagged_words)
    
    noun_phrases = []
    for subtree in chunked_sentence:
        if isinstance(subtree, nltk.tree.Tree) and subtree.label() == 'NP':
            noun_phrase = " ".join(word for word, tag in subtree.leaves())
            noun_phrases.append(noun_phrase)
    
    return noun_phrases

def determine_meaning(noun_phrase):
    # Dummy implementation, replace this with your actual logic to determine meanings
    # For this example, we'll just return a placeholder meaning
    meanings = {
        "cat": "a small domesticated carnivorous mammal with soft fur, a short snout, and retractile claws",
        "ball": "a round or spherical object that is used in games and sports"
    }
    return meanings.get(noun_phrase, "Meaning not found")

def main():
    sentence = input("Enter a sentence: ")
    noun_phrases = extract_noun_phrases(sentence)
    
    print("\nNoun phrases found in the sentence:")
    for noun_phrase in noun_phrases:
        print("- {}".format(noun_phrase))
        meaning = determine_meaning(noun_phrase.lower())
        print("  Meaning:", meaning)

if __name__ == "__main__":
    main()
