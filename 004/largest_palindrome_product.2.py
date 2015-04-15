from math import sqrt

def largest_palindrome_product():
    palindrome = lambda num: int(num+num[::-1])
    for num in xrange(999, 99, -1):
        possible_solution = palindrome(str(num))
        for div1 in xrange(999, int(sqrt(possible_solution)), -1):
            div2 = possible_solution / div1
            if div2 < 1000 and div1 * div2 == possible_solution:
                return possible_solution

if __name__ == "__main__":
    print largest_palindrome_product()
