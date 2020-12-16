# Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
# nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
# polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
# (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
# T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
# w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
# narożnika.

def d(w1,k1):
    return ((w1-7)**2+(k1-7)**2)**0.5

def digits(n):
    counter = 0
    while n != 0:
        n -= n % 10
        n //= 10
        counter += 1
    return counter

def get_digit(n, p):  # potrzeba digits()
    q = digits(n)
    if p == q:
        return n % 10
    n = n - n % (10 ** (q - p))
    a = n % (10 ** (q - p + 1))
    a //= 10 ** (q - p)
    return a

def king(t):
    def rek(t,w,k,odl):
        if w==7 and k==7:
            return True
        else:
            if w+1<=7 and get_digit(t[w][k],digits(t[w][k]))<get_digit(t[w+1][k],1) and d(w+1,k)<=odl:
                if rek(t,w+1,k,d(w+1,k)):
                    return True
            if k+1<=7 and get_digit(t[w][k],digits(t[w][k]))<get_digit(t[w][k+1],1) and d(w,k+1)<=odl:
                if rek(t,w,k+1,d(w,k+1)):
                    return True
            if k + 1 <= 7 and w+1<=7 and get_digit(t[w][k], digits(t[w][k])) < get_digit(t[w+1][k + 1], 1) and d(w+1, k + 1) <= odl:
                if rek(t,w+1,k+1,d(w+1,k+1)):
                    return True
            if k + 1 <= 7 and w-1>=0 and get_digit(t[w][k], digits(t[w][k])) < get_digit(t[w-1][k + 1], 1) and d(w-1, k + 1) <= odl:
                if rek(t,w-1,k+1,d(w+1,k+1)):
                    return True
    res = rek(t,0,0,d(0,0))
    return True if res else False


t=[[21,0,0,0,0,0,0,0],
   [0,21,0,0,0,0,0,0],
   [0,0,21,0,0,0,0,0],
   [0,0,0,21,0,0,0,0],
   [0,0,0,0,21,0,0,0],
   [0,0,0,0,0,21,0,0],
   [0,0,0,0,0,0,21,0],
   [0,0,0,0,0,0,0,21]]
print(king(t))
