# Zadanie 11. Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
# są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
# naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z
# przyjaciółkami

def czy_przyjaciolki(a, b):
    if a == -1 or b == -1:
        return False
    cyfry_a = set()
    cyfry_b = set()
    for letter in str(a):
        cyfry_a.add(int(letter))
    for letter in str(b):
        cyfry_b.add(int(letter))
    if cyfry_a == cyfry_b:
        return True
    else:
        return False


def funkcja(t):

    N = len(t)
    pomt = [[-1] * (N+2) for _ in range(N+2)]
    final_c = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            pomt[i][j] = t[i-1][j-1]
    print(pomt)
    for i in range(1,N+1):
        for j in range(1,N+1):
            counter = 0
            sr = pomt[i][j]
            srg = pomt[i-1][j]
            srp = pomt[i][j+1]
            srd = pomt[i+1][j]
            srl = pomt[i][j-1]
            if czy_przyjaciolki(sr,srg):
                counter += 1
            if czy_przyjaciolki(sr,srp):
                counter+= 1
            if czy_przyjaciolki(sr,srd):
                counter+= 1
            if czy_przyjaciolki(sr,srl):
                counter+= 1
            if ((i==1 and j==1) or (i==N+1 and j==N) or (i==1 and j==N) or (i==N and j==1) ) and counter == 2:
                final_c += 1
            elif (i==1 or i==N or j==N or j==1) and counter == 3:
                final_c += 1
            elif counter == 4:
                final_c += 1
    return final_c


if __name__ == "__main__":
    t = [[24, 4, 4],
         [3, 4, 4],
         [3, 3, 4]]
    print(funkcja(t))