def silnia(n):
    q=1
    if n==0:
        return 1
    for i in range (1,n+1):
        q=q*i
    return q
e=0
for i in range (0,10):
    e+=1/(silnia(i))
print(e)