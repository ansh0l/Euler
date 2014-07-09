fibonacci_numbers = {1: 1, 2: 1}
n = 2
while len(str(fibonacci_numbers[n])) < 1000:
    n += 1
    fibonacci_numbers[n] = fibonacci_numbers[n-1] + fibonacci_numbers[n-2]
print n
