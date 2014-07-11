denominations = [1, 2, 5, 10, 20, 50, 100, 200]
denominations = [200, 100, 50, 20, 10, 5, 2, 1]

VALUE = 200
ways = {1:1}

def can_make_value(dct):
    sigma = 0
    for coin, count in dct:
        sigma += coin * count 
    if sigma == VALUE:
        return True
    retun False

def main():


if __name__ == "__main__":
    main()
