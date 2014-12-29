"""
Dictionary in unix is present at /etc/dictionaries-common/words or in file/directory at /usr/share/dict
Actually, this is just a list of words which are commonly used in English language
"""

from itertools import product
from string import ascii_lowercase, ascii_letters, digits

key_options = [''.join(p) for p in product(ascii_lowercase, repeat=3)]

with open("/etc/dictionaries-common/words", "r") as f:
    dict_words = set(f.read().split())
    
with open("cipher.txt", "r") as f:
    ascii_codes = [int(code) for code in f.read().split(",")]

len_needed = len(ascii_codes)
len_key = 3

def get_full_key(small_key):
    key = [ord(ch) for ch in small_key]
    return key * (len_needed/len_key) + key[:len_needed%len_key]

def un_xor_values(ascii_codes, full_key):
    return ''.join([chr(a^b) for a, b in zip(ascii_codes, full_key)])

characters = set(ascii_letters + digits)



for key in key_options:
    full_key = get_full_key(key)
    possible_text = un_xor_values(ascii_codes, full_key)
    count_actual_words = 0
    separators = ",. \n"

    possible_words = [possible_text]
    for sep in separators:
        old_possible_words = possible_words
        possible_words = []
        for word in old_possible_words:
            possible_words += word.split(sep)

    if len(possible_words) > 50:
        for idx, word in enumerate(possible_words):
            if word in dict_words:
                count_actual_words += 1

        if count_actual_words > .5* len(possible_words):
            print count_actual_words, key, float(count_actual_words)/len(possible_words)*100
            print possible_text
