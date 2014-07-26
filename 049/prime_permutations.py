primes = [2]

def get_primes_before_10000():
    candidate = 3
    while candidate < 10000:
        if all(candidate % prime for prime in primes if prime**2 <= candidate):
            primes.append(candidate)
        candidate += 2

def main():
    get_primes_before_10000()
    idx = 0
    for p1 in primes:
        idx += 1
        if len(str(p1)) < 4:
            continue
        for p2 in primes[idx:]:
            p3 = 2 * p2 - p1
            if p3 in primes and set(str(p1)) == set(str(p2)) == set(str(p3)):
                print p1, p2, p3, str(p1) + str(p2) + str(p3)



if __name__ == "__main__":
    main()
