# Zadanie 28. Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję,
# która zwraca informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym
# podzbiorze, łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była
# jednakowa. Na przykład: [2, 3, 5, 7, 15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
# [5, 7, 15] → false, podział nie istnieje.


def jedynki(n):
    pow = 0
    while 2 ** pow < n:
        pow += 1
    counter = 0
    while n != 0:
        if n >= 2 ** pow:
            n -= 2 ** pow
            counter += 1
        pow -= 1
    return counter


def wszystkie_jedynki(T):
    s = 0
    for e in T:
        s += jedynki(e)
    return s


# z1 - liczba jedynek w zbiorze 1
# z2 - liczba jedynek w zbiorze 2
# z3 - liczba jedynek w zbiorze 3
# p1 - lista przechowująca liczby 1 zbioru
# p2 - lista przechowująca liczby 2 zbioru
# p3 - lista przechowująca liczby 3 zbioru

def funkcja(T, p=0, z1=0, z2=0, z3=0, p1=[], p2=[], p3=[]):
    if wszystkie_jedynki(T) % 3 != 0:
        return False
    if z1 == z2 == z3 and z1 + z2 + z3 == wszystkie_jedynki(T):
        print(p1, p2, p3)
        return True
    if p == len(T):
        return False
    return funkcja(T, p + 1, z1 + jedynki(T[p]), z2, z3, p1 + [T[p]], p2, p3) or \
           funkcja(T, p + 1, z1, z2 + jedynki(T[p]), z3, p1, p2 + [T[p]], p3) or \
           funkcja(T, p + 1, z1, z2, z3 + jedynki(T[p]), p1, p2, p3 + [T[p]])


T1 = [2, 3, 5, 7, 15]
T2 = [5, 7, 15]
T3 = [2, 3, 5, 7, 6, 6, 6, 6, 255]
print(funkcja(T3))
