def reszta(n,t, last):
    counter = 0
    if n==0:
        return 1
    if n<0:
        return 0
    for e in t:
        if n-e>=0 and e>=last:
            counter += reszta(n-e,t, e)
    return counter


t = [3,5,2]
print(reszta(15,t,-1))