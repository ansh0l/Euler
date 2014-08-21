from fractions import Fraction as f

expression = "(f(1) + (f(1)/f(2)))"
"""
One way is to replace f(2) with expression, but at the 1000th times, that's too much nesting

1 + 1/2
1 + 1/
      (2 + 1/2)
f(1) + f(1)/
            (f(2) + f(1)/
                        (f(2) + f(1)/f(2)))

"""
print eval(expression)
