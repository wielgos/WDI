if __name__ == "__main__":
    n = int(input("n="))
    l = [-1, -1]
    for i in range (2,n+1):
        l.append(1)

    i = 2
    while i*i<=n:
        if l[i]==1:
            k = n//i
            for j in range (1,k):
                l[i+i*j] = 0
        i += 1
    for i in range (2,n):
        if l[i]==1:
            print(i)