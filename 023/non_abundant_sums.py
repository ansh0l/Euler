#from find_abundant_numbers import * 
from constant import *

def get_abundant_numbers():
    with open("abundant_numbers.txt", "r") as f:
        abundant_numbers = [int(val) for val in f.read().split()]
    return abundant_numbers

def get_abundant_sum_numbers(abundant_numbers):
    length = len(abundant_numbers)
    abundant_sum_numbers = {}
    for idx, num1 in enumerate(abundant_numbers):
        for num2 in abundant_numbers[idx:length]:
            if num1 + num2 >= limit:
                break
            abundant_sum_numbers[num1 + num2] = num1 + num2
    return abundant_sum_numbers

def sum_of_numbers_before_limit(l):
    return (l-1)*(l)/2

def main():
    abundant_numbers = get_abundant_numbers()
    abundant_sum_numbers = get_abundant_sum_numbers(abundant_numbers)
    print sum_of_numbers_before_limit(limit) - sum(abundant_sum_numbers.keys())

if __name__ == "__main__":
    main()
