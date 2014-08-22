with open("primes.million.txt", "r") as f:
    primes = [int(p) for p in f.read().split()]

MILLION = 1000000
TENMILLION = MILLION * 10

def is_prime(number):
    for prime in primes:
        if prime**2 > number:
            break
        elif number % prime == 0: 
            return False
    return True 

with open("primes.ten.million.txt", 'w') as f:
    for p in primes:
        f.write(' %s' % str(p))

number = MILLION + 1
new_primes = []
while number < TENMILLION:
    if is_prime(number):
        new_primes.append(number)
    if len(new_primes) == 10000:
        with open("primes.ten.million.txt", 'a') as f:
            #f.write(' ' + ' '.join(new_primes))
            for p in new_primes:
                f.write(' %s' % str(p))
        new_primes = []

    number += 2
    pass
