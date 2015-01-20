"""
Problem:
Find n for which n/phi(n) is a maximum
"""

"""
Soluion:
Implement a Sieve of Erastosthenes like loop which provides a list of factors for all numbers
Now for each number N, find numbers before it that have a null intersection with N's factors.
count such n and move on.

Time Complexity: 
O(n log log n) for sieve => n/2 + n/3 + n/4 + n/5 + n/6 + n/7 + ...
                         => n*(1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + ...)
                         => n log(log(n))  -  check http://stackoverflow.com/a/2582776/1860929
for finding factors
    => sigma((k-1)*len(factors(k))) for k = 2 to N
    => O(k**2 * log(k))

"""

import time

from collections import defaultdict

MAX=10**6
dict_of_factors = defaultdict(lambda: set())

t1 = time.time()

for num in range(2, MAX):
    i = num
    if num % 10**4 == 0:
        print num, time.time() - t1
    while i < MAX:
        dict_of_factors[i].add(num)
        i += num

t2 = time.time()
print "Phase 1 took: %s" % (t2-t1)

def phi(n):
    """
    Method for calculating phi of n
    Hunch is any would perform faster than a full blown intersection
    """
    # return sum(1 for i in range(2, n-1) if dict_of_factors[n].intersection(dict_of_factors[i]))
    return sum(1 for i in range(2, n-1) if any(f in dict_of_factors[n] for f in dict_of_factors(i)))
