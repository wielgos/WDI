# Zadanie 13. Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na
# sumę składników. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.

def f(n, flag=True,l=[],prev=-1):
    if n == 0:
        print(l)
        return
    if flag:
        for i in range(1, n):
            if i>=prev:
                f(n - i, False,l + [i],i)
    else:
        for i in range(1, n + 1):
            if i>=prev:
                f(n - i, False,l + [i],i)

f(8)