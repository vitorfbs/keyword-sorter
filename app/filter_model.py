import unidecode
import json
import re
from collections import Counter

class FilterModel():
    def open_source_text(self):
        with open("text/source_text.txt", encoding='utf-8', mode="r") as file:
            text = file.read()
            file.close()
        return text

    def generate_terms(self, text):
        decoded_text = unidecode.unidecode(text)
        return decoded_text.lower().split(" ")

    def remove_words_connections_from_terms(self, terms):
        terms_without_connections_list = []
        words_to_remove = ["como","que","esta", "foi", "com","se","para","o","os","a","as","um","uns","uma","umas","a","ao","aos","de","do","dos","da","das","dum","duns","duma","dumas","em","no","nos","na","nas","num","nuns","numa","numas","por","per","pelo","pelos","pela","pelas","e","ou","entao","senao"]

        for term in terms:
            term = re.sub(r'[^\w\s]','', term)
            term = re.sub(" \d+", " ", term)
            if term not in words_to_remove and len(term) > 2 and term != "":
                terms_without_connections_list.append(term)
        return terms_without_connections_list

    def get_most_common_words(self, terms_without_connections):

        counter = Counter(terms_without_connections)
        ocurrences_number = Counter(terms_without_connections).most_common(1)[0][1]
        
        most_occur = counter.most_common(ocurrences_number)

        return most_occur;

    def generate_suggestion_json(self, suggestions):
        suggestions_dict = []
        for suggestion in suggestions:
            suggestion_with_occurrence = {
                    "term": suggestion[0],
                    "occurrence": suggestion[1]
                }
            suggestions_dict.append(suggestion_with_occurrence)
        
        with open('output/filter_suggestions.json', 'w') as f:
            json.dump(suggestions_dict, f)

    def main(self):
        text = self.open_source_text()
        terms = self.generate_terms(text)
        terms_without_connections = self.remove_words_connections_from_terms(terms)
        most_commun_ocurrences = self.get_most_common_words(terms_without_connections)
        self.generate_suggestion_json(most_commun_ocurrences)