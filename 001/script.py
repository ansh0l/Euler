sigma = 0
for num in range(2, 1000):
    if num % 5==0 or num % 3==0:
        sigma += num
        print num, sigma
print sigma
