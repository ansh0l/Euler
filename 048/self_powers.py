LAST_10_MODULO = 10**10

def get_last_10_digit_of_power(n):
    last_10_digits = 1
    iterations = n
    if n % 10 == 0:
        return 0
    while iterations > 0:
        last_10_digits = (last_10_digits * n) % LAST_10_MODULO
        iterations -= 1
    return last_10_digits

def main():
    sigma = 0
    for n in range(1, 1001):
        sigma = (sigma + get_last_10_digit_of_power(n)) % LAST_10_MODULO
    print sigma

if __name__ == "__main__":
    main()
