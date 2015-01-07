import sys

from collections import defaultdict

def main():
    d = defaultdict(lambda: [])
    for i in range(10000):
        cube = i**3
        key = tuple(sorted(str(i**3)))
        d[key].append(cube)
        if len(d[key]) > 4:
            print d[key]
            break

if __name__ == "__main__":
    main()
