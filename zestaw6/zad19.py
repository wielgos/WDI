# Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
# nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
# polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
# (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
# T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
# w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
# narożnika.

def d(w1,k1,w2,k2):
    return ((w1-w2)**2+(k1-k2)**2)**0.5

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
    def rek(t,w,k,odl,dirw,dirk):
        if (w==7 and k==7) or (w==0 and k==7) or (w==7 and k==0):
            return True
        else:
            for i in range(-1,2):
                for j in range(-1,2):
                    if i==j==0:
                        continue
                    if 0<=w+i<=7 and 0<=k+j<=7 and get_digit(t[w][k],digits(t[w][k]))<get_digit(t[w+i][k+j],1) and odl<=d(w+i,k+j,dirw,dirk):
                        if rek(t,w+i,k+j,d(w+i,k+j,dirw,dirk),dirw,dirk):
                            return True


    if rek(t,0,0,d(0,0,7,7),7,7) or rek(t, 0, 0, d(0, 0, 0, 7), 0, 7) or rek(t, 0, 0, d(0, 0, 7, 0), 7, 0):
        return True
    else:
        return False

t=[[25,34,56,78,89,12,13,14],
   [64,34,56,78,89,12,13,14],
   [53,34,56,78,89,12,13,14],
   [78,34,56,78,89,12,13,14],
   [96,34,56,78,89,12,13,14],
   [75,34,56,78,89,12,13,14],
   [64,34,56,78,89,12,13,14],
   [58,34,56,78,89,12,13,14]]

print(king(t))
