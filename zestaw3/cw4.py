from math import factorial

if __name__ == "__main__":
    n=3
    jednosc = 0
    t = []
    for i in range(n):
        t.append(0)

    for i in range(0,100):
        w = 1/(factorial(i))
        print(w)