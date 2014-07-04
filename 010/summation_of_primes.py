import math

NUMBER = 2000000

prime_numbers = [2]
candidate = 3

while candidate < NUMBER:
    candidature_holds = True
    for prime in prime_numbers:
        if candidate % prime == 0:
            candidature_holds = False
            break
        elif prime > math.floor(math.sqrt(candidate) + 1):
            break
    if candidature_holds:
        prime_numbers.append(candidate)
    candidate += 2

print sum(prime_numbers)

