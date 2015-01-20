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

MAX=10**3
dict_of_factors = defaultdict(lambda: set())
maximum = {"max": 1.0, "num": -1}

def phi(num):
    """
    Method for calculating phi of n
    Hunch is any would perform faster than a full blown intersection
    """
    # return sum(1 for i in range(2, n-1) if dict_of_factors[n].intersection(dict_of_factors[i]))
    # return 1 + sum(1 for iterator in range(2, num) if any(factor in dict_of_factors[num] for factor in dict_of_factors(iterator)))
    count = 1
    for iterator in range (2, num):
        for factor in dict_of_factors[iterator]:
            if factor in dict_of_factors[num]:
                count += 1
                break
    return count


t1 = time.time()

for num in range(2, MAX):
    i = num
    if num % 10**4 == 0:
        print num, time.time() - t1
    while i < MAX:
        dict_of_factors[i].add(num)
        i += num

t2 = time.time()
print "Phase 1 took: %s" % (t2-t1), "\n"

for num in range(2, MAX):
    totient = float(num)/float(phi(num))
    if num % 10**4 == 0:
        print num, time.time() - t2
    if totient > maximum["max"]:
        maximum["max"] = totient
        maximum["num"] = num

t3 = time.time()
print "Phase 2 took: %s" % (t3-t2), "\n"
print maximum
