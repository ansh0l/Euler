def main():
    pandigital = []
    for a in range(10000): #10000, since 9876*5=49380 => total digits exceed 9
        for b in range(10000):
            string = str(a)+str(b)+str(a*b)
            if len(string) > 9:
                break
            elif set(string) == set("123456789") and a*b not in pandigital:
                pandigital.append(a*b)
    print sum(pandigital)

if __name__ == "__main__":
    main()
