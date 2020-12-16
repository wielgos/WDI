# Zadanie 10. Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)


def new_tablica(T,w,k):
    N = len(T)
    new_T = [[0]*(N-1) for _ in range(N-1)]
    wn=0
    for i in range(N):
        if i==w:
            continue
        kn=0
        for j in range(N):
            if k==j:
                continue
            new_T[wn][kn]=T[i][j]
            kn+=1
        wn+=1
    return new_T


def wyznacznik(T):
    if len(T)==1:
        return T[0][0]
    value = 0
    for i in range(0,len(T)):
        value += T[0][i]*(-1)**(0+1+i+1) * wyznacznik(new_tablica(T,0,i))
    return value


T2=[[7,4],
    [4,1]]
T=[[5,6,3,2],
   [4,3,2,5],
   [8,7,6,5],
   [4,3,2,1]]
T3=[[3,2,5],
    [7,6,5],
    [3,2,1]]

print(wyznacznik(T))
