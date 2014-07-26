primes = [2]

def get_divisors(n):
    return [p for p in primes if p <= n/2 and n % p == 0]

def main():
    candidate = 3
    flag = 0
    while True:
        divisors = get_divisors(candidate)
        if not divisors:
            primes.append(candidate)
        flag = flag + 1 if len(divisors) == 4 else 0
        if flag == 4:
            print range(candidate - 3, candidate + 1)
            break
        candidate += 1

if __name__ == "__main__":
    main()
