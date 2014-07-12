def is_palindrome(string):
    return string == string[::-1] #reverse a string

def is_double_base_palindrome(n):
    return is_palindrome(str(n)) and is_palindrome(str(bin(n)).split('b')[1])

def main():
    sigma = 0
    for n in range(1000000):
        if is_double_base_palindrome(n):
            sigma += n
    print sigma

if __name__ == "__main__":
    main()
