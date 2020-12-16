a1 = 1
a2 = 1

b1 = 1
b2 = 1

liczba = 71778070001175615

while a2 <= liczba:
    a1, a2 = a2, a1 + a2
    if a2 > liczba:
        a1, a2 = a2 - a1, a1
        savea2 = a2
        savea1 = a1
        break
# a2 = najwieksza liczba z ciagu fibonacci mniejsza od liczby
Ą
if (a2 == liczba):
    print("yes")
    exit()

while True:
    while a2 != 1:
        a1, a2 = a2 - a1, a1
        if b2 * a2 == liczba:
            print("Tak", liczba, b2, a2)
            exit()
    b1, b2 = b2, b1 + b2
    a2 = savea2
    a1 = savea1
    if (b2 == a2):
        break
