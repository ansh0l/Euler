def get_primes_before_10000():
    primes = [2]
    candidate = 3
    while candidate < 10000:
        if all(candidate % prime for prime in primes if prime**2 <= candidate):
            primes.append(candidate)
        candidate += 2
    return primes

def get_primes_hashing_to_same_keywords(primes):
    prime_count = {}
    for prime in primes:
        key = int(''.join(sorted(list(str(prime)))))
        if prime_count.has_key(key):
            prime_count[key].append(prime)
        else:
            prime_count[key] = [prime]
    return prime_count

def main():
    primes = get_primes_before_10000()
    primes_hash = get_primes_hashing_to_same_keywords(primes)
    for primes in primes_hash.values():
        if len(primes) > 2:
            print primes

if __name__ == "__main__":
    main()
