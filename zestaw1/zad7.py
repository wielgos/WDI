n = int(input())

p=4
t=7

while p*t<=n:
    if p*t==n:
        print("tak")
        exit()
    else:
        m=p
        p=p+t
        t=m
print("nie")