import math

def is_triangle_number(p):
    def satisfies_triangle_property(n):
        return lambda x: x*(x+1)/2 == n
    stp = satisfies_triangle_property(p)
    return stp(int((math.sqrt(1 + 8 * p) - 1)/2))

def get_words(filename):
    with open(filename, "r") as f:
        data = f.read().replace('"', '').split(',')
    return data

def get_value_of_word(word):
    sigma, ord_A = 0, ord('A') - 1
    for ch in word:
        sigma += (ord(ch) - ord_A)
    return sigma

def main():
    count_triangle_number = 0
    words = get_words("words.txt")
    for word in words:
        if is_triangle_number(get_value_of_word(word)):
            count_triangle_number += 1
    print count_triangle_number

if __name__ == "__main__":
    main()
