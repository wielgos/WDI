# Zadanie 8. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
# poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
# co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
# się znaleźć taki ciąg oraz długość tego ciągu.

from random import randint

def najdluzszy_ciag_geo(T, N):
    dl_ciagu = 2
    max_dl = 0
    for i in range(1, N - 1):
        qL = T[i] / T[i - 1]
        qP = T[i + 1] / T[i]
        if qL == qP:
            dl_ciagu += 1
        else:
            dl_ciagu = 2
        if dl_ciagu > max_dl:
            max_dl = dl_ciagu
    return max_dl


def najdluzszy_ciag_geo_calej_tablicy(T, N):
    max_dl = 0

    # przekatna
    ciag = [0] * N
    for i in range(0, N):
        ciag[i] = T[i][i]
    if (najdluzszy_ciag_geo(ciag, N)) > max_dl:
        max_dl = najdluzszy_ciag_geo(ciag, N)
    # symetryczne przekatne

    for i in range(1, N - 2):  # iteruję po kolejnych kolumnach
        ciag1 = [0] * (N - i)
        ciag2 = [0] * (N - i)
        w = 0
        k = i
        for j in range(N - i):
            ciag1[j] = T[w][k]
            ciag2[j] = T[k][w]  # ciag pod przekatna (symetryczny punkt)
            w += 1
            k += 1
        if (najdluzszy_ciag_geo(ciag1, N - i)) > max_dl:
            max_dl = najdluzszy_ciag_geo(ciag1, N - i)
        if (najdluzszy_ciag_geo(ciag2, N - i)) > max_dl:
            max_dl = najdluzszy_ciag_geo(ciag2, N - i)
    if max_dl > 2:
        return max_dl
    else:
        return 0


if __name__ == "__main__":
    #N = 4
    #T = [[2, 3, 1, 6], [5, 4, 9, 2], [6, 25, 3, 24], [3, 2, 125, 16]]

    #N = 6
    # T = [[0] * N for _ in range(N)]
    #T = [[2, 4, 1, 6, 7, 2], [5, 4, 9, 2, 3, 1], [6, 25, 8, 24, 3, 2], [3, 2, 125, 16, 1, 2], [3, 2, 125, 16, 32, 2],
          #[3, 2, 125, 16, 1, 64]] #przekatna ma ciag geo o dlugosci 6

    N = 6
    # T = [[0] * N for _ in range(N)]
    T = [[2, 4, 1, 6, 7, 2], [7, 3, 9, 2, 3, 1], [6, 49, 8, 24, 3, 2], [3, 2, 343, 7, 1, 2], [3, 2, 125, 2401, 32, 2],
         [3, 2, 125, 16, 16807, 64]] #przekatna ma ciag geo o dlugosci 5 (znajdujacy sie pod przekatna)

    # N = 7
    # T = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            #T[i][j] = randint(1,100)
            print(T[i][j], end="\t")
        print()

    dlugosc_ciagu = najdluzszy_ciag_geo_calej_tablicy(T, N)
    if dlugosc_ciagu != 0:
        print("Udalo sie znalezc ciag i ma on dlugosc:", dlugosc_ciagu)
    else:
        print("Nie udalo sie znalezc ciagu")
