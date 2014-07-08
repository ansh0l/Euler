def f(n):
    if n > 1:
        return f(n-1) * n
    return 1

f_100 = f(100)

sigma_digit = sum([int(digit) for digit in str(f_100)])

print sigma_digit
