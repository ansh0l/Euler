
#dividend / divisor = quotient * divisor + remainder

highest_repetition_qr_dict = {}
for divisor in range(2, 1000):
    qr_dict = {'q':'', 'r':''}
    dividend = 10 if d < 10 else (100 if d < 100 else 1000)
    while dividend % divisor !=0:
        remainder = dividend % divisor
        quotient = dividend / divisor
        qr_dict['q'] += str(quotient)
        qr_dict['r'] += str(remainder)
        dividend = remainder * 10
        if remainder == initial_remainder && quotient == initial_quotient:
            break #cycle is here
