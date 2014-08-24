"""
Only those numbers, which have digits less than equal to 2 can be replaced effectively
Example:
    if number is 562133
        then only on digits {2, 1} can there be replacements, since minimum 8 replacements are needed.
        If we try replacing any other digit, they should have already been detected
Also, in case of multiple digits replacement the number should have repeat digits (only then it can satisfy the rules)
"""

#class Prime():
#    def __init__(self, number):
#        self.number = int(number)
#        self.is_visited = False

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
            #replacements = set("0123456789".replace(str(key), ""))
            replacements = [str(i) for i in range(key+1, 10)]
            for item in replacements:
                if int(number.replace(str(key), item)) in all_primes:
                    count += 1
            if count > 7:
                return prime
    
print find()
