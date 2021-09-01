import json

from filter_model import FilterModel
from semantic_model import SemanticModel

filter_model = FilterModel()
semantic_model = SemanticModel()

filter_model.main()
semantic_model.main()

with open('output/cross_suggestions.json') as json_file:
    cross_suggestions = json.load(json_file)

with open('output/entities_suggestions.json') as json_file:
    entities_suggestions = json.load(json_file)

with open('output/token_suggestions.json') as json_file:
    token_suggestions = json.load(json_file)

with open('output/filter_suggestions.json') as json_file:
    filter_suggestions = json.load(json_file)

junction_suggestions = []


for filter_suggestion in filter_suggestions:
    occurrence_increment = 0
    for token_suggestion in token_suggestions:
        if filter_suggestion["term"] in token_suggestion["term"]:
            occurrence_increment = occurrence_increment + 1
    for entity_suggestion in entities_suggestions:
        if filter_suggestion["term"] in token_suggestion["term"]:
            occurrence_increment = occurrence_increment + 1
    print(f"{filter_suggestion} : {occurrence_increment}")
    if occurrence_increment > 0:
        junction_suggestion = {
            "term": filter_suggestion["term"],
            "occurrence": filter_suggestion["occurrence"] + occurrence_increment
        }
        junction_suggestions.append(junction_suggestion)

print(junction_suggestions)

with open('output/junction_suggestions.json', 'w') as f:
            json.dump(junction_suggestions, f)

