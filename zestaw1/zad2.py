n=int(input())

p1=0
p2=1
t1=0
t2=1

s=0

while s<n:
    s+=p2
    m=p2
    p2=p1+p2
    p1=m
    if s==n:
        print("istn")
        exit()
while s>n:
    s-=t2
    m=t2
    t2=t1+t2
    t1=m
    if s==n:
        print("istn")
        exit()