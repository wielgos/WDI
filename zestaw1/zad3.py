
n = int(input())

a1=1
a2=1

b1=1
b2=1

suma =0

while True:
    if suma<n:
        suma+=a2
        a1,a2 = a2, a1+ a2
    if suma>n:
        suma-=b2
        b1,b2 = b2, b1+b2
        if suma<n:
            print("nie istn")
            exit()
    if suma==n:
        print("istn")
        exit()