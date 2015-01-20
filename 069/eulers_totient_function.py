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
