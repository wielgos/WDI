for i in range(2, 1000000):
    s1 = 0
    s2 = 0
    for k in range(1, i // 2 + 1):
        if i % k == 0:
            s1 += k  # suma dzielnikow pierwszej liczby
    if (s1 <= i):
        continue
    for j in range(1, s1 // 2 + 1):
        if s1 % j == 0:
            s2 += j  # s1 to druga liczba
    if (s2 == i and i != s1):
        print("Okej:", i, s1)
