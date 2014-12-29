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
    primes = [int(st) for st in f.read().split()]
primes = primes[1:1000]

def is_prime(n):
    for p in primes:
        if p**2 > n:
            break
        if n % p == 0:
            return False
    return True

is_prime_joining = lambda x, y: is_prime(int(str(x) + str(y))) and is_prime(int(str(y) + str(x)))


def main():
    one, two, three, four, five = primes, set(), set(), set(), set()
    for p in primes:
        for o in one:
            if is_prime_joining(p, o):
                two.add((p, o))
    print "twos done", p, len(two)
    for p in primes:
        for t in two:
            if all(is_prime_joining(x, y) for x, y in combinations(t + (p,), 2)):
                three.add(t + (p,))
    print "threes done"
    for p in primes:
        for t in three:
            if all(is_prime_joining(x, y) for x, y in combinations(t + (p,), 2)):
                four.add(t + (p,))
    print "fours done"
    for p in primes:
        for f in four:
            if all(is_prime_joining(x, y) for x, y in combinations(f + (p,), 2)):
                print f + (p,)
                return
                five.add(f + (p,))

if __name__ == "__main__":
    main()
