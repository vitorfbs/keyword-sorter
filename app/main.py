import unidecode

def open_source_text():
    with open('text/source_text.txt', encoding='utf-8', mode="r") as f:
        text = f.read()
        f.close()
    return text

def generate_terms(text):
    decoded_text = unidecode.unidecode(text.upper())
    terms = strip_text(decoded_text.split(" "))
    
    return terms

def strip_text(terms):
    with open('collections/filter.txt', encoding='utf-8', mode="r") as f:
        filters = f.read()
        f.close()

    filters = filters.upper()
    filters = filters.split(",")

    for filter in filters:
        terms = [word for word in terms if word != filter]
    return terms

text = open_source_text()
terms = generate_terms(text)
print(terms)