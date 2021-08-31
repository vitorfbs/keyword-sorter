import spacy

nlp = spacy.load("pt_core_news_sm")
with open('text/source_text.txt', encoding='utf-8', mode="r") as f:
        text = f.read()
        f.close()

text = text.replace("#","").upper()
doc = nlp(text)

tokenized_suggestions = []

doc_size = len(doc)

for i in range(doc_size):

    if doc[i].pos_ == "NOUN" or doc[i].pos_ == "PROPN":
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

minimum_occurrence = 99
maximum_occurrence = 1

for suggestion in tokenized_suggestions_set:
    occurrence = tokenized_suggestions.count(suggestion)
    if occurrence > maximum_occurrence:
        maximum_occurrence = occurrence
    if occurrence < minimum_occurrence:
        minimum_occurrence = occurrence

for suggestion in tokenized_suggestions_set:
    occurrence = tokenized_suggestions.count(suggestion)
    if maximum_occurrence != minimum_occurrence and occurrence > minimum_occurrence:
        suggestion_with_occurrence = {
            "term": suggestion,
            "occurrence": occurrence
        }
        tokenized_suggestions_dictionaries.append(suggestion_with_occurrence)

tokenized_suggestions_dictionaries = sorted(tokenized_suggestions_dictionaries, key=lambda k: k['occurrence']) 
print(tokenized_suggestions_dictionaries)

entities_suggestions_set = list(set(entities_suggestions))

minimum_occurrence = 99
maximum_occurrence = 1

entities_suggestions_dictionaries = []

for suggestion in entities_suggestions_set:
    occurrence = entities_suggestions.count(suggestion)
    if occurrence > maximum_occurrence:
        maximum_occurrence = occurrence
    if occurrence < minimum_occurrence:
        minimum_occurrence = occurrence

for suggestion in entities_suggestions_set:
    occurrence = entities_suggestions.count(suggestion)
    if maximum_occurrence != minimum_occurrence and occurrence > minimum_occurrence:
        suggestion_with_occurrence = {
            "term": suggestion,
            "occurrence": occurrence
        }
        entities_suggestions_dictionaries.append(suggestion_with_occurrence)
print ("")

print(entities_suggestions_dictionaries)