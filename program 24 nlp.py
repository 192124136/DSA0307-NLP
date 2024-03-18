import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download NLTK resources if not already downloaded
nltk.download('punkt')

def recognize_dialog_acts(dialog):
    sentences = sent_tokenize(dialog)
    dialog_acts = []

    for sentence in sentences:
        tokens = word_tokenize(sentence.lower())
        dialog_act = classify_dialog_act(tokens)
        dialog_acts.append((sentence, dialog_act))

    return dialog_acts

def classify_dialog_act(tokens):
    greetings = ['hello', 'hi', 'hey']
    farewells = ['goodbye', 'bye', 'see you']
    questions = ['what', 'where', 'when', 'who', 'why', 'how']
    statements = ['i think', 'i believe', 'in my opinion']

    if any(token in greetings for token in tokens):
        return 'GREETING'
    elif any(token in farewells for token in tokens):
        return 'FAREWELL'
    elif any(token in questions for token in tokens):
        return 'QUESTION'
    elif any(token in statements for token in tokens):
        return 'STATEMENT'
    else:
        return 'OTHER'

def main():
    dialog = """
    Speaker 1: Hi, how are you?
    Speaker 2: I'm doing well, thank you. How about you?
    Speaker 1: Goodbye then, have a great day!
    """
    dialog_acts = recognize_dialog_acts(dialog)

    print("Dialog Acts:")
    for utterance, dialog_act in dialog_acts:
        print(f"{utterance.strip()} - {dialog_act}")

if __name__ == "__main__":
    main()
