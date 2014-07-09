def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    return 1

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

required_pos = 1000000
current_pos = 0

lexi_number = 0

while current_pos < required_pos and digits != []:
    digits_left = list(digits)
    for digit in digits_left:
        fact = factorial(len(digits_left) - 1)
        if current_pos + fact < required_pos:
            current_pos += fact 
        else:
            lexi_number = lexi_number * 10 + digit
            digits.remove(digit)
            break

print lexi_number
