def is_prime(n):
    if n==1: return False
    if n==2: return True
    if n%2==0: return False
    for i in range(3,int(n**(0.5)+1),2):
        if n%i==0:
            return False
    return True

def f(t1,t2,p=0,s=0):
    #print(s)
    if p==len(t1):
        if is_prime(s):
            print(s)
            return 1
        else:
            return 0
    else:
        return f(t1,t2,p+1,s + t1[p]) or f(t1,t2,p+1,s+t2[p])




t1 = [1,3,2,4]
t2 = [9,3,4,1]

print(f(t1,t2))