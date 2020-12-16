# Zadanie 6. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
# tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
# powinny zawierać zera.

def przesun_elementy_prawo(od_ktorego,t,N):
    for i in range(N-1,od_ktorego,-1):
        t[i] = t[i-1]
        t[i-1] = 0
    return None

if __name__ == "__main__":
    N = 3
    T1 = [[0]*N for _ in range(N)]
    T1 = [[1,5,7], [7,12,16], [32,1,24]]

    T2 = [0]*(N*N)
    start = 1
    T2[0] = T1[0][0]
    for wiersz in range(N):
        for kolumna in range(N):
            if T1[wiersz][kolumna] in T2:
                continue
            if T1[wiersz][kolumna] > T2[start-1]:
                T2[start] = T1[wiersz][kolumna]
            else:
                j = start - 1
                while T2[j] > T1[wiersz][kolumna]:
                    j -= 1
                przesun_elementy_prawo(j+1,T2,N*N)
                T2[j+1] = T1[wiersz][kolumna]
            start += 1
    for e in T1:
        print(e)
    print()
    print(T2)