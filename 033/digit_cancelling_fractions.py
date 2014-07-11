from fractions import Fraction as fraction

def is_digit_cancelling_fraction(num, denom):
    str_num, str_denom = str(num), str(denom)
    frac = None
    try:
        if str_num[0] == str_denom[0] != '0':
            frac = fraction(int(str_num[1]), int(str_denom[1]))
        elif str_num[0] == str_denom[1] != '0':
            frac = fraction(int(str_num[1]), int(str_denom[0]))
        elif str_num[1] == str_denom[0] != '0':
            frac = fraction(int(str_num[0]), int(str_denom[1]))
        elif str_num[1] == str_denom[1] != '0':
            frac = fraction(int(str_num[0]), int(str_denom[0]))
    except ZeroDivisionError:
        pass
    if frac == fraction(num, denom):
        return True
    return False

def main():
    product = 1
    for denominator in range(10+1, 100):
        for numerator in range(10, denominator):
            if is_digit_cancelling_fraction(numerator, denominator):
                product *= fraction(numerator, denominator)
    print product.denominator

if __name__ == "__main__":
    main()
