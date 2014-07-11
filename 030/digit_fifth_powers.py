up_limit = 6*(9**5) # 999999 has sum of digits = 354294, greater digit not possible
low_limit = 2 #Since 1 is not counted
power = 5

def is_same_as_sum_of_power_of_digits(n):
    sigma = 0
    original = n
    while n > 0:
        last_digit = n % 10
        sigma += last_digit**power
        n /= 10
    if original == sigma:
        return True
    return False

def main():
    matching_numbers = []
    for n in range(low_limit, up_limit):
        if is_same_as_sum_of_power_of_digits(n):
            matching_numbers.append(n)
    print matching_numbers, sum(matching_numbers)

if __name__ == "__main__":
    main()        
