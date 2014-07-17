import math

def get_triangle(n):
    return n*(n + 1)/2

def is_pentagonal(x):
    n = int((math.sqrt(24*x + 1) + 1)/6)
    return x > 0 and n*(3*n - 1)/2 == x

def is_hexagonal(x):
    n = int((math.sqrt(8*x + 1) + 1)/4)
    return x > 0 and n*(2*n - 1) == x

def main():
    n = 286
    while True:
        triangle = get_triangle(n)
        if is_pentagonal(triangle) and is_hexagonal(triangle):
            print n, triangle
            break
        n += 1

if __name__ == "__main__":
    main()
