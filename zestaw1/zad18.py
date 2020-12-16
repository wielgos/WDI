A=880870922056  

a2=A/2
a1=A/3
a3=A/(a2*a1)


def pierw3stopnia(A):
    a=A/2
    b=A/3
    c=A/(a*b)
    boki=[a,b,c]
    boki.sort()
    for i in range(1,10000):
        boki[0]=float(boki[1]+boki[2])/2
        boki.sort()
        boki[2]=A/float(boki[1]*boki[0])
    print(boki[0])
    return

for i in range (1,10000):
    if a1<a2 and a1<a3:
        if a2>a3:
            a1=(a1+a2)/2
            a2=A/(a1*a3)
        else:
            a1=(a3+a1)/2
            a3=A/(a1*a2)
    elif a2<a3 and a2<a1:
        if a1>a3:
            a2=(a1+a2)/2
            a1=A/(a1*a3)
        else:
            a2=(a3+a1)/2
            a3=A/(a1*a2)
    elif a3<a1 and a3<a2:
        if a2>a1:
            a3=(a3+a2)/2
            a2=A/(a1*a3)
        else:
            a3=(a3+a1)/2
            a1=A/(a2*a3)

print(a3)
pierw3stopnia(A)

