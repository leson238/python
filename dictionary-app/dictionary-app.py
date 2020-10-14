import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    else:
        predict_word = get_close_matches(word, data.keys(), n=1)[0]
        if predict_word:
            option = input('Do you mean {} instead? Type in Y or N: '.format(predict_word))
            if option.lower() == 'n':
                return 'Cannot find your word.'
            else:
                return data[predict_word]
        else:
            return '{} does not exist'.format(word)


word = input('Enter word: ')
print(translate(word))
