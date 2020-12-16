# Zadanie 9. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
# długość najdłuższego, spójnego podciągu rosnącego.
from random import randint
if __name__ == "__main__":
    N = 10
    t = [randint(1,1000) for _ in range(N)]
    print(t)
    podciagi = []
    x = [] # x to dany pojedynczy spojny podciag
    x.append(t[0])
    for i in range(0, len(t) - 1):
        if t[i] < t[i + 1]:
            x.append(t[i+1])
        else:
            podciagi.append(x.copy())
            x.clear()
            x.append(t[i+1])
    podciagi.append(x.copy())
    maxlen = 0
    for el in podciagi:
        if len(el) > maxlen:
            maxlen = len(el)
    print(maxlen)