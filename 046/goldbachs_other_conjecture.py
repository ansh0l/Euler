"""
composite_number = p + 2*(k**2), where p is prime, k is any +ve integer
or composite = a + b, where a belongs to primes, and b belongs to set of 2*(k**2), double_squares
Hence maintain two sets, one of primes, other of double_squares
"""

"""primes are ascending order, doubles_sqaures in descending"""
primes = [2]
double_squares = [2, 8]

def is_prime(n):
    return all(n % p for p in primes if p**2 <= n) 

def is_odd(n):
    return n % 2 == 1

def holds_goldbach_conjecture(n):
    holds = False
    for ds in double_squares:
        if ds > n or holds: 
            break
        for p in primes:
            if p + ds > n: 
                break
            elif p + ds == n:
                holds = True
                break
    print n, holds
    return holds 

def main():
    n = 3
    while True:
        double_squares.append(2*(n**2))
        if is_prime(n):
            primes.append(n)
        elif is_odd(n) and not holds_goldbach_conjecture(n):
            break
        n += 1

if __name__ == "__main__":
    main()
