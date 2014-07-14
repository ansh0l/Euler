MAX = 1000000000

def is_pandigital(n):
    string_n = str(n)
    len_n = len(string_n)
    if len_n == 9:
        return set(string_n) == set('123456789')
    elif len_n == 8:
        return set(string_n) == set('12345678')
    elif len_n == 7:
        return set(string_n) == set('1234567')
    elif len_n == 6:
        return set(string_n) == set('123456')
    elif len_n == 5:
        return set(string_n) == set('12345')
    elif len_n == 4:
        return set(string_n) == set('1234')
    return False

def get_primes():
    primes = [2]
    candidate = 3
    while candidate**2 < MAX:
        can_be_prime = True
        for p in primes:
            if p**2 > candidate:
                break
            elif candidate % p == 0:
                can_be_prime = False
                break
        if can_be_prime:
            primes.append(candidate)
        candidate += 2
    return primes

def is_prime(n, primes):
    can_be_prime = True
    for p in primes:
        if p**2 > n:
            break
        elif n % p == 0:
            can_be_prime = False
            break
    return can_be_prime

def main():
    from itertools import permutations
    primes = get_primes()
    max_digit = 9
    digits = [int(d) for d in "987654321"]
    digits = "987654321"
    biggest_pdp_found = False
    while not biggest_pdp_found:
        for permutation in permutations(digits, max_digit):
            number = int(''.join(permutation))
            if is_prime(number, primes):
                biggest_pdp_found = True
                print number
                break
        if not biggest_pdp_found:
            digits = digits[1:]
            max_digit -= 1

if __name__ == "__main__":
    main()
