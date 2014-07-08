def get_special_word_for_number(n):
    special_word_for_numbers = {
        1  : "one",
        2  : "two",
        3  : "three",
        4  : "four",
        5  : "five",
        6  : "six",
        7  : "seven",
        8  : "eight",
        9  : "nine",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
        30 : "thirty",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety",
        }
    if special_word_for_numbers.has_key(n):
        return special_word_for_numbers[n]
    return ""

def generate_word_for_number(n):
    if n < 20:
        return get_special_word_for_number(n)
    elif n < 100:
        tens_digit = n/10
        tens_digit_in_words = get_special_word_for_number(tens_digit*10)
        ones_digit = n%10
        ones_digit_in_words = get_special_word_for_number(ones_digit)
        if ones_digit_in_words != "":
            return tens_digit_in_words + "-" + ones_digit_in_words
        return tens_digit_in_words
    elif n < 1000:
        hundreds_digit = n/100
        hundreds_digit_in_words = get_special_word_for_number(hundreds_digit)
        remaining_digits = n%100
        remaining_digits_in_words = generate_word_for_number(remaining_digits)
        if remaining_digits_in_words != "":
            return hundreds_digit_in_words + " hundred and " + remaining_digits_in_words
        return hundreds_digit_in_words + " hundred"
    elif n == 1000:
        return "one thousand"

def main():
    numbers_in_words, count_characters = {}, 0
    for n in range(1, 1001):
        number_in_word = generate_word_for_number(n)
        numbers_in_words[n] = number_in_word
        #print "%3d %s" %(n, number_in_word)
        count_characters += len(number_in_word.replace(" ", "").replace("-", ""))
    print count_characters

main()
