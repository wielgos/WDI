# Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy
# elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.

def suma_wiersza(t,w,N):
    s = 0
    for i in range(N):
        s += t[w][i]
    return s

def suma_kolumny(t,k,N):
    s = 0
    for i in range(N):
        s += t[i][k]
    return s


if __name__ == "__main__":

    N = 3
    t = [[9,1,4], [7,6,8], [6,10,12]]
    # N = 5
    # t = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # t[i][j] = randint(1,1000)
            print(t[i][j], end="\t")
        print()

    max = -1
    for i in range(N):
        for j in range(N):
            value = suma_kolumny(t,j,N)/suma_wiersza(t,i,N)
            if value>max:
                max = value
                kolumna = j
                wiersz = i
    print(f"[{wiersz}][{kolumna}]")