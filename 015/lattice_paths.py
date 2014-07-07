"""
A * * * * * * * * * * * * * * * * * * D
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
C * * * * * * * * * * * * * * * * * * B

Going from A to B is same as going from C to D. Hence, we take number of steps at each point around C
Let C be (0,0). Then D becomes (19, 19), B becomes (19, 0), A becomes (0, 19)
"""

SIDE = 21

step_matrix = [[-1 for x in range(SIDE)] for y in range(SIDE)]

def print_step_matrix(step_matrix):
    for row in step_matrix:
        string = ""
        for element in row:
            string += "%3d, " % element
        print string

for n in range(SIDE):
    step_matrix[0][n] = 1
for n in range(SIDE):
    step_matrix[n][0] = 1

"""
All points across CB and CA can be reached in only one way.
Also, C can be reached in 1 way only

Further, ways(x, y) = ways(x-1, y) + ways(x, y-1), where 19 >= x > 0, 19 >= y > 0
Here, 19 => SIDE - 1
"""

for x in range(1, SIDE):
    for y in range(1, SIDE):
        step_matrix[x][y] = step_matrix[x - 1][y] + step_matrix[x][y - 1]

print step_matrix[-1][-1]
