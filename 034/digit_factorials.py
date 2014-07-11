fact = {0:1, 1:1}

def factorial(n):
    if n < 2:
        return 1
    elif fact.get(n, '') != '':
        return fact[n]
    else:
        fact[n] = n * factorial(n - 1)
        return fact[n]

def is_digit_factorial(n):
    digit_factorial_sum = 0
    for digit in str(n):
        digit_factorial_sum += fact[int(digit)]
    return digit_factorial_sum == n


def main():
    factorial(9)
    sigma = 0
    for num in range(3, fact[9] * 7):
        if is_digit_factorial(num):
            sigma += num
    print sigma
    

if __name__ == "__main__":
    main()
