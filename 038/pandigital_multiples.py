def is_pandigital(string):
    return len(string) == 9 and set(string) == set('123456789')

largest_pandigital = 0
for num in range(1, 10000):
    string, multiplier = '', 1
    while len(string) < 9:
        string += str(multiplier * num)
        multiplier += 1
    if is_pandigital(string) and int(string) > largest_pandigital:
        largest_pandigital = int(string)

print largest_pandigital
