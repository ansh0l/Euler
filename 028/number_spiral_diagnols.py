"""
(1)
delta = 2, numbers_on_diagonal = 3, 5, 7, 9
delta = 4, numbers_on_diagonal = 13, 17, 21, 25
"""

idx = 1
sigma = 1
MATRIX = 1001
CORNER = 4
delta = 2
number = 1
while idx < MATRIX:
    for c in range(CORNER):
        number += delta
        sigma += number
    delta += 2
    idx +=2 #since 2 edges added in each spiral
print sigma
