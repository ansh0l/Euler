import math

prime_numbers = [2]
candidate = 3

while len(prime_numbers) < 10001:
    candidature_holds = True
    for prime in prime_numbers:
        if candidate % prime == 0:
            candidature_holds = False
            break
        elif prime > int(math.floor(math.sqrt(candidate) + 1)):
            break
    if candidature_holds:
        prime_numbers.append(candidate)
        print len(prime_numbers), candidate
    candidate += 2
