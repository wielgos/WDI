liczba = 10

s = liczba

q = 1
c = 1

while s != 0:
    if s >= 3:
        s -= 3
        q = q * 3
    if s == 1:
        q = 1
        s = liczba
        s -= c * 2
        q = q * (2 ** c)
        c += 1
    elif s == 2:
        q = q * 2
        break

print(liczba, q)
