import spacy
import json
import re
import unidecode

nlp = spacy.load("pt_core_news_lg")

stopwords = nlp.Defaults.stop_words

with open('text/source_text.txt', encoding='utf-8', mode="r") as f:
        text = f.read()
        f.close()

text = text.lower()
doc = nlp(text)

tokenized_suggestions = []

doc_size = len(doc)

for i in range(doc_size):
    token = doc[i]
    if token.text not in stopwords:
        if token.pos_ == "PROPN" or token.pos_ == "NOUN":
            print(token.text + " " + token.pos_)
            if i-1 >= 0 and (doc[i-1].pos_ == "NOUN" or doc[i-1].pos_ == "PROPN"):
                tokenized_suggestions.pop()
                tokenized_suggestions.append(f"{doc[i-1].text} {doc[i].text}")
            else:
                tokenized_suggestions.append(doc[i].text)

print(tokenized_suggestions)

entities_suggestions = []

for ent in doc.ents:
    entities_suggestions.append(ent.text)

print (entities_suggestions)

print ("")

print ("NOW WITH UNIQUE LISTS")

tokenized_suggestions_set = list(set(tokenized_suggestions))

print(tokenized_suggestions_set)

tokenized_suggestions_dictionaries = []

for suggestion in tokenized_suggestions_set:
    occurrence = len(re.findall(suggestion, text, re.IGNORECASE)) 
    suggestion_with_occurrence = {
        "term": unidecode.unidecode(suggestion),
        "occurrence": occurrence
    }
    tokenized_suggestions_dictionaries.append(suggestion_with_occurrence)

tokenized_suggestions_dictionaries = sorted(tokenized_suggestions_dictionaries, key=lambda k: k['occurrence'], reverse=True) 
print(tokenized_suggestions_dictionaries)

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
print ("")

print(entities_suggestions_dictionaries)

double_blind = []

for token_suggestion in tokenized_suggestions_set:
    for entities_suggestion in entities_suggestions_set:
        if token_suggestion in entities_suggestion:
           double_blind.append(token_suggestion)

print(set(double_blind))