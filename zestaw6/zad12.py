# Zadanie 12. Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki


def f(t,q,n,p=0,used=[]):
    if n==1:
        if t[p]==q:
            used = used + [t[p]]
            print(used)
            return 1
        else:
            return 0
    if p==len(t):
        return 0
    if q%t[p]==0:
        return f(t,q//t[p],n-1,p+1,used + [t[p]]) or f(t,q,n,p+1)
    else:
        return f(t,q,n,p+1)


t=[1,2,3,4]

print(f(t,6,2))



