MILLION = 1000000

def get_ncr(n, r):
    if r > n or r < 0:
        raise
    elif 2 * r > n:
        r = n - r
    if r == 0:
        return 1
    numerator, denominator = n, 1
    iterator = 2
    while iterator <= r:
        numerator *= (n + 1 -iterator)
        denominator *= iterator
        iterator += 1
    return numerator/denominator

def find_r_for_n(n):
    r, ncr = 0, 1
    while 2 *r <= n:
        ncr = get_ncr(n, r)
        if ncr > MILLION:
            return r
        r += 1
    return -1
    
def get_combinatoric_selections(n):
    r = find_r_for_n(n)
    return 0 if r == -1 else len(range(r, n + 1 - r))

def main():
    total_selections = 0
    for n in range(1, 100 + 1):
        total_selections += get_combinatoric_selections(n)
    print total_selections


if __name__ == "__main__":
    main()
