years = 100
months = 12
start_year = 1901
start_month = 1

days_so_far = 2
count_sundays_on_first_of_month = 0

def check_sunday(days_so_far):
    return (days_so_far) % 7 == 0

for year in range(start_year, start_year + years):
    for month in range(start_month, start_month + months):
        if check_sunday(days_so_far):
            count_sundays_on_first_of_month += 1
        #print "%4d %2d %4d %s" %(days_so_far, month, year, str(check_sunday(days_so_far)))
        if month in [1, 3, 5, 7, 8, 10, 12]:
            days_so_far += 31
        elif month in [4, 6, 9, 11]:
            days_so_far += 30
        elif (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0): #leap year feb
            days_so_far += 29
        else: #non leap year feb
            days_so_far += 28

print count_sundays_on_first_of_month
