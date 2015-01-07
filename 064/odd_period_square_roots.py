import math

def is_irrational_root(N):
    return not int(round(math.sqrt(N)))**2 == N

def get_concise_representation(n):
    return {"repeat": []}

def main():
    count_odd_period = 0
    for i in range(1, 10000):
        if is_irrational_root(i):
            representation = get_concise_representation(i)
            if len(representation["repeat"]) % 2:
                count_odd_period += 1

if __name__ == "__main__":
    main()
