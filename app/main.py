import unidecode
from collections import Counter


def open_source_text():
    #with open('source_text.txt', encoding='utf-8', mode="r") as f: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    with open("/Users/regisdarosa/PycharmProjects/keyword-sorter/app/text/source_text.txt", encoding='utf-8', mode="r") as file:
        text = file.read()
        file.close()
    return text

def generate_terms(text):
    decoded_text = unidecode.unidecode(text)
    return decoded_text.lower().split(" ")

def remove_words_connections_from_terms(terms):
    terms_without_connections_list = []
    words_to_remove = ["como","que","esta", "foi", "com","se","para","o","os","a","as","um","uns","uma","umas","a","ao","aos","de","do","dos","da","das","dum","duns","duma","dumas","em","no","nos","na","nas","num","nuns","numa","numas","por","per","pelo","pelos","pela","pelas","e","ou","entao","senao"]
    
    for term in terms:
        if term not in words_to_remove:
            terms_without_connections_list.append(term)
    return terms_without_connections_list

def get_most_common_words(terms_without_connections):

    counter = Counter(terms_without_connections)
    ocurrences_number = Counter(terms_without_connections).most_common(1)[0][1]
    
    most_occur = counter.most_common(ocurrences_number)

    return most_occur;        

text = open_source_text()
terms = generate_terms(text)
terms_without_connections = remove_words_connections_from_terms(terms)
most_commun_ocurrences = get_most_common_words(terms_without_connections)

print(most_commun_ocurrences)