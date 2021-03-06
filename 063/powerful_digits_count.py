from math import log10 as log

"""
For numbers beyond 9, any nth power will have at least n+1 digits.
    Example 10**1 => 2 digits
            10**2 => 3 digits
            10**3 => 4 digits
So only numbers till 9 need to be counted.

The other thing to note is that 9*99 has 95 digits.
So an arbitary range of 100 power has been taken up.
"""

count = 0
for i in range(1, 10):
    for power in range(100):
        if len(str(i**power)) == power:
            count += 1
print count
