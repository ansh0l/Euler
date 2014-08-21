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
    
    print eval(expression)

The other way si to identify patterns. Numbers we are given:
   3 /   2    |     numerator(n) = denominator(n-1)*2 + numerator(n-1) ; denominator(n) = denominator(n-1) + numerator(n-1)
   7 /   5    |     7 = 2*2 + 3; 5 = 2 + 3 
  17 /  12    |   
  41 /  29    |   
  99 /  70    |   
 239 / 169    |   
 577 / 408    |
1393 / 985    |



"""
