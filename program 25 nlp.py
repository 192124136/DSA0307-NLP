import openai

# Set your OpenAI API key
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

def generate_text(prompt, max_tokens=50):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the GPT-3 engine you prefer
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

def main():
    prompt = "Once upon a time"
    generated_text = generate_text(prompt)
    print("Generated text:")
    print(generated_text)

if __name__ == "__main__":
    main()
