# zad2

def rek():
    c = 0
    def rek2(used=[1],p=1):
        nonlocal c
        if len(used) == 9:
            c+=1
            return
        for i in range(2, 10):
            if i not in used:
                if i in [2, 3, 5, 7]:
                    if abs(used[p-1] - i) >= 2 and used[p-1] not in [2, 3, 5, 7]:
                        rek2(used + [i], p + 1)
                else:
                    if abs(used[p-1] - i) >= 2:
                        rek2(used + [i], p + 1)
    rek2()
    return c

print(rek())