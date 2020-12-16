# Zadanie 2. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
# z nieparzystych cyfr.

from random import randint

def czy_same_nieparzyste(n):
    while n!=0:
        a = n%10
        if a%2==0:
            return False
        n = n - a
        n = n//10
    return True

def funkcja(t,N):
    counter = 0
    for i in range(N):
        for j in range(N):
            if czy_same_nieparzyste(t[i][j]):
                counter += 1
                break
    if counter == N:
        return True
    else:
        return False

if __name__ == "__main__":

    N = 3
    t = [[1,2,4], [3,6,8], [5,10,12]]
    # N = 5
    # t = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # t[i][j] = randint(1,1000)
            print(t[i][j], end="\t")
        print()

    print(funkcja(t,N))