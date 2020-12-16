# Zadanie 12. Dana jest tablica T[N][N][N]. Proszę napisać funkcję, do której przekazujemy tablicę wypełnioną liczbami większymi od zera. Funkcja powinna zwracać wartość True, jeżeli na wszystkich poziomach
# tablicy liczba elementów sąsiadujących (w obrębia poziomu) z co najmniej 6 liczbami złożonymi jest jednakowa albo wartość False w przeciwnym przypadku.

from random import randint

def czy_zlozona(n):
    if n == 1: return False
    i = 2

    while i * i <= n:
        if n % i == 0:
            return True
        i += 1
    return False


def funkcja(t):
    N = len(t)

    ele_s = [0]*N
    for p in range(N):
        elements = 0
        for i in range(1,N-1):
            for j in range(1,N-1):
                counter = 0
                if czy_zlozona(t[p][i-1][j])==True:
                    counter += 1
                if czy_zlozona(t[p][i-1][j-1])==True:
                    counter+=1
                if czy_zlozona(t[p][i-1][j+1])==True:
                    counter+=1
                if czy_zlozona(t[p][i][j+1])==True:
                    counter+=1
                if czy_zlozona(t[p][i+1][j+1])==True:
                    counter+=1
                if czy_zlozona(t[p][i+1][j])==True:
                    counter+=1
                if czy_zlozona(t[p][i+1][j-1])==True:
                    counter+=1
                if czy_zlozona(t[p][i][j-1])==True:
                    counter+=1
                if counter>=6:
                    elements += 1
        ele_s[p] = elements
    print(ele_s)
    for p in range(1,N):
        if ele_s[p]!=ele_s[0]:
            return False
    return True

if __name__ == "__main__":
    N = 4
    t = [
            [
                [4, 2, 6, 8],
                [4, 2, 6, 8],
                [4, 2, 6, 8],
                [4, 2, 6, 8]
            ],
            [
                [4, 2, 6, 9],
                [4, 2, 6, 9],
                [4, 2, 6, 9],
                [4, 2, 6, 9]
            ],
            [
                [4, 2, 6, 9],
                [4, 2, 6, 9],
                [4, 2, 6, 9],
                [4, 2, 6, 9]
            ],
            [
                [4, 2, 6, 9],
                [4, 2, 6, 9],
                [4, 2, 6, 9],
                [4, 2, 6, 9]
            ]
        ]
    for p in range(N):
        print(f"p{p}:")
        for i in range(N):
            for j in range(N):
                t[p][i][j] = randint(1,9)
                print(t[p][i][j],end="\t")
            print()

    print(funkcja(t))
