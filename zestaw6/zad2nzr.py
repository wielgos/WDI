# Zadanie 2. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.

def prime(n):
    if n==2 or n==3 or n==5:
        return True
    i = 2
    while i*i <=n:
        if n%i==0:
            return False
        i+= 1
    return True

def waga(n):
    s = set()
    for i in range(2,n+1):
        if prime(i) and n%i==0:
            s.add(i)
            n //= i
    return len(s)


def funkcja(T):
    N = len(T)
    s = set()
    for i in range(N):
        s.add(waga(T[i]))
    print(s)
    if len(s) == 3: return True
    return False

T = [12,14,16,18,2,4,6,17]
print(funkcja(T))