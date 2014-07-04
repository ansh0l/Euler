def find_a(b, c):
    return 1000 - (b + c)

def find_c(b):
    """
    a**2 + b**2 = c**2
    => (1000 - b - c)**2 + b**2 = c**2
    => 1000**2 + b**2 + c**2 + 2*-1*b*-1*c + 2*1000*-1*b + 2*1000*-1*c = c**2
    => 1000000 + 2*b**2 + 2*b*c - 2000*b - 2000*c = 0
    => c = (2*(b**2) - 2000*b + 1000000)/(2000 - 2b)
    """
    return (2*(b**2) - 2000*b + 1000000)/(2000 - 2*b) 

def validate(a, b, c):
    assert a**2 + b**2 == c**2

a, b, c = 1, 1, 1
while b < 1000 and a > 0 and c > 0: 
    c = find_c(b)
    a = find_a(b, c)
    try:
        validate(a, b, c)
        print a, b, c, a*b*c
    except AssertionError:
        pass
    b += 1
