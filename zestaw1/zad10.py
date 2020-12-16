for i in range(2,1000000):
    s = 0
    for j in range(1,i//2+1):
        if i%j==0:
            s+=j
    if(s==i):
        print(i)

