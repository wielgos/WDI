# Mikołaj Wielgos
# 20.11.2020
# Zadanie 2.
# Ulatwiam sobie zadanie poprzez zamiane na system dziesietny
# Nastepnie iteruje po mozliwych kombinacjach wierszy (liczbach) i zapisuje roznice w1-w2 oraz w2-w1
# Porownuje z dotychczas najwieksza znaleziona
# Jezeli przejde przez wszystkie mozliwosci, z zapisanych indeksow obliczam odległość

def porownaniebin(b1,b2):
    N = len(b1)
    for i in range(N):
        if b1[i]>b2[i]:
            return 1
        elif b1[i]<b2[i]:
            return 2
        continue

def distance(T):
    N = len(T)
    maxw = 0
    minw = 0
    for i in range(N-1):
        if porownaniebin(T[maxw],T[i+1]) == 2:
            maxw = i+1
        if porownaniebin(T[minw],T[i+1]) == 1:
            minw = i+1
    return abs(minw-maxw)

T=[[1,1,1,1],
   [0,1,0,1],
   [1,0,1,1],
   [0,0,0,0]]

print(distance(T))