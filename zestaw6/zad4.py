# Zadanie 4. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego

def skoczek(T, w=0, k = 0, jmp=1):
    T[w][k] = jmp
    if jmp==len(T)**2:
        for e in T:
            for e2 in e:
                print(e2, end="\t")
            print()
        return 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (abs(i * j) == 4) or i * j == 0 or abs(i * j) == 1:
                continue
            if len(T) - 1 >= w + i >= 0 and len(T) - 1 >= k + j >= 0 and T[w + i][k + j] == 0:
                skoczek(T, w + i, k + j, jmp + 1)
    T[w][k] = 0

def funkcja(T):
    for i in range(0,len(T)):
        skoczek(T,i)

N = 5
T2 = [[0] * N for _ in range(N)]
T = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

funkcja(T)
