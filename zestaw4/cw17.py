# Zadanie 17. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego suma otaczających go elementów jest największa

def najw_suma_ot_ele(t):
    N = len(t)


    max_s = 0
    for i in range(N):
        for j in range(N):
            s = 0
            if i==0 and j==0: #jestesmy w 0,0
                s = s + t[i][j+1] + t[i+1][j+1] + t[i+1][j]
            elif i==0 and j==N-1: #jestesmy w 0,N-1
                s = s + t[i+1][j] + t[i+1][j-1] + t[i][j-1]
            elif i==0:
                s = s + t[i][j+1] + t[i+1][j+1] + t[i+1][j] + t[i+1][j-1] + t[i][j-1]
            elif i==N-1 and j==0:
                s = s + t[i-1][j] + t[i-1][j+1] + t[i][j+1]
            elif i==N-1 and j==N-1:
                s = s + t[i][j-1] + t[i-1][j] + t[i-1][j-1]
            elif i==N-1:
                s = s + t[i][j-1] + t[i-1][j] + t[i-1][j-1] + t[i-1][j+1] + t[i][j+1]
            elif j==0:
                s = s + t[i-1][j] + t[i+1][j] + t[i-1][j+1] + t[i+1][j+1] + t[i][j+1]
            elif j==N-1:
                s = s + t[i-1][j] + t[i+1][j] + t[i-1][j-1] + t[i+1][j-1] + t[i][j-1]
            else:
                s = s + t[i-1][j] + t[i+1][j] + t[i-1][j-1] + t[i+1][j-1] + t[i][j-1] + t[i-1][j+1] + t[i+1][j+1] + t[i][j+1]
            if s > max_s:
                max_s = s
                w = i
                k = j
    return w,k,max_s

if __name__ == "__main__":
    t = [[7, 30, 21, 3], [25, 1, 3, 9], [9, 32, 32, 24], [3, 2, 64, 44]]
    for e in t:
        for e2 in e:
            print(e2, end="\t")
        print()
    print(najw_suma_ot_ele(t))

