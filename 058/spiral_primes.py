"""
(1)
delta = 2, numbers_on_diagonal = 3, 5, 7, 9
delta = 4, numbers_on_diagonal = 13, 17, 21, 25
delta = 6, numbers_on_diagonal = 31, 37, 43, 49
"""

with open("primes.million.txt", "r") as f:
    primes = [int(p) for p in f.read().split()]

def is_prime(number):
    for prime in primes:
        if prime**2 > number:
            break
        elif number % prime == 0: 
            return False
    return True 

side_length = 3
CORNERS = 4
delta = 4
number = 9

MILLION = 1000000

diagonal_numbers = 5 #[1, 3, 5, 7, 9] 
prime_diagonal_numbers = 3 #[3, 5, 7]
while diagonal_numbers < 10 * prime_diagonal_numbers:
    side_length += 2 # 2 edges added every spiral
    for c in range(CORNERS):
        number += delta
        if number in primes or ( number > MILLION and is_prime(number)):
            prime_diagonal_numbers += 1
        diagonal_numbers += 1
    delta += 2
print side_length 
