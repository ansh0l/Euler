import math

def is_triangle_number(p):
    def satisfies_triangle_property(n):
        return lambda x: x*(x+1)/2 == n
    stp = satisfies_triangle_property(p)
    return stp((math.sqrt(1 + 8 * p) - 1)/2)

