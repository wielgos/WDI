# Zadanie 2. Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą układ 2 równań
# o 2 niewiadomych.


def nwd(a,b):
    a = abs(a)
    b = abs(b)
    while a!=b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def dodawanie(l1,m1,l2,m2):
    if m1!=m2:
        m1, l1, m2, l2 = m1*m2,l1*m2,m2*m1,l2*m1
    return l1+l2,m1

def odejmowanie(l1,m1,l2,m2):
    if m1!=m2:
        m1, l1, m2, l2 = m1*m2,l1*m2,m2*m1,l2*m1
    return l1-l2,m1

def mnozenie(l1,m1,l2,m2):
    return l1*l2,m1*m2

def dzielenie(l1,m1,l2,m2):
    return l1*m2,l2*m1

def potegowanie(l1,m1,n):
    if n<0:
        l1,m1 = m1,l1
    lstart = l1
    mstart = m1
    for i in range(n-1):
            l1,m1 = l1*lstart,m1*mstart
    return l1,m1

def skracanie(l1,m1):
    n = nwd(l1,m1)
    return l1//n,m1//n

def wypisywanie(l1,m1):
    if l1<0:
        znak = -1
    else:
        znak = 1

    l1 = abs(l1)

    if l1==m1:
        print(1)
        return

    calk = l1//m1
    if calk>0:
        l1 = l1 - calk*m1
    if l1==0:
        print(znak*calk)
    else:
        print(znak*calk,end=".")
        for i in range(7):
            l1 = l1 * 10
            print(l1//m1,end="")
            l1 = l1%m1

def wczytywanie(n):
    liczby = str(n).split('.')
    if len(liczby) == 1:
        print(liczby[0])
    else:
        l1 = int(liczby[1])
        calk = int(liczby[0])
        if calk<0:
            calk = abs(calk)
            znak = "-"
        else:
            znak = ""
        cyfry_m = len(str(l1))
        dzielnik = 10**(cyfry_m)
        ulamek = skracanie(l1,dzielnik)
        print(znak,int(ulamek[0])+calk*int(ulamek[1]),"/",int(ulamek[1]),sep="")


def uklad_rownan(a1,b1,c1,a2,b2,c2):
    y = (a2*c1-a1*c2,a2*b1-a1*b2)
    mnoznik = mnozenie(b2,1,y[0],y[1])
    odejmnik = odejmowanie(c2,1,mnoznik[0],mnoznik[1])
    podzielnik = dzielenie(odejmnik[0],odejmnik[1],a2,1)
    x = (podzielnik[0],podzielnik[1])
    x = skracanie(x[0],x[1])
    y = skracanie(y[0],y[1])
    return x,y

print(uklad_rownan(1,4,3,1,-1,5))