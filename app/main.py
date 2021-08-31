import unidecode

def open_source_text():
    #with open('source_text.txt', encoding='utf-8', mode="r") as f:
    with open("/Users/regisdarosa/PycharmProjects/keyword-sorter/app/text/source_text.txt", encoding='utf-8', mode="r") as file:
        text = file.read()
        file.close()
    return text

def generate_terms(text):
    decoded_text = unidecode.unidecode(text)
    return decoded_text.lower().split(" ")

def remove_word_connections_from_terms(terms):
    terms_without_connections_list = []
    words_to_remove = ["para","o","os","a","as","um","uns","uma","umas","a","ao","aos","de","do","dos","da","das","dum","duns","duma","dumas","em","no","nos","na","nas","num","nuns","numa","numas","por","per","pelo","pelos","pela","pelas","e","ou","entao","senao"]
    for term in terms:
        if term not in words_to_remove:
            terms_without_connections_list.append(term)
    return terms_without_connections_list

def calc(terms_without_connections):
    textSize = len(terms_without_connections)
   
    return ""        

text = open_source_text()
terms = generate_terms(text)
terms_without_connections = remove_word_connections_from_terms(terms)

print(terms_without_connections)