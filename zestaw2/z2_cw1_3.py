def funkcja(liczba):
    if liczba==1: return True,1,1
    a1, a2 = 1, 1
    b1, b2 = 1, 1
    while a2<=liczba:
        a1, a2 = a2, a1+a2
    a1, a2 = a2-a1, a1
    while a2*b2!=liczba and b2<=a2:
        if a2*b2<liczba:
            b1, b2 = b2, b1+b2
        elif a2*b2>liczba:
            a1, a2 = a2 - a1, a1
        if a2*b2==liczba:
            return True,b2,a2
    return False

n = int(input())
print(funkcja(n))