# Make sure we include the provided function for reading the files
import files as f

def split_into_sentences(text):
    sentences = []
    # TODO: split it into sentences - hard!!!
    sentences.split(".")
    return sentences

# Removes all punctuation other than ' and space from the text
def remove_punctuation(text):
    keep = " 'abcdefghijklmnopqrstuvwxyz"
    keep += keep.upper()

    clean_text = ""
    for char in text:
        if char in keep:
            clean_text += char
        else:
            clean_text += " "

    return clean_text

def find_proper_nouns(sentence):
    # TODO: figure out if it is a proper noun and add it to list
    pass

def create_dictionary():
    dictionary = []
    proper_nouns = []

    for file_num in range(1,2):
        # Read a file
        text = f.read_file(file_num)

        sentences = split_into_sentences(text)

        for sentence in sentences:
            find_proper_nouns(sentence)

            sentence = remove_punctuation(sentence)

            words = sentence.split()

            for word in words:
                if word in proper_nouns:
                    continue
                elif "'" in word:
                    continue
                elif word == word.upper():
                    continue
                elif len(word) == 5 and word not in dictionary:
                    dictionary.append(word.lower())


    # print proper_nouns
    # print dictionary
    return dictionary

sent ="The color of animals is by no means a matter of chance; it depends on many considerations,but in the majority of cases tends to protect the animal from danger by rendering it less conspicuous. Perhaps it may be said that if coloring is mainly protective, there ought to be but few brightly colored animals."
print(sent)
print(remove_punctuation(sent))