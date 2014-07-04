biggest_prime_number = 0 
for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        product = num1 * num2
        if str(product%1000)[::-1] == str(product/1000) and product > biggest_prime_number:
            biggest_prime_number = product
            print biggest_prime_number, num1, num2
print biggest_prime_number
