import random

# Sample text data
text_data = "I like to eat pizza and I like to drink soda"

# Function to create a bigram model
def create_bigram_model(text):
    words = text.split()
    bigrams = [tuple(words[i:i+2]) for i in range(len(words)-1)]
    model = {}
    for word1, word2 in bigrams:
        if word1 in model:
            model[word1].append(word2)
        else:
            model[word1] = [word2]
    return model

# Function to generate text using the bigram model
def generate_text(model, num_words=10, seed=None):
    if seed is not None:
        random.seed(seed)
    current_word = random.choice(list(model.keys()))
    generated_text = [current_word]
    for _ in range(num_words - 1):
        if current_word in model:
            next_word = random.choice(model[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break
    return ' '.join(generated_text)

# Create a bigram model from the sample text data
bigram_model = create_bigram_model(text_data)

# Generate text using the bigram model
generated_text = generate_text(bigram_model, num_words=10)

print("Generated Text:", generated_text)
