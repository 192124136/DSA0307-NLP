import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

def calculate_coherence(text):
    sentences = sent_tokenize(text)
    word_tokens = [word.lower() for sentence in sentences for word in word_tokenize(sentence) if word.isalnum()]
    filtered_tokens = [word for word in word_tokens if word not in stopwords.words('english')]

    bigram_measures = BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(filtered_tokens)
    pmi = finder.score_ngrams(bigram_measures.pmi)

    coherence_score = sum(score for bigram, score in pmi) / len(pmi)
    return coherence_score

def main():
    text = """
    Coherence in writing means that all the ideas in a paragraph flow smoothly from one sentence to the next. 
    With each sentence building on the previous one and leading logically to the next. 
    Achieving coherence requires paying attention to the organization and development of ideas.
    """
    coherence_score = calculate_coherence(text)
    print("Coherence score:", coherence_score)

if __name__ == "__main__":
    main()
