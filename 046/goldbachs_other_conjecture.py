"""
composite_number = p + 2*(k**2), where p is prime, k is any +ve integer
or composite = a + b, where a belongs to primes, and b belongs to set of 2*(k**2), double_squares
Hence maintain two sets, one of primes, other of double_squares
"""

"""primes are ascending order, doubles_sqaures in descending"""
primes = [2]
double_squares = [2, 8]

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
    idx_p, idx_ds = 0, 0
    len_p, len_ds = len(primes) - 1, len(double_squares) - 1
    while idx_p <= len_p or idx_ds <= len_ds:
        if primes[idx_p] + double_squares[idx_ds] > n and idx_ds < len_ds:
            idx_ds += 1
        elif primes[idx_p] + double_squares[idx_ds] < n and idx_p < len_p:
            idx_p += 1
        else:
            return True
    return False

def is_odd(n):
    return n%2 == 0

def main():
    n = 3
    while True:
        double_squares.insert(0, 2*(n**2))
        if is_prime(n):
            primes.append(n)
            print n
        elif is_odd(n) and not holds_goldbach_conjecture(n):
            print n
            break
        n += 1

if __name__ == "__main__":
    main()
