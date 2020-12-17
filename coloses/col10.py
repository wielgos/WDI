t1 = [1,2,3,4]
t2 = [100,3,3,3]

def funk2(t1,t2,i1=0,i2=0,s1=0,s2=0,u1=[],u2=[]):

    if len(u1) == len(u2) and len(u1) != 0 and s1 == s2:
        return len(u1)
    if i1==len(t1):
        return 0
    c1 = funk2(t1, t2, i1 + 1, i2 + 1, s1 + t1[i1], s2 + t2[i2], u1 + [t1[i1]], u2 + [t2[i2]])
    c2 = funk2(t1, t2, i1+1 , i2 + 1, s1 , s2 + t2[i2], u1 , u2 + [t2[i2]])
    c3 = funk2(t1, t2, i1 + 1, i2+1 , s1 + t1[i1], s2 , u1 + [t1[i1]], u2)
    c4 = funk2(t1, t2, i1 + 1, i2 + 1, s1 , s2, u1 , u2)
    return max(c1,c2,c3,c4)




print(funk2(t1,t2))