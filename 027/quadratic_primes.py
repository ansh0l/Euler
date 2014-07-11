limit = 1000
primes = [2]

def get_primes_less_than_1000():
    candidate = 3
    while candidate < limit:
        can_be_prime = True
        for prime in primes:
            if candidate % prime == 0:
                can_be_prime = False
                break
        if can_be_prime:
            primes.append(candidate)
        candidate += 2

def main():
    get_primes_less_than_1000()

def is_quadratic_prime(a, b, n):
    return True if n**2 + a*n + b in primes else False

def get_range_a():
    range_a = []
    for i in range(limit):
        range_a += [i, i * -1] 
    return range_a

def get_range_b():
    range_b = []
    for p in primes:
        range_b += [p, p * -1] 
    return range_b

def get_main():
    range_a, range_b = get_range_a(), get_range_b()
    longest_streak, largest_ab = 0, 0
    for a in range_a:
        for b in range_b:
            for n in range(limit):
                if not is_quadratic_prime(a, b, n):
                    if n >= longest_streak and a*b > largest_ab:
                        longest_streak = n
                        largest_ab = a*b
    print largest_ab

if __name__ == "__main__":
    main()
