def is_pandigital(a, b): #1 through 9 pandigital; a*b=c
    string = str(a)+str(b)+str(a*b)
    return len(string) == 9 and set(string) == set("123456789")

def main():
    pandigital = []
    for a in range(10000):
        for b in range(10000):
            string = str(a)+str(b)+str(a*b)
            if len(string) > 9:
                break
            elif set(string) == set("123456789") and a*b not in pandigital:
                pandigital.append(a*b)
    print sum(pandigital)


if __name__ == "__main__":
    main()
