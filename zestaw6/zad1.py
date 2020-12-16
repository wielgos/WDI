# Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje
# liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez
# wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry.

def prime(n):
    if n == 2 or n == 3 or n == 5: return True
    i = 2
    while i*i <= n:
        if n%i==0:
            return False
        i+= 1
    return True

s = set()

def funkcja(n):
    nstr = str(n)
    dl = len(nstr)
    for i in range(0, dl):
        new = (nstr[:i] + nstr[i + 1:])
        if len(new)>=2:
            if new[0]!="0" and int(new) not in s and prime(int(new)):
                s.add(int(new))
            funkcja(new)


n = 171103
funkcja(n)
print(s)