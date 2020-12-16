# Zadanie 3. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
# parzystą.


from random import randint


def czy_ma_parzysta(n):
    while n != 0:
        a = n % 10
        if a % 2 == 0:
            return True
        n = n - a
        n = n // 10
    return False


def funkcja(t, N):
    for i in range(N):
        counter = 0
        for j in range(N):
            if czy_ma_parzysta(t[i][j]):
                counter += 1
        if counter != N and i==N-1:
            return False
        elif counter == N:
            return True,i

if __name__ == "__main__":

    # N = 3
    # t = [[9,1,4], [7,6,8], [6,10,12]]
    N = 2
    t = [[9,75], [143,4] ]
    #t = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            #t[i][j] = randint(1, 10)
            print(t[i][j], end="\t")
        print()
    print(funkcja(t, N))