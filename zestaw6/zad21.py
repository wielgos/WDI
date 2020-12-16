# Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool.


def f(t, s):
    def r(t, s, w=0, k=0, usedw=[], usedk=[]):
        if s == 0:
            return True
        if w>7 or k>7 or s<0: return False
        else:

            for i in range(0,8):
                if i not in usedk:
                    if r(t, s - t[w][i], w + 1, 0, usedw + [w], usedk + [i]):
                        return True
            if r(t, s, w + 1, 0, usedw, usedk):
                return True

    return r(t, s)


t = [[25, 34, 56, 78, 89, 12, 13, 14],
     [64, 34, 56, 78, 89, 12, 13, 14],
     [53, 34, 56, 78, 89, 12, 13, 14],
     [78, 34, 56, 78, 89, 12, 13, 14],
     [96, 34, 56, 78, 89, 12, 31, 14],
     [75, 34, 56, 78, 89, 29, 13, 14],
     [64, 34, 56, 78, 11, 12, 13, 14],
     [58, 34, 56, 78, 89, 12, 13, 14]]

print(f(t, 209))
