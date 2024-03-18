import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def resolve_references(text):
    sentences = sent_tokenize(text)
    resolved_text = ""
    for sentence in sentences:
        tagged_sentence = pos_tag(word_tokenize(sentence))
        chunked_sentence = ne_chunk(tagged_sentence)
        resolved_sentence = ""
        for subtree in chunked_sentence:
            if type(subtree) == nltk.tree.Tree:
                if subtree.label() == 'NP':  # Noun phrase
                    antecedent = find_antecedent(subtree)
                    resolved_sentence += antecedent + " "
                else:
                    resolved_sentence += " ".join(word for word, tag in subtree.leaves()) + " "
            else:
                resolved_sentence += subtree[0] + " "
        resolved_text += resolved_sentence.strip() + "\n"
    return resolved_text

def find_antecedent(subtree):
    for node in subtree:
        if type(node) == nltk.tree.Tree:
            if node.label() == 'NP':
                return find_antecedent(node)
        else:
            if node[1] == 'PRP':
                antecedent = get_antecedent(node)
                return antecedent
    return ""

def get_antecedent(pronoun):
    antecedent = ""
    if pronoun[0].lower() == 'he':
        antecedent = "John"  # Replace with actual antecedent from context
    elif pronoun[0].lower() == 'she':
        antecedent = "Mary"  # Replace with actual antecedent from context
    # Add more cases for other pronouns as needed
    return antecedent

def main():
    text = """
    John saw Mary at the store. She was buying groceries.
    He decided to greet her.
    """
    resolved_text = resolve_references(text)
    print("Original text:")
    print(text)
    print("\nResolved text:")
    print(resolved_text)

if __name__ == "__main__":
    main()
