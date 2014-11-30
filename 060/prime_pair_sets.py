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
Solution:

This looks like a graph problem so it seems to me.

Essentially, if we connect every two vertices, which have this property
    (eg 3 -> 7, 3-> 109, 3 -> 673) and so on, then we are looking for a
    completely connected graph with 5 vertices (i.e., the number of edges
    must be 5C2 = 10 between the 5 edges)

If we have prime numbers less than X, then total edges = O(n**2)
The assumption to be made is that most of them won't exist, though this
ensures the TimeComplexity is O(n**2) always (don't think TC matters much)
"""

from collections import defaultdict

def is_prime(n, primes):
    for p in primes:
        if n % p == 0:
            return False
    return True

joining = lambda x, y: (int(str(x) + str(y)), int(str(y) + str(x)))

def get_node_dict(primes):
    length = len(primes)
    d = defaultdict(lambda: [])
    for i in range(1, length):
        for j in range(0, i):
            joins = joining(i, j)
            if is_prime(joins[0], primes) and is_prime(joins[1], primes):
                d[i].append(j)
    print "\n".join("%s: %s" % (str(k), str(v)) for k, v in d.items())

def main():
    with open("primes.million.txt", "r") as f:
        primes = [int(st) for st in f.read().split()]
    primes = primes[:1000]
    get_node_dict(primes)

if __name__ == "__main__":
    main()
