primes = [2]
circular_primes = []
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
    string_n = rotate(str(n), 1)
    num = int(string_n)
    is_cp = True
    if set('02468').intersection(set(string_n)) != set() and n != 2 :
        is_cp = False
    else:
        while num != n:
            if num in circular_primes:
                break
            elif num not in primes:
                is_cp = False
                break
            string_n = rotate(string_n, 1)
            num = int(string_n)
    return is_cp
    
def main():
    get_prime_numbers()

    for p in primes:
        if is_circular_prime(p):
            circular_primes.append(p)
    
    print circular_primes, len(circular_primes)

if __name__ == "__main__":
    main()
