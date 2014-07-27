class Number():

    def __init__(self, value = None, is_prime = True):
        self.value = value
        self.is_prime = is_prime

    def mark_not_prime(self):
        self.is_prime = False

TARGET = MILLION = 1000000

def run_sieve_of_erastosthenes(candidates):
    idx_num = 0
    while idx_num < TARGET:
        if candidates[idx_num].is_prime:
            idx_iter = idx_num * 2
            while idx_iter < TARGET:
                candidates[idx_iter].mark_not_prime()
                idx_iter += idx_num
        idx_num += 1
    return [c.value for c in candidates if c.is_prime]

def write_to_file(filename, primes):
    with open(filename, "w") as f:
        for p in primes:
            f.write('%d ' % p)


def main():
    candidates = [Number(0, False), Number(1, False)] +\
        [Number(n) for n in range(2, TARGET)]

    primes = run_sieve_of_erastosthenes(candidates)

    write_to_file("primes.million.txt", primes)

if __name__ == "__main__":
    main()
