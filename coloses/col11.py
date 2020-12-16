# Zad. 3. Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę
# napisać funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego króla szachowego tak aby żadne dwa króle
# nie stały w odległości mniejszej niż dwa ruchy króla. Dodatkowo, suma wartości pól zajmowanych przez wszystkie
# figury była równa zero.

def f(t):
    def rek(t,w,k,s=0,forbid=[],time=1):
        #print(w, k,forbid)
        if s==0 and w==len(t)-1 and t[w][k]==0:
            return True
        else:
            for i in range(3,8):
                if w+1<=len(t)-1 and 0<=k+i<=len(t)-1:
                    if time%2==1 and k+i not in forbid:
                        if rek(t,w+1,k+i,s+t[w][k],[k-2,k-1,k,k+1,k+2]):
                            return True
                if w+1<=len(t)-1 and 0<=k-i<=len(t)-1:
                    if time % 2 == 1 and k + i not in forbid:
                        if rek(t,w+1,k-i,s+t[w][k],[k-2,k-1,k,k+1,k+2]):
                            return True
            return False

    for i in range(8):
        if rek(t,0,i):
            return True
    return False


t = [[0,2,3,4,5,6,7,8],
     [1,2,3,0,5,6,4,8],
     [1,2,3,4,5,6,0,8],
     [0,2,3,4,5,6,7,8],
     [1,2,0,4,5,6,7,8],
     [1,2,3,4,5,6,7,0],
     [0,2,3,4,5,6,7,8],
     [4,2,3,4,0,6,7,8]]

print(f(t))