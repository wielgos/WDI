#szachownica domino

def nwd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        b, a = a % b, b
    return a

def f(t,domw=[],domk=[],p=0,last='none'):
    print(domw, domk)
    if len(domw)==4:
        if nwd(nwd(t[domw[0]][domk[0]],t[domw[1]][domk[1]]),nwd(t[domw[2]][domk[2]],t[domw[3]][domk[3]]))==1:
            return True
        else:
            return False
    if p==len(t):
        return False
    for i in range(len(t)):
        #poziomo
        if i+1<=len(t)-1 and len(domw)<=2 and i not in domk and last != 'r':
            if f(t,domw+[p,p],domk+[i,i+1],p+1,'r'):
                return True
        #pionowo
        if p+1<=len(t)-1 and len(domw)<=2 and i not in domk and last != 'p':
            if f(t,domw+[p,p+1],domk+[i,i],p+2,'p'):
                return True
        if f(t, domw, domk, p + 1,last):
            return True


t = [[2,3,5],
     [7,11,13],
     [17,19,23]]

print(f(t))
