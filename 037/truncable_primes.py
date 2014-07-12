primes = [2, 3, 5, 7]

def is_ltr_truncable_prime(n):
    ltr_truncable_prime = True
    string_n = str(n)
    while string_n != '':
        n = int(string_n) #if at end, will throw ValueError on ''
        if n not in primes:
            ltr_truncable_prime = False
            break
        string_n = string_n[:-1]
    return ltr_truncable_prime


def is_rtl_truncable_prime(n):
    rtl_truncable_prime = True
    string_n = str(n)
    while string_n != '':
        n = int(string_n) #if at end, will throw ValueError on ''
        if n not in primes:
            rtl_truncable_prime = False
            break
        string_n = string_n[1:]
    return rtl_truncable_prime

def get_next_prime():
    candidate = primes[-1] + 2
    while candidate not in primes:
        cab_be_prime = True
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
        if is_ltr_truncable_prime(p) and is_rtl_truncable_prime(p):
            print p
            sigma += p
            idx += 1
    print sigma

if __name__ == "__main__":
    main()
