# sr 14 gr 2016zad2adwki2b


def sum_col(t, w1, k1):
    s = 0
    for i in range(8):
        if i != w1:
            s += t[i][k1]
    return s


def f(t, w):
    largest = -1
    col1 = -1
    col2 = -1
    for i in range(7):
        for k in range(i + 1, 8):
            s = 0
            s += sum_col(t, w[i], i) + sum_col(t, w[k], k)
            used = []
            for l in range(8):
                if l == i or l == k:
                    continue
                elif w[l] not in used:
                    s -= t[w[l]][i]
                    s -= t[w[l]][k] #s to roznica jest ja kcos
                    used += [w[l]]
            if s > largest:
                largest = s
                print(largest)
                col1 = i
                col2 = k
    return col1, col2


t = [[1, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0]]

w = [1, 1, 1, 1, 2, 1, 1, 1]

g = [[8, 5, 5, 3, 6, 7, 3, 6],
     [5, 6, 7, 2, 6, 5, 3, 5],
     [1, 3, 5, 3, 5, 9, 7, 3],
     [2, 3, 4, 2, 6, 3, 3, 1],
     [7, 7, 9, 8, 2, 9, 9, 5],
     [4, 4, 5, 5, 4, 3, 8, 2],
     [4, 5, 7, 8, 2, 5, 2, 3],
     [7, 7, 8, 6, 9, 3, 5, 9]]

g2 = [0, 2, 1, 4, 4, 4, 6, 7]

print(f(t, w))
