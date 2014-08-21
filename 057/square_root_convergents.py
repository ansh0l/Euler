"""
expression = "(f(1) + (f(1)/f(2)))"
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
   7 /   5    |     7 = 2*2+3; 5 = 2+3 
  17 /  12    |     17 = 2*5+7; 12 = 5+7
  41 /  29    |     41 = 12*2+17; 29 = 12+17
  99 /  70    |     99 = 29*2+41; 70 = 29+41
 239 / 169    |     239 = 70*2+99; 169 = 70+99
 577 / 408    |     577 = 169*2+239; 408 = 169+239
1393 / 985    |     1393 = 408*2+577; 985 = 577+408
"""

numerator=3
denominator=2
count = 0
for iterator in range(1000):
    if len(str(numerator)) > len(str(denominator)):
       count += 1
    numerator += denominator*2
    denominator = numerator - denominator
print count
