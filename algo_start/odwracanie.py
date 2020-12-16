def odwracanie(a, p=0):
    if p == len(a) // 2:
        return
    a[len(a) - p - 1], a[p] = a[p], a[len(a) - p - 1]
    odwracanie(a, p + 1)


a = [1, 2, 3, 4, 5, 6, 7]
odwracanie(a)
print(a)
