"""
composite_number = p + 2*(k**2), where p is prime, k is any +ve integer
or composite = a + b, where a belongs to primes, and b belongs to set of 2*(k**2), double_squares
Hence maintain two sets, one of primes, 
"""

primes = [2]
double_squares = [1]



def is_prime(n):
    can_be_prime = True
    for p in primes:
        if p**2 > n:
            break
        elif n % p == 0:
            can_be_prime = False
            break
    return can_be_prime

def holds_goldbach_conjecture(n):
    


def main():
    n = 3
    while True:
        if is_prime(n):
            primes.append(n)
        else:
            double_squares.insert(2*(n**2), 0)
        if not holds_goldbach_conjecture(n):
            print n
            break
        n += 1
    
