import json
from difflib import get_close_matches


DICT = json.load(open('data.json', 'r'))


def LOOKUP(LOOKUP_WORD):
    LOOKUP_WORD = LOOKUP_WORD.lower()
    if LOOKUP_WORD in DICT:
        OUTPUT = (DICT[LOOKUP_WORD])
        i = 1
        for ITEM in OUTPUT:
            print (i,' ',ITEM)
            i += 1
    elif len(get_close_matches(LOOKUP_WORD, DICT.keys())) > 0:
        print ('Did you mean %s instead?' %get_close_matches(LOOKUP_WORD, DICT.keys())[0])
    else:
        print ('The word does not exist.')

while True:
    WORD = input('What is the WORD to lookup: ')
    LOOKUP(WORD)