#dzielenie tablicy na x kawalkow o takich samych sumach
def f(t):
    maxlen = 0
    def rek(t,poc=[],sumy=[],p=1,values=t[0]):
        nonlocal maxlen
        if p==len(t):
            if len(poc)>=1:
                a = sumy[0]
                for e in sumy:
                    if e!=a:
                        return 0
                maxlen = max(maxlen, len(poc) + 1)
            return
        else:
            rek(t,poc +[p],sumy + [values],p+1,t[p])
            rek(t,poc,sumy,p+1,values + t[p])
    rek(t)
    return maxlen


t = [1,2,3,1,5,2,2,2,6]

print(f(t))