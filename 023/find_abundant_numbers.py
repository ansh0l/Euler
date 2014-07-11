from constant import *

prime_numbers = [2]
for num in range(3, limit):
    is_prime = True
    for prime in prime_numbers:
        if num % prime == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

def get_abundant_numbers():
    abundant_numbers = []
    for num in range(2, limit):
        divisors = []
        if num in prime_numbers:
            continue
        for candidate in range(1, num/2 + 1):
            if num % candidate == 0:
                divisors.append(candidate)
        if sum(divisors) > num:
            abundant_numbers.append(num)
            #print "%5d %6d %3d" %(num, sum(divisors), len(divisors))
    return abundant_numbers

if __name__ == "__main__":
    abundant_numbers = get_abundant_numbers()
    with open("abundant_numbers.txt", "w") as f:
        for an in abundant_numbers:
            f.write("%d " % an)
