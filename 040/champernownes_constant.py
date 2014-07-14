irrational_string = "."
MAX = 1000000

if __name__ == "__main__":
    num = 1
    while len(irrational_string) <= MAX:
        irrational_string += str(num)
        num += 1
    product, num = 1, 1
    while num <= MAX:
        product *= int(irrational_string[num])
        num *= 10
    print product
