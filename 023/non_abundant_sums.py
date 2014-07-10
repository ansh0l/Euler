#limit = 280 + 1
limit = 28123 + 1

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
            print "%5d %6d %3d" %(num, sum(divisors), len(divisors))
    return abundant_numbers

def is_a_sum_of_abundant_numbers(num, abundant_numbers, idx_end): #a+b = k problem
    idx_st = 0
    while idx_st < idx_end:
        if abundant_numbers[idx_st] + abundant_numbers[idx_end] == num:
            return True
        elif abundant_numbers[idx_st] + abundant_numbers[idx_end] < num:
            idx_st += 1
        else:
            idx_end -= 1
    return False
    

def main():
    abundant_numbers = get_abundant_numbers()
    print "found_abundant_numbers", len(abundant_numbers)
    non_abundant_sum_numbers = [] 
    for num in range(1, limit):
        if num in abundant_numbers:
            continue
        is_sum_of_abundant_numbers = False
        for diff in range(1, num):
            if diff in abundant_numbers and num - diff in abundant_numbers:
                is_sum_of_abundant_numbers = True
        if not is_sum_of_abundant_numbers:
            non_abundant_sum_numbers.append(num)
    print sum(non_abundant_sum_numbers)

if __name__ == "__main__":
    main()
