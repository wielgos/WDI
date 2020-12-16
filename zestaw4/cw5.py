# Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy
# elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.

from random import randint

def suma_wiersza(t, w, N):
    s = 0
    for i in range(N):
        s += t[w][i]
    return s


def suma_kolumny(t, k, N):
    s = 0
    for i in range(N):
        s += t[i][k]
    return s


def funkcja(t, N):
    for i in range(N):  # biorę pierwszą możliwą wartość do porównywania
        if suma_wiersza(t, i, N) == 0:
            if i + 1 == N:
                return "Nie istnieje"
            continue
        else:
            max = suma_kolumny(t, 0, N) / suma_wiersza(t, i, N)
            wiersz = i
            kolumna = 0
            break
    for i in range(N):
        for j in range(N):
            if suma_wiersza(t, i, N) == 0:
                break
            value = suma_kolumny(t, j, N) / suma_wiersza(t, i, N)
            if value > max:
                max = value
                kolumna = j
                wiersz = i
    return wiersz, kolumna, max


if __name__ == "__main__":


    #t = [[9, 1, 4], [20, 6, -8], [30, 10, 12]]
    #t = [[1, 2, -3], [4, 9, 0], [6, 5, -11]] #wszystkie wiersze sumują się do zera
    t = [[8220, 5771, 3473, 1345, 1516, 9994, 5683, 9548, 8351, 7624],

 [9095, 7512, 5961, 4316, 2394, 4699, 2697, 2574, 249, 4360],

 [9558, 4109, 5193, 5869, 5877, 4619, 6369, 1315, 263, 6915],

 [3421, 3312, 7683, 4353, 5102, 5277, 4372, 527, 1624, 756],

 [1085, 5915, 7542, 8367, 1879, 2902, 1492, 7540, 624, 1673],

 [5436, 2075, 8576, 9241, 6699, 6584, 5258, 1552, 7224, 6577],

 [7847, 1577, 6507, 1942, 3810, 7795, 4332, 3476, 4467, 135],

 [5076, 4357, 942, 4276, 9594, 7986, 5976, 2291, 7956, 8357],

 [5772, 9338, 6944, 9765, 9656, 467, 1347, 3191, 5337, 564],

 [5877, 4699, 7603, 2021, 8542, 4532, 7995, 3230, 1025, 328]]
    N = 10
    #t = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            #t[i][j] = randint(-100,100)
            print(t[i][j], end="\t")
        print()

    print(funkcja(t, N))
