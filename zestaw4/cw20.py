# Zadanie 20. Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
# przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
# wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi

from random import randint

def suma_kolumny(t,k):
    N = len(t)
    s = 0
    for i in range(N):
        s += t[i][k]
    return s

def suma_wiersza(t,w):
    N = len(t)
    s = 0
    for i in range(N):
        s += t[w][i]
    return s

def najwieksze_szachowane_pole(t):
    N = len(t)
    max_value = 0
    max_i, max_j = -1, -1
    max_i2, max_j2 = -1, -1
    for i in range(N):
        for j in range(N): #[i][j] to pozycja 1 wiezy
            for i2 in range(i,N):
                for j2 in range(j+1,N): #[i2][j2] to pozycja 2 wiezy
                    value = suma_kolumny(t,j) + suma_wiersza(t,i) + suma_kolumny(t,j2) + suma_wiersza(t,i2)
                    if i2 == i: #jezeli stoja w obrebie tego samego wiersza
                        value = value - suma_wiersza(t,i2)
                        value = value - 2*(t[i][j] + t[i2][j2])
                    elif j2 == j: #jezeli stoja w obrebie tej samej kolumny
                        value = value - suma_kolumny(t,j2)
                        value = value - 2*(t[i][j] + t[i2][j2])
                    else:
                        value = value - t[i][j2] - t[i2][j] - 2*(t[i][j] + t[i2][j2])
                    if value > max_value:
                        max_value = value
                        max_i, max_j = i, j
                        max_i2, max_j2 = i2, j2
    return max_i,max_j,max_i2,max_j2,max_value

if __name__ == "__main__":
    #t = [[4,7], [7,5]]
    N = 26
    t = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            t[i][j] = randint(1,9)
            print(t[i][j],end="\t")
        print()
    print(najwieksze_szachowane_pole([[4,0,2],[3,0,0],[6,5,3]]))
