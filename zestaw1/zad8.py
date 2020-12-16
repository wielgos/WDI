n = int(input())


if n < 2:
    print("Nie jest pierwsza")
else:
    i=2
    while i*i<=n:
        if n%i==0:
            print("nie")
            exit()
        i=i+1
    print("tak")