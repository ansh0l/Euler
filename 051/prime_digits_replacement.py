"""
Only those numbers, which have digits less than equal to 2 can be replaced effectively
Example:
    if number is 562133
        then only on digits {2, 1} can there be replacements, since minimum 8 replacements are needed.
        If we try replacing any other digit, they should have already been detected
Also, the number should have repeat digits (only then it can satisfy the rules)
"""

#class Prime():
#    def __init__(self, number):
#        self.number = int(number)
#        self.is_visited = False

with open("primes.million.txt", "r") as f:
    all_primes = [int(p) for p in f.read().split()]

for prime in all_primes:
    if prime 

numbers = []

if all(num in all_primes for num in numbers):
    print numbers
