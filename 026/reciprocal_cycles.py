#dividend / divisor = quotient * divisor + remainder
#Anytime a remainder repeats, means quotient is going to repeat

highest_repetition_qr_dict = {'q':'0.', 'r':[], 'n': 0}
for divisor in range(2, 1000):
    qr_dict = {'q':'', 'r':[], 'n': divisor}
    dividend = 10 if divisor < 10 else (100 if divisor < 100 else 1000)
    remainder, quotient = None, None
    repetitive = False
    while dividend % divisor !=0:
        remainder = dividend % divisor
        quotient = dividend / divisor
        qr_dict['q'] += str(quotient)
        qr_dict['r'].append(remainder)
        dividend = remainder * 10
        if qr_dict['r'].count(remainder) > 1: #cycle is here
            repetitive = True
            break
    if repetitive and len(qr_dict['q']) > len(highest_repetition_qr_dict['q']):
        highest_repetition_qr_dict = qr_dict

print highest_repetition_qr_dict
