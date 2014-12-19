"""
Problem Statement:

By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.  

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime
with this property.  

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

""" 
Solution

Only those numbers, which have digits less than equal to 2 can be replaced
effectively Example: if number is 562133 then only on digits {2, 1} can there be
replacements, since minimum 8 replacements are needed.  If we try replacing any
other digit, they should have already been detected Also, in case of multiple
digits replacement the number should have repeat digits (only then it can
satisfy the rules) Finally, the number can either all replacement digits will
have to be greater than the key being replaced 

""" 
from collections import Counter

with open("primes.million.txt", "r") as f:
    all_primes = [int(p) for p in f.read().split()]

def find():
    for prime in all_primes:
        number = str(prime)
        count_digits = Counter([int(i) for i in list(str(prime))])
        keys = [key for key in count_digits.keys() if key < 3]
        for key in keys:
            count = 1
            replacements = [str(i) for i in range(key+1, 10)]
            for item in replacements:
                if int(number.replace(str(key), item)) in all_primes:
                    count += 1
            if count > 7:
                return prime

print find()
