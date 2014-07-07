import math
import pdb

prime_numbers = [2, 3]

def get_next_prime(**kwargs):
    new_primes_needed, primes_found = 1, 0
    global prime_numbers
    if kwargs.has_key("n") and type(kwargs["n"]) == int and kwargs["n"] > 1:
        new_primes_needed = kwargs["n"]
    candidate = prime_numbers[-1] + 2
    while primes_found < new_primes_needed:
        candidature_holds = True
        for prime in prime_numbers:
            if prime**2 > candidate:
                break
            elif candidate % prime == 0:
                candidature_holds = False
                break
        if candidature_holds:
            prime_numbers.append(candidate)
            primes_found += 1
        candidate += 2

def triangle_number(n):
    return n * (n+1) / 2

def get_divisor_count(n):
    multiplicity, count = {}, 1
    while prime_numbers[-1]**2 < n:
        get_next_prime()
    for prime in prime_numbers:
        dividend, count_for_prime = n, 1
        while dividend % prime == 0:
            multiplicity[prime] = count
            count_for_prime += 1
            dividend /= prime
        count *= count_for_prime
    return count

def main():
    n = 500
    get_next_prime(n = 500)
    count_divisors, triangle = 1, 1
    while count_divisors < 500:
        triangle = triangle_number(n)
        count_divisors = get_divisor_count(triangle)
        print triangle, count_divisors, n
        n += 1

main()
