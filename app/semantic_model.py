import spacy
import json
import re
import unidecode


class SemanticModel:
    def __init__(self):
        self.nlp = spacy.load("pt_core_news_lg")
        self.stopwords = self.nlp.Defaults.stop_words
        self.text = self.open_source_text()

    def open_source_text(self):
        with open('text/source_text.txt', encoding='utf-8', mode="r") as f:
            text = f.read()
            f.close()
   
        text = re.sub(r'[^\w\s]','', text)
        return unidecode.unidecode(text.lower())

    def process_text(self):
        return self.nlp(self.text)

    def generate_tokenized_suggestions(self, doc):
        tokenized_suggestions = []

        doc_size = len(doc)

        for i in range(doc_size):
            token = doc[i]
            if token.text not in self.stopwords:
                if token.pos_ == "PROPN" or token.pos_ == "NOUN":
                    if i-1 >= 0 and (doc[i-1].pos_ == "NOUN" or doc[i-1].pos_ == "PROPN"):
                        tokenized_suggestions.pop()
                        tokenized_suggestions.append(f"{doc[i-1].text} {doc[i].text}")
                    else:
                        tokenized_suggestions.append(doc[i].text)
        
        return tokenized_suggestions

    def generate_entities_suggestions(self, doc):
        entities_suggestions = []

        for ent in doc.ents:
            entities_suggestions.append(ent.text)
        
        return entities_suggestions

    def generate_tokenized_suggestions_json(self, tokenized_suggestions):
        tokenized_suggestions_set = list(set(tokenized_suggestions))

        tokenized_suggestions_dictionaries = []

        for suggestion in tokenized_suggestions_set:
            occurrence = len(re.findall(suggestion, self.text, re.IGNORECASE)) 
            suggestion_with_occurrence = {
                "term": unidecode.unidecode(suggestion),
                "occurrence": occurrence
            }
            tokenized_suggestions_dictionaries.append(suggestion_with_occurrence)

        tokenized_suggestions_dictionaries = sorted(tokenized_suggestions_dictionaries, key=lambda k: k['occurrence'], reverse=True) 

        with open('output/token_suggestions.json', 'w') as f:
            json.dump(tokenized_suggestions_dictionaries, f)

        return tokenized_suggestions_set

    def generate_entities_suggestions_json(self, entities_suggestions):
        entities_suggestions_set = list(set(entities_suggestions))

        entities_suggestions_dictionaries = []

        for suggestion in entities_suggestions_set:
            occurrence = len(re.findall(suggestion, self.text))
            suggestion_with_occurrence = {
                "term": unidecode.unidecode(suggestion),
                "occurrence": occurrence
            }
            entities_suggestions_dictionaries.append(suggestion_with_occurrence)

        with open('output/entities_suggestions.json', 'w') as f:
            json.dump(entities_suggestions_dictionaries, f)

        return entities_suggestions_set

    def generate_cross_suggestions_json(self, 
        tokenized_suggestions_set, 
        entities_suggestions_set):
        
        cross = []

        for token_suggestion in tokenized_suggestions_set:
            for entities_suggestion in entities_suggestions_set:
                if token_suggestion in entities_suggestion:
                    cross.append(token_suggestion)

            cross_set = list(set(cross))

            cross_suggestions = []

            for suggestion in cross_set:
                cross_suggestion = {
                    "term": unidecode.unidecode(suggestion),
                }
                cross_suggestions.append(cross_suggestion)

        with open('output/cross_suggestions.json', 'w') as f:
            json.dump(cross_suggestions, f)

    def main(self):
        doc = self.process_text()
        tokenized_suggestions = self.generate_tokenized_suggestions(doc)
        entities_suggestions = self.generate_entities_suggestions(doc)
        tokenized_suggestions_set = self.generate_entities_suggestions_json(tokenized_suggestions)
        entities_suggestions_set = self.generate_tokenized_suggestions_json(entities_suggestions)
        self.generate_cross_suggestions_json(tokenized_suggestions_set, entities_suggestions_set)
