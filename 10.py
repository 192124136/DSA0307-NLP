from nltk.tag import brill, brill_trainer

# Define transformation rules
def transformation_rules():
    return [
        brill.WordRule(r'^-?[0-9]+(.[0-9]+)?$', [(1, 'CD')]),
        brill.WordRule(r'.*ly$', [(1, 'RB')]),
        brill.WordRule(r'.*', [(1, 'NN')])
    ]

# Train the transformation-based tagger
def train_transformation_tagger(tagged_corpus):
    templates = brill.brill24()
    trainer = brill_trainer.BrillTaggerTrainer(initial_tagger=nltk.DefaultTagger('NN'),
                                               templates=templates,
                                               trace=3)
    return trainer.train(tagged_corpus, transformation_rules())

# Example tagged corpus
tagged_corpus = brown.tagged_sents(categories='news')

# Train transformation-based tagger
transformation_tagger = train_transformation_tagger(tagged_corpus)

# Example sentence
sentence = "The quick brown fox jumps over the lazy dog"
tokenized_sentence = nltk.word_tokenize(sentence)

# Perform transformation-based tagging
tagged_sentence = transformation_tagger.tag(tokenized_sentence)
print("Transformation-based Tagging Result:")
print(tagged_sentence)
