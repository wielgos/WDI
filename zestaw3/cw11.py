# Zadanie 11. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej
# liczbami naturalnym wyznacza długość najdłuższego, spójnego podciągu geometrycznego.

from random import randint

if __name__ == "__main__":
    n = 20
    t = [0]*20
    for i in range(n):
        t[i] = randint(1,10)
        print(t[i],end=" ")
    print("")
    podciagi = []
    x = []
    for i in range(1,n-1):
        if t[i]/t[i-1] == t[i+1]/t[i] and len(x)<3:
            x.append(t[i-1])
            x.append(t[i])
            x.append(t[i+1])
        elif len(x)>=3 and t[i]/t[i-1] == t[i+1]/t[i]:
            x.append(t[i+1])
        elif len(x)>=3:
            podciagi.append(x.copy())
            x.clear()
        else:
            x.clear()
    print(podciagi)
    max_length = 0
    for lista in podciagi:
        if len(lista)>max_length:
            max_length = len(lista)
    print(max_length)
