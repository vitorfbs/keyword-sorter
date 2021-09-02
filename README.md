# Keyword Sorter
**made by Archimedes**

## How to run

First, you will need to install the project dependancies available in the requirements file.

After you install them, run the following command (this may take a while):
```
python -m spacy download pt_core_news_lg
```
This command will install the Natural Language Processing model for Spacy in Portuguese, which will
be used in the Keyword Sorter project for the Semantic Model.

To run the project, run:
```
python main.py
```
After running these commands, your report will be available in the output folder, together with the 
JSON files for each model's suggestions.

If you have any problem with both the installation and usage of Spacy, or the installation of 
unidecode for this project, please refer to the official documentation for both libraries:

SPACY

https://spacy.io/usage

UNIDECODE

https://pypi.org/project/Unidecode/