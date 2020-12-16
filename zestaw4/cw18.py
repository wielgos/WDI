from random import randint

def funkcja(t):
    N = len(t)
    smax = t[0][0]
    for i in range(N):
        for j in range(N):
            count = 0
            s1 = 0
            s2 = 0
            while count<10 and count + j < N:
                s1 += t[i][j+count]
                count += 1
                smax = max(smax,s1)
            count = 0
            while count < 10 and count + i < N:
                s2 += t[i+count][j]
                count += 1
                smax = max(smax, s2)
    return smax

def znajdz(t):
    res = t[0][0]   #[0] for rows, [1] for cols

    for i in range(len(t)):
        for j in range(len(t)):
            temp_row = t[i][j]
            count = 1
            while count < 10 and count + j < len(t):
                temp_row += t[i][j + count]
                count += 1
                if temp_row > res:
                    res = temp_row
    return res

if __name__ == "__main__":
    N = 3
    t = [[0]*N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            t[i][j] = randint(-9,9)
            print(t[i][j],end="\t")
        print()
    print(funkcja(t))