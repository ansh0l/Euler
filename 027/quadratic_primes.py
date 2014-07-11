LIMIT = 1000
primes = [2]

def get_primes_less_than_1000():
    candidate = 3
    while candidate < LIMIT:
        can_be_prime = True
        for prime in primes:
            if candidate % prime == 0:
                can_be_prime = False
                break
        if can_be_prime:
            primes.append(candidate)
        candidate += 2

def is_quadratic_prime(a, b, n):
    return True if n**2 + a*n + b in primes else False

def get_range_a():
    range_a = []
    for i in range(LIMIT):
        range_a += [i, i * -1] 
    return range_a

def get_range_b():
    range_b = []
    for p in primes:
        range_b += [p, p * -1] 
    return range_b

def main():
    get_primes_less_than_1000()
    range_a, range_b = get_range_a(), get_range_b()
    ab = {'a': None, 'b': None, 'ab': 0, 'n': 0}
    for a in range_a:
        for b in range_b:
            for n in range(LIMIT):
                if not is_quadratic_prime(a, b, n):
                    if n >= ab['n']:
                        ab = {'a': a, 'b': b, 'ab': a*b, 'n': n}
                    break
    print ab

if __name__ == "__main__":
    main()
