"""
Dictionary in unix is present at /etc/dictionaries-common/words or in file/directory at /usr/share/dict
Actually, this is just a list of words which are commonly used in English language
"""

from itertools import product
from string import ascii_lowercase

key_options = [''.join(p) for p in product(ascii_lowercase, repeat=3)]

with open("/etc/dictionaries-common/words", "r") as f:
    dict_words = f.read().split()
    
with open("cipher.txt", "r") as f:
    ascii_codes = [int(code) for code in f.read().split(",")]

def get_full_key(small_key):
    len_needed, len_key = len(ascii_codes), len(small_key)
    return [ord(ch) for ch in small_key]  * (len_needed / len_key + len_needed % len_key)

def un_xor_values(ascii_codes, full_key):
    import pdb; pdb.set_trace()
    return ''.join([chr(a^b) for a, b in zip(ascii_codes, full_key)])

for key in key_options:
    full_key = get_full_key(key)
    possible_text = un_xor_values(ascii_codes, full_key)
    count_actual_words = 0
    possible_words = possible_text.split(",")
    if len(possible_words) < 2:
        possible_words = possible_text.split(",")
    elif len(possible_words) < 2:
        possible_words = possible_text.split(".")
    elif len(possible_words) < 2:
        possible_words = possible_text.split(" ")

    #print possible_text
    import pdb; pdb.set_trace()
    if len(possible_words) > 50:
        print len(possible_words), key
        print possible_words
        for idx, word in enumerate(possible_words):
            if word in dict_words:
                count_actual_words += 1
            elif idx > 10 and  count_actual_words < .5 * len(possible_words):
                break
        if count_actual_words > .8* len(possible_words):
            break
            print count_actual_words, key, float(count_actual_words)/len(possible_words)*100
