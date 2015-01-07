import math
import sys

from collections import defaultdict

"""
a*x**2 + b*x + c = 0 has the solution 
x = (-1*b + sqrt(b**2 - 4*a*c))/(2*a)
"""

triangle = lambda n: n*(n+1)/2

def is_triangle(N):
    """
    A number is Triangle if N == n*(n+1)/2
    => n**2 + n - 2*N = 0
    => n = (-1 + sqrt(1 + 8*N))/2
    """
    n = int(round((-1 + math.sqrt(1 + 8*N))/2))
    return N == triangle(n)

square = lambda n: n**2

def is_square(N):
    """
    A number is Square if N == n**2
    """
    n = int(round(math.sqrt(N)))
    return N == square(n)

pentagonal = lambda n: n*(3*n-1)/2

def is_pentagonal(N):
    """
    A number is pentagonal if N == n*(3*n-1)/2
    => 3*n**2 - n -2*N == 0
    => n = (1 + sqrt(1 + 24*N))/6
    """
    n = int(round((1 + math.sqrt(1 + 24*N))/6))
    return N == pentagonal(n)

hexagonal = lambda n: n*(2*n-1)

def is_hexagonal(N):
    """
    A number is hexagonal if N == n*(2*n-1)
    => 2*n**2 - n - N == 0
    => n = (1 + sqrt(1 + 8*N))/4
    """
    n = int(round((1 + math.sqrt(1 + 8*N))/4))
    return N == hexagonal(n)

heptagonal = lambda n: n*(5*n-3)/2

def is_heptagonal(N):
    """
    A number is heptagonal if N == n*(5*n-3)/2
    => 5*n**2 - 3*n - 2*N == 0
    => n = (3 + sqrt(9 + 40*N))/10
    """
    n = int(round((3 + sqrt(9 + 40*N))/10))
    return N == heptagonal(n)

octagonal = lambda n: n*(3*n-2)

def is_octagonal(N):
    """
    A number is octagonal if N == n*(3*n-2)
    => 3*n**2 - 2*n - N == 0
    => n = (2 + sqrt(4 + 16*N))/6
    """
    n = int(round((2 + math.sqrt(4 + 16*N))/6))
    return N == octagonal(n)


is_valid = lambda x: 999 < x < 10000 and 9 < x % 100

class DD(defaultdict):
    def __init__(self, f=lambda: [], *args, **kwargs):
        return super(DD, self).__init__(f, *args, **kwargs)
        

def get_numbers():
    tria, squa, pent, hexa, hept, octa = DD(), DD(), DD(), DD(), DD(), DD()

    temp = {str(triangle(n)) for n in range(150) if is_valid(triangle(n))}
    for num in temp:
        tria[num[:2]].append(num[2:])

    temp = {str(square(n)) for n in range(150) if is_valid(square(n))}
    for num in temp:
        squa[num[:2]].append(num[2:])

    temp = {str(pentagonal(n)) for n in range(150) if is_valid(pentagonal(n))}
    for num in temp:
        pent[num[:2]].append(num[2:])

    temp = {str(hexagonal(n)) for n in range(150) if is_valid(hexagonal(n))}
    for num in temp:
        hexa[num[:2]].append(num[2:])

    temp = {str(heptagonal(n)) for n in range(150) if is_valid(heptagonal(n))}
    for num in temp:
        hept[num[:2]].append(num[2:])

    temp = {str(octagonal(n)) for n in range(150) if is_valid(octagonal(n))}
    for num in temp:
        octa[num[:2]].append(num[2:])

    return tria, squa, pent, hexa, hept, octa

def main():
    number_sets = get_numbers()

if __name__ == "__main__":
    main()
