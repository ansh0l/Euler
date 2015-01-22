import math
import sys

from collections import defaultdict

"""
a*x**2 + b*x + c = 0 has the solution
x = (-1*b + sqrt(b**2 - 4*a*c))/(2*a)
"""

triangle = lambda n: n*(n+1)/2
square = lambda n: n**2
pentagonal = lambda n: n*(3*n-1)/2
hexagonal = lambda n: n*(2*n-1)
heptagonal = lambda n: n*(5*n-3)/2
octagonal = lambda n: n*(3*n-2)

is_valid = lambda x: 999 < x < 10000 and 9 < x % 100

class DD(defaultdict):
    def __init__(self, f=lambda: [], *args, **kwargs):
        return super(DD, self).__init__(f, *args, **kwargs)

def get_numbers():
    tria, squa, pent, hexa, hept, octa = DD(), DD(), DD(), DD(), DD(), DD()
    type_of_numbers = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]

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

def find_cycle(sets, start=[], original=""):
    current, remaining = sets[0], sets[1:]
    if not sets:
        return original
    elif start:
        for item in start:
            if item
    for item in current:
        find_cycle(sets[1:], current[item], item)
    return find_cycle(sets[1:], start, original)

def main():
    number_sets = get_numbers()
    cycle = find_cycle(number_sets + number_sets[0])
    if cycle:
        print cycle
        print sum(map(int, [cycle[0:4],cycle[2:6], cycle[4:8], cycle[6:10], cycle[8:12], cycle[10:] + cycle[:2]]))
        print [cycle[0:4],cycle[2:6], cycle[4:8], cycle[6:10], cycle[8:12], cycle[10:] + cycle[:2]]

if __name__ == "__main__":
    main()
