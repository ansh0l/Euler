MAX = 1000000000
primes = [2]
candidate = 3

def is_pandigital(n):
    string_n = str(n)
    len_n = len(string_n)
    if len_n == 9:
        return set(string_n) == set('123456789')
    elif len_n == 8:
        return set(string_n) == set('12345678')
    elif len_n == 7:
        return set(string_n) == set('1234567')
    elif len_n == 6:
        return set(string_n) == set('123456')
    elif len_n == 5:
        return set(string_n) == set('12345')
    elif len_n == 4:
        return set(string_n) == set('1234')
    return False

while candidate < MAX:
    can_be_prime = True
    for p in primes:
        if p**2 > candidate:
            break
        elif candidate % p == 0:
            can_be_prime = False
            break
    if can_be_prime:
        primes.append(candidate)
        print candidate
    candidate += 2

primes.reverse()
print "got primes"

for p in primes:
    if is_pandigital(p):
        print p
        break 
