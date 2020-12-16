# Zadanie 13. Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest tablica
# T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje elementy nie posiadające
# liczby komplementarnej.

def is_prime(n):
    if n==1: return False
    if n==2: return True
    if n==3: return True
    i=2
    while i * i <= n:
        if n%i ==0:
            return False
        i += 1
    return True

def funkcja(t):
    N = len(t)
    temp_t = [[-1]*N for _ in range(N)]
    for i in range(N*N):
        for j in range(i+1,N*N):
                if is_prime(t[i//N][i%N]+t[j//N][j%N]):
                    temp_t[i//N][i%N] = 0
                    temp_t[j//N][j%N] = 0
    for i in range(N):
        for j in range(N):
            if temp_t[i][j]==0:
                t[i][j]=0

if __name__ == "__main__":
    t = [[24, 6, 6],
         [2, 6, 6],
         [6, 6, 4]]
    print(t)
    funkcja(t)
    print(t)