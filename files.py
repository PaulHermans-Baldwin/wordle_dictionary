"""
---------------------------------------------------

    DO NOT EDIT CODE IN THIS FILE!


    This code is written for you because it is beyond the scope of
    what you have learned so far. You should write all your code
    in the wordle_dictionary.py file.

    There is also NO NEED TO COPY any code from this file!


 ------------------------------------------------------    """

import urllib.request


# Read the specified file, and return the text as a single element
# containing its contents.
def read_file(passage_number):
    file_path = 'https://raw.githubusercontent.com/PaulHermans-Baldwin/wordle_dictionary/master/Content/passage_' + \
                str(passage_number) + '.txt'
    with urllib.request.urlopen(file_path) as response:
        text_passage = response.read().decode('utf-8')

    return text_passage