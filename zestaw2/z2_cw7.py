def wartosc_ciagu(n):
    return n*n+n+1

def finalnie(liczba):
    n = 1
    while True:
        if liczba%wartosc_ciagu(n) == 0:
            return True, wartosc_ciagu(n), n
        if wartosc_ciagu(n) > liczba:
            return False
        n += 1
liczba = int(input("L:"))

print(finalnie(liczba))