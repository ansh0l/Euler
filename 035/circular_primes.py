primes = [2]
LIMIT = 1000000

def get_prime_numbers():
    candidate = 3
    while candidate < LIMIT:
        can_be_prime = True
        for prime in primes:
            if prime**2 > candidate:
                break
            elif candidate % prime == 0:
                can_be_prime = False
                break
        if can_be_prime:
            primes.append(candidate)
        candidate += 2

def rotate(string, n):
    return string[n:] + string[:n]

def is_circular_prime(n):
    str_n = rotate(str(n), 1)
    can_be_circular_prime = True
    while int(str_n) != n:
        if int(str_n) not in primes:
            can_be_circular_prime = False
            break
        str_n = rotate(str_n, 1)
    return can_be_circular_prime
    
get_prime_numbers()

circular_primes = []
for p in primes:
    if is_circular_prime(p):
        circular_primes.append(p)

print circular_primes
