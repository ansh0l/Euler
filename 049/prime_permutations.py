primes = [2]

def get_primes_before_10000():
    candidate = 3
    while candidate < 10000:
        if all(candidate % prime for prime in primes if prime**2 <= candidate):
            primes.append(candidate)
        candidate += 2

def satisfy_permutation(n):
    str_n = str(n)
    rotate_by_1 = int(str_n[1:] + str_n[:1])
    rotate_by_2 = int(str_n[2:] + str_n[:2])
    return len(str_n) == 4 and len(str(rotate_by_1)) == 4 and len(str(rotate_by_2)) == 4\
        and rotate_by_1 in primes and rotate_by_2 in primes
    

def main():
    get_primes_before_10000()
    for prime in primes:
        if satisfy_permutation(prime):
            print prime
            break

if __name__ == "__main__":
    main()
