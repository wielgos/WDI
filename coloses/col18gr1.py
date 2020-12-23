# Mikołaj Wielgos
# Data: 18.12.2020

def suma_kolumny(t,k):
    N = len(t)
    s = 0
    for i in range(N):
        s += t[i][k]
    return s

def suma_wiersza(t,w):
    N = len(t)
    s = 0
    for i in range(N):
        s += t[w][i]
    return s

def chess(t):
    max_value = suma_kolumny(t, 0) + suma_wiersza(t, 0) + suma_kolumny(t, 1) + suma_wiersza(t, 1)
    max_value = max_value - suma_wiersza(t, 1)
    max_value = max_value - 2 * (t[0][0] + t[1][1])
    N = len(t)
    max_i, max_j = 0, 0
    max_i2, max_j2 = 1, 1
    for i in range(N):
        for j in range(N):  # [i][j] to pozycja 1 wiezy
            for i2 in range(N):
                for j2 in range(N):  # [i2][j2] to pozycja 2 wiezy
                    if i==i2 and j==j2:
                        continue
                    value = suma_kolumny(t, j) + suma_wiersza(t, i) + suma_kolumny(t, j2) + suma_wiersza(t, i2)
                    if i2 == i:  # jezeli stoja w obrebie tego samego wiersza
                        value = value - suma_wiersza(t, i2)
                        value = value - 2 * (t[i][j] + t[i2][j2])
                    elif j2 == j:  # jezeli stoja w obrebie tej samej kolumny
                        value = value - suma_kolumny(t, j2)
                        value = value - 2 * (t[i][j] + t[i2][j2])
                    else:
                        value = value - t[i][j2] - t[i2][j] - 2 * (t[i][j] + t[i2][j2])
                    if value > max_value:
                        max_value = value
                        max_i, max_j = i, j
                        max_i2, max_j2 = i2, j2
    return max_i, max_j, max_i2, max_j2
