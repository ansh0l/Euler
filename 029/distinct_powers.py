lower, upper = 2, 100
all_powers = []
for a in range(lower, upper + 1):
    for b in range(lower, upper + 1):
        all_powers.append(a**b)
all_powers = set(all_powers)
print len(all_powers)
