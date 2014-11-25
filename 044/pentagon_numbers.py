import math

"""
Question:
    Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
    The first ten pentagonal numbers are:
        1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
    It can be seen that
        P4 + P7 = 22 + 70 = 92 = P8
    However, their difference,
        70 − 22 = 48
        is not pentagonal.
    Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
        difference are pentagonal and D = |Pk − Pj| is minimised;
        what is the value of D?

Solution:
    Let this be true for n = x, n = y, with x < y
    Then,
        Px = x*(3*x-1)/2,
        Py = y*(3*y-1)/2
    Hence, there exist k, j such that Pk = Py - Px and Pj = Py + Px
    Let Py - Px be a constant c1, and Py + Px = c2
    Hence, we have two quadratic equations
        k*(3*k-1)/2 = c1
    =>  3*k**2 - k - 2*c1 = 0
    and
        3*j**2 - j - 2*c2 = 0

    Now, a quadratic equation of form a*x**2 + b*x + c = 0 has solution
        (-1*b + math.sqrt(b**2 - 4*a*c))/(2*a)

    Hence,
        k = (-1*-1 + math.sqrt((-1)**2 - 4*3*-2*c1))/(2*3)
    =>  k = 1/6.0 + math.sqrt(1 + 24*c1)/6.0
    =>  k = 1/6.0 + math.sqrt(1 + 12*(3*y**2 - y + 3*x**2 - x))/6.0
    and
        j = 1/6.0 + math.sqrt(1 + 12*(3*y**2 - y - 3*x**2 + x +))/6.0
    and both j, k must be integer


"""

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
