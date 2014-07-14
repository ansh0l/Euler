import math

def get_pentagonal_number(n):
    return n * (3*n - 1) / 2

def is_pentagonal_number(x):
    n = int((math.sqrt(24*x + 1) + 1)/6)
    return n*(3*n - 1)/2 == x

def main():
    
if __name__ == "__main__":
    main()
