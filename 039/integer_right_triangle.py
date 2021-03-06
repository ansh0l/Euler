"""
a + b + c = p
Since right triangles, a**2 + b**2 = c**2
=> a**2 + b**2 = (p - a - b)**2
and c = (p - a - b)
"""

def are_valid_sides(a, b, p):
    return a**2 + b**2 == (p - a - b)**2

max_solutions = []
for num in range(3, 1001):
    solutions = []
    for b in range(1, num - 2):
        for a in range(1, b):
            if a + 2*b + 1 > num: #hypotenuse is at least 2nd_largest_side+1
                break
            elif are_valid_sides(a, b, num):
                solutions.append([a, b, num - a - b, num])
    if len(solutions) > len(max_solutions):
        max_solutions = solutions

print max_solutions


