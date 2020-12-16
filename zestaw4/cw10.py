# Zadanie 10. Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartość
# True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość
# False w przeciwnym przypadku.

def funkcja(t):
    N = len(t)
    for i in range(N):
        ck = 0
        cr = 0
        for j in range(N):
            if t[i][j] == 0:
                cr += 1
            if t[j][i] == 0:
                ck += 1
        if cr ==0 or ck ==0:
            return False
    return True


if __name__ == "__main__":
    t = [[0, 0, 3,],
         [0, 1, 3,],
         [0, 2, 0,]]
    print(funkcja(t))
