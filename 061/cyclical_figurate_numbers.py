import sys
import math

"""
a*x**2 + b*x + c = 0 has the solution 
x = (-1*b + sqrt(b**2 - 4*a*c))/(2*a)
"""

def is_triangle(N):
    """
    A number is Triangle if N = n*(n+1)/2
    => n**2 + n - 2*N = 0
    => n = (-1 + sqrt(1 + 8*N))/2
    """
    n = int(round((-1 + math.sqrt(1 + 8*N))/2))
    return n**2 == N
    

def is_square(N):
    """
    A number is Square if N == n**2
    """
    return int(round(math.sqrt(N)))**2 == N

def is_pentagonal(N):
    """
    n*(3*n-1)/2
    """
    pass

def is_hexagonal(N):
    """
    n*(2*n-1)
    """
    pass

def is_heptagonal(N):
    """
    n*(5*n-3)/2
    """
    pass

def is_octagonal(N):
    """
    n*(3*n-2)
    """
    pass

def main():
    pass

if __name__ == "__main__":
    main()
