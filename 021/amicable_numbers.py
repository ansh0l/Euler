def find_divisors(number):
    divisors = []
    for divisor_candidate in range(1, (number/2) + 1):
        if number % divisor_candidate == 0:
            divisors.append(divisor_candidate)
    return divisors

def find_sum_of_divisors(number):
    return sum(find_divisors(number))

def main():
    divisor_sums = {}
    amicable_number_sum = 0
    for number in range(2, 10001):
        if not divisor_sums.has_key(number):
            divisor_sums[number] = find_sum_of_divisors(number)
        if divisor_sums[number] != number:
            if not divisor_sums.has_key(divisor_sums[number]):
                divisor_sums[divisor_sums[number]] = find_sum_of_divisors(divisor_sums[number])
            if divisor_sums[divisor_sums[number]] == number and number < divisor_sums[number]:
                amicable_number_sum += (divisor_sums[number] + number)
    print amicable_number_sum

if __name__ == "__main__":
    main()
