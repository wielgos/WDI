def check_235(n):
    if n==1: return True
    while n!=1:
        if n%2==0:
            n=n/2
        elif n%3==0:
            n=n/3
        elif n%5==0:
            n=n/5
        else:
            return False
    return True

c=0
n = int(input("N:"))
for i in range(1,n+1):
    if check_235(i)==True:
        c+=1
print("Takich liczb jest:", c)