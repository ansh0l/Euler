def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a * b / gcd(a, b)

product = 1

for num in range(1, 20):
    product = lcm(product, num)
    print product

print product
