primes = [2, 3, 5, 7]

def is_ltr_truncatable_prime(n):
    ltr_truncatable_prime = True
    string_n = str(n)
    while string_n != '':
        n = int(string_n) #if at end, will throw ValueError on ''
        if n not in primes:
            ltr_truncatable_prime = False
            break
        string_n = string_n[:-1]
    return ltr_truncatable_prime


def is_rtl_truncatable_prime(n):
    rtl_truncatable_prime = True
    string_n = str(n)
    while string_n != '':
        n = int(string_n) #if at end, will throw ValueError on ''
        if n not in primes:
            rtl_truncatable_prime = False
            break
        string_n = string_n[1:]
    return rtl_truncatable_prime

def get_next_prime():
    candidate = primes[-1] + 2
    while True:
        can_be_prime = True
        for p in primes:
            if p**2 > candidate:
                break
            elif candidate % p == 0:
                can_be_prime = False
                break
        if can_be_prime:
            primes.append(candidate)
            return candidate
        candidate += 2

def main():
    idx, sigma = 0, 0
    while idx != 11:
        p = get_next_prime()
        if set('02468').intersection(str(p)[1:]) == set() and \
                is_ltr_truncatable_prime(p) and is_rtl_truncatable_prime(p):
            print p, idx
            sigma += p
            idx += 1
    print sigma

if __name__ == "__main__":
    main()
