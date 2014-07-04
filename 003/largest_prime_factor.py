import math

number = 600851475143

prime_numbers = [2]
candidate = 3
biggest_factor = 1
sqrt = int(math.floor(math.sqrt(number) + 1))
while candidate <= sqrt and candidate <= number: 
    undivided = True
    for divider in prime_numbers:
        if candidate % divider == 0:
            undivided = False
            break
    if undivided:
        prime_numbers.append(candidate)
        if number % candidate == 0 :
            print number, candidate, sqrt
            number = number/candidate
            biggest_factor = candidate
    candidate += 2

print biggest_factor
