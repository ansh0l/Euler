# -*- coding: utf-8 -*-

"""
Question:
    The primes 3, 7, 109, and 673, are quite remarkable.
    By taking any two primes and concatenating them in any order the result
    will always be prime. For example, taking 7 and 109, both 7109 and 1097
    are prime. The sum of these four primes, 792, represents the lowest sum
    for a set of four primes with this property.

    Find the lowest sum for a set of five primes for which any two primes
    concatenate to produce another prime.
"""

"""
DP -> Find sets of 3, sets of 4, and so on
"""

from collections import defaultdict
from itertools import combinations

with open("primes.million.txt", "r") as f:
    all_primes = [int(st) for st in f.read().split()]
primes = all_primes[1:1000]
largest_prime = all_primes[-1]
all_primes = set(all_primes)

def is_prime(n):
    if n < largest_prime:
        return n in primes
    elif n < primes[-1]**2:
        for p in primes:
            if p**2 > n:
                break
            if n % p == 0:
                return False
        return True

is_prime_joining = lambda x, y: is_prime(int(str(x) + str(y))) and is_prime(int(str(y) + str(x)))

def main():
    prime_pairs = ((a, b, c, d, e) for a in primes for b in primes for c in primes for d in primes for e in primes if a < b < c < d < e)
    for pair in prime_pairs:
        print pair
        if all(is_prime_joining(a, b) for a, b in combinations(pair, 2)):
            break

if __name__ == "__main__":
    main()
