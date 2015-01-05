import sys
import math

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

def get_numbers():
    tria = {str(triangle(n)) for n in range(150) if is_valid(triangle(n))}
    squa = {str(square(n)) for n in range(150) if is_valid(square(n))}
    pent = {str(pentagonal(n)) for n in range(150) if is_valid(pentagonal(n))}
    hexa = {str(hexagonal(n)) for n in range(150) if is_valid(hexagonal(n))}
    hept = {str(heptagonal(n)) for n in range(150) if is_valid(heptagonal(n))}
    octa = {str(octagonal(n)) for n in range(150) if is_valid(octagonal(n))}
    return tria, squa, pent, hexa, hept, octa

def main():
    number_sets = get_numbers()
    l = len(number_sets)
    for number in number_sets[0]:

if __name__ == "__main__":
    main()
