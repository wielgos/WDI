def funkcja(x):
    return float(1 / x)


n = 10000

k = 23

podstawa = (k - 1) / n
x1 = 1 + podstawa / 2
s = 0
for i in range(0, n):
    s += podstawa * funkcja(x1)
    x1 += podstawa
print(s)
