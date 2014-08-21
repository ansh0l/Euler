biggest_sum = 0

def digital_sum(a, b):
    return sum([int(d) for d in str(a**b)])

for a in range(1, 101):
    for b in range(1, 101):
        sigma = digital_sum(a, b)
        if sigma > biggest_sum:
            biggest_sum = sigma

print biggest_sum
