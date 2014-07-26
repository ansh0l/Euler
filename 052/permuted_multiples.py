for n in range(100000, 200000):
    if set(str(n)) == set(str(2*n)) == set(str(3*n)) == set(str(4*n)) == set(str(5*n)) == set(str(6*n)):
        print n
        break
