def nwd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

print(nwd(nwd(6,8),12))