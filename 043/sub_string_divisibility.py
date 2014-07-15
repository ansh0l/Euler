from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]

def generate_0to9_pandigital_numbers():
    pandigitals = []
    digits = "0123456789"
    for permutation in permutations(digits, len(digits)):
        number_in_string = ''.join(permutation)
        if number_in_string[0] != '0':
            pandigitals.append(number_in_string)
    return pandigitals

def has_sub_string_divisibility(string_n):
    i = 0
    has_property = True
    if len(primes) != len(string_n) - 3:
        has_property = False
    else:
        while i < len(primes):
            if int(string_n[i+1:i+4]) % primes[i] != 0:
                has_property = False
                break
            i += 1
    return has_property

def main():
    pandigitals = generate_0to9_pandigital_numbers()
    sigma = 0
    for p in pandigitals:
        if has_sub_string_divisibility(p):
            sigma += int(p)
    print sigma

if __name__ == "__main__":
    main()
