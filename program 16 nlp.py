import spacy

# Load the SpaCy English language model
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text using SpaCy
    doc = nlp(text)
    
    # Iterate over the entities found in the text
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    
    return entities

# Example usage
text = "Apple is looking at buying U.K. startup for $1 billion"
entities = perform_ner(text)
print("Named Entities:")
for entity, label in entities:
    print(f"{entity}: {label}")
