import spacy
import json
import re
import unidecode


nlp = spacy.load("pt_core_news_lg")
stopwords = nlp.Defaults.stop_words6

with open('text/source_text.txt', encoding='utf-8', mode="r") as f:
        text = f.read()
        f.close()

text = unidecode.unidecode(text.lower())
doc = nlp(text)

tokenized_suggestions = []

doc_size = len(doc)

for i in range(doc_size):
    token = doc[i]
    if token.text not in stopwords:
        if token.pos_ == "PROPN" or token.pos_ == "NOUN":
            if i-1 >= 0 and (doc[i-1].pos_ == "NOUN" or doc[i-1].pos_ == "PROPN"):
                tokenized_suggestions.pop()
                tokenized_suggestions.append(f"{doc[i-1].text} {doc[i].text}")
            else:
                tokenized_suggestions.append(doc[i].text)

entities_suggestions = []

for ent in doc.ents:
    entities_suggestions.append(ent.text)

tokenized_suggestions_set = list(set(tokenized_suggestions))

tokenized_suggestions_dictionaries = []

for suggestion in tokenized_suggestions_set:
    occurrence = len(re.findall(suggestion, text, re.IGNORECASE)) 
    suggestion_with_occurrence = {
        "term": unidecode.unidecode(suggestion),
        "occurrence": occurrence
    }
    tokenized_suggestions_dictionaries.append(suggestion_with_occurrence)

tokenized_suggestions_dictionaries = sorted(tokenized_suggestions_dictionaries, key=lambda k: k['occurrence'], reverse=True) 

with open('output/token_suggestions.json', 'w') as f:
    json.dump(tokenized_suggestions_dictionaries, f)

entities_suggestions_set = list(set(entities_suggestions))

entities_suggestions_dictionaries = []

for suggestion in entities_suggestions_set:
    occurence = len(re.findall(suggestion, text))
    suggestion_with_occurrence = {
        "term": unidecode.unidecode(suggestion),
        "occurrence": occurrence
    }
    entities_suggestions_dictionaries.append(suggestion_with_occurrence)

with open('output/entities_suggestions.json', 'w') as f:
    json.dump(entities_suggestions_dictionaries, f)

double_blind = []

for token_suggestion in tokenized_suggestions_set:
    for entities_suggestion in entities_suggestions_set:
        if token_suggestion in entities_suggestion:
           double_blind.append(token_suggestion)

double_blind_set = list(set(double_blind))

double_blind_suggestions = []

for suggestion in double_blind_set:
    double_blind_suggestion = {
        "term": unidecode.unidecode(suggestion),
    }
    double_blind_suggestions.append(double_blind_suggestion)

with open('output/double_blind_suggestions.json', 'w') as f:
    json.dump(double_blind_suggestions, f)