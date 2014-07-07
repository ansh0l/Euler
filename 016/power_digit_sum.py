power = pow(2, 1000)

sigma = 0
for digit in str(power):
    sigma += int(digit)

print sigma
