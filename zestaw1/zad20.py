a_n = 24
b_n = 6
while abs(a_n - b_n) > 0.000000000001:
    a_n, b_n = (a_n * b_n) ** (0.5), (a_n + b_n) / 2.0
print(a_n)