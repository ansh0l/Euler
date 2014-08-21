MAX_ITERATIONS = 50

def reverse(num):
    return int(str(num)[::-1])

def is_palindrome(num):
    string_n = str(num)
    length = len(string_n)
    half_length = length/2
    return string_n[:half_length] ==\
        string_n[length - half_length:][::-1]

def is_lychrel_number(num):
    new_num = num
    for i in range(MAX_ITERATIONS):
        new_num += reverse(new_num)
        if is_palindrome(new_num):
            return False 
    return True
        
sigma = 0
for num in range(0, 10000):
    if is_lychrel_number(num):
        sigma += 1
print sigma
