from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, model_name="Helsinki-NLP/opus-mt-en-fr"):
    # Load pre-trained model and tokenizer
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Perform translation
    outputs = model.generate(**inputs)

    # Decode the translated text
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

def main():
    # Input English text
    english_text = "Hello, how are you?"

    # Translate English text to French
    french_text = translate_text(english_text)

    # Output translated text
    print("Translated French text:")
    print(french_text)

if __name__ == "__main__":
    main()
