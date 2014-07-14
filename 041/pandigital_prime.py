MAX = 1000000000

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
    """
    sum_of_digits = n*(n+1)/2
    Hence digits can't be "987654321" and "87654321", 
    since sum_of_digits will be divisible by 3 and numbers won't be primes'
    Hence max_digit = 7 and not 9
    """
    max_digit = 7
    digits = "7654321" 
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
