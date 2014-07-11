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
