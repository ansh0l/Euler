def reverse(num):
    return int(str(num)[::-1])

def is_palindrome(num):
    string_n = str(num)
    length = len(string_n)
    half_length = length/2
    return string_n[:half_length] ==\
        string_n[length - half_length:][::-1]
