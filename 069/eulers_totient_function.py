"""
Problem:
Find n for which n/phi(n) is a maximum
"""

"""
Soluion:
Implement a Sieve of Erastosthenes like loop which provides a list of factors for all numbers
Now for each number N, find numbers before it that have a null intersection with N's factors.
count such n and move on.
"""
