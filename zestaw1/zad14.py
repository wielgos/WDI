from math import pi


def silnia(n):
    q = 1
    for i in range(2, n + 1):
        q = q * i
    return q


s = 0
x =

sz1 = 5
sz2 = 4
n = 0
while (abs(sz1 - sz2) > 0.0000000005):
    sz1, sz2 = (((-1) ** n) * (x ** (2 * n))) / silnia(2 * n), sz1
    s += sz1
    n += 1
print(s)
