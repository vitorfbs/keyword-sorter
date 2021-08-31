import spacy
sp = spacy.load('pt_core_news_lg')

all_stopwords = sp.Defaults.stop_words

print(all_stopwords)