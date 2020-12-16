def funkcja(t, w=0, k=0):
    if w == len(t) - 1 and k == len(t) - 1:
        return True
    if w + 1 < len(t) and t[w + 1][k] > t[w][k]:
        return funkcja(t, w + 1, k)
    if k + 1 < len(t) and t[w][k + 1] > t[w][k]:
        return funkcja(t, w, k + 1)
    return False


t = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(funkcja(t))
