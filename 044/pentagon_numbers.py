import math

def get_pentagonal_number(n):
    return n * (3*n - 1) / 2

def is_pentagonal_number(x):
    n = int((math.sqrt(24*x + 1) + 1)/6)
    return x > 0 and n*(3*n - 1)/2 == x

def main():
    MAX = 5000
    diff = {}
    for i in range(1, MAX):
        for j in range(i, MAX + 1):
            pnj, pni = get_pentagonal_number(j), get_pentagonal_number(i)
            if is_pentagonal_number(pnj + pni) and is_pentagonal_number(pnj - pni):
                diff[j-i] = [j, i, pnj, pni, pnj - pni]
    print diff
    print diff[min(diff.keys())]

    
if __name__ == "__main__":
    main()
