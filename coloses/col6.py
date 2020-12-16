#kartk gra zad1




def f(t,w1,k1,w2,k2):
    def row_value(t,w1,k1):
        n = len(t)
        s = 0
        for i in range(0,n):
            if i==k1:
                continue
            s+= t[w1][i]
        #kolumny^
        return s
    def col_value(t,w1,k1):
        n = len(t)
        s = 0
        for i in range(0,n):
            if i==w1:
                continue
            s+= t[i][k1]
        return s
    def szach_value_2(t,w1,k1,w2,k2):
        s = 0
        if w1==w2:
            s += row_value(t,w1,k1) #nie mam w1k1
            s += col_value(t,w1,k1) + col_value(t,w2,k2)
            s += t[w1][k1]
        elif k1==k2:
            s += col_value(t, w1, k1)  # nie mam w1k1
            s += row_value(t, w1, k1) + row_value(t, w2, k2)
            s += t[w1][k1]
        else:
            s += col_value(t,w1,k1) + col_value(t,w2,k2)
            s += row_value(t,w1,k1) + row_value(t,w2,k2)
            s -= t[w1][k2]
            s -= t[w2][k1]
        return s

    start_value = szach_value_2(t,w1,k1,w2,k2)
    print(start_value)
    for i in range(len(t)):
        if i!=k2:
            if szach_value_2(t,w1,i,w2,k2)>start_value:
                return True
    for i in range(len(t)):
        if i!=w2:
            if szach_value_2(t,i,k1,w2,k2)>start_value:
                return True
    for i in range(len(t)):
        if i!=w1:
            if szach_value_2(t,w1,k1,i,k2)>start_value:
                return True
    for i in range(len(t)):
        if i!=k1:
            if szach_value_2(t,w1,k1,w2,i)>start_value:
                return True
    return False




t = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(f(t,0,0,1,1))