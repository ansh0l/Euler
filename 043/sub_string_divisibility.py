from itertools import permutations

def generate_0to9_pandigital_numbers():
    pandigital = []
    digits = "0123456789"
    for permutation in permutations(digits, max_digit):
        number_in_string = ''.join(permutation)
        if number_in_string[0] == '0':
            continue
        pandigital.append(int(number_in_string))
    return pandigital
