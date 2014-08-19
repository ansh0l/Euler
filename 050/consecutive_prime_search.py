with open("primes.million.txt", "r") as f:
    all_primes = [int(p) for p in f.read().split()]

max_streak = {"length": 21,
              "prime": 953, 
              "numbers": None}

MILLION = 10**6

def get_highest_possible_prime_for_sequence():
    max_median = all_primes[-1]/max_streak["length"]
    if max_median % 2 == 0:
        max_median += 1
    while max_median not in all_primes:
        max_median += 2
    location = all_primes.index(max_median)
    return location + max_streak["length"]

def find_longest_sequence(primes_for_sequence):
    length = len(primes_for_sequence)
    i, j, sigma = 0, 0, 0
    while i + max_streak["length"] <= length:
        sigma = primes_for_sequence[i]
        j = i + 1
        while sigma < MILLION:
            sigma += primes_for_sequence[j]
            j += 1
            if j > length - 1:
                break
            elif sigma in all_primes and j - i > max_streak["length"]:
                max_streak["length"] = j - i
                max_streak["prime"] = sigma 
                max_streak["numbers"] = primes_for_sequence[i:j]
                print max_streak, "\n"
        sigma -= primes_for_sequence[i]
        i += 1

    
def main():
    loc = get_highest_possible_prime_for_sequence()
    primes_for_sequence = all_primes[:loc]
    primes_for_sequence.reverse()
    find_longest_sequence(primes_for_sequence)
    print max_streak

if __name__ == "__main__":
    main()

