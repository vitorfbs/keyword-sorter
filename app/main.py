import unidecode

def open_source_text():
    with open('source_text.txt', encoding='utf-8', mode="r") as f:
        text = f.read()
        f.close()
    return text

def generate_terms(text):
    decoded_text = unidecode.unidecode(text)
    return decoded_text.split(" ")

text = open_source_text()
terms = generate_terms(text)
print(terms)