# Zadanie 3. Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie
# hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )] Proszę napisać funkcję,
# która odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują? Do funkcji należy przekazać
# położenie hetmanów.

def nadpisz_szachowane(t,w1,k1):
    N = len(t)
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            k = 1 #mnoznik
            while w1 + i*k>=0 and k1 + j*k>=0 and w1 + i * k <= N-1 and k1 + j*k <= N -1: #straznik wyjscia z tablicy
                t[w1 + i*k][k1 + j*k] = 1
                k+=1
    return


def funkcja(t,dane):
    for elements in dane:
        if(t[elements[0]][elements[1]] != 1):
            nadpisz_szachowane(t,elements[0],elements[1])
        else:
            return False
    return True



N=8
t = [[0]*N for _ in range(N)]
dane = [(1,4),(5,5),(6,2)]


nadpisz_szachowane(t,5,5)
for e in t:
    for e2 in e:
        print(e2,end="\t")
    print()

# print(funkcja(t,dane))