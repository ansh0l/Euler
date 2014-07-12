"""
a + b + c = p
Since right triangles, a**2 + b**2 = c**2
=> a**2 + b**2 = (p - a - b)**2
and c = (p - a - b)
"""

def are_valid_sides(a, b, p):
    return p > a + b and a**2 + b**2 == (p - a - b)**2

for num in range(3, 1001):
    solutions = []
    for a in range(1, num - 2):
        if are_valid_sides(a, num - a, num):
            solutions.append(a, num - a, num - a - b))

