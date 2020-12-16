# Zadanie 1. Dana jest tablica T[N][N]. Proszę napisać
# funkcję wypełniającą tablicę kolejnymi liczbami
# naturalnymi po spirali.

def spirala(t,N):
    kierunek = "prawo"
    kolejna = 1
    wiersz = 0
    kolumna = 0
    for i in range(N**2):
        if kierunek == "prawo":
            t[wiersz][kolumna] = kolejna
            kolejna += 1
            kolumna += 1
            if kolumna == N - 1 or t[wiersz][kolumna+1] != 0:
                kierunek = "dol"
        elif kierunek == "dol":
            t[wiersz][kolumna] = kolejna
            wiersz += 1
            kolejna += 1
            if wiersz == N - 1 or t[wiersz+1][kolumna] != 0:
                kierunek = "lewo"
        elif kierunek == "lewo":
            t[wiersz][kolumna] = kolejna
            kolejna += 1
            kolumna -= 1
            if t[wiersz][kolumna-1] != 0 or kolumna == 0:
                kierunek = "gora"
        elif kierunek == "gora":
            t[wiersz][kolumna] = kolejna
            wiersz -= 1
            kolejna += 1
            if t[wiersz-1][kolumna] != 0 or wiersz == 0:
                kierunek = "prawo"
    return 0

if __name__ == "__main__":
    N = 9
    t = [[0] * N for i in range(N)]  # 5 elem. tablica

    spirala(t,N)
    for i in range(N):
        for j in range(N):
            print(t[i][j], end="\t")
        print()