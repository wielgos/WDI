def function(x):
    return x**x-2020

a=1 #ujemne
b=5 #dodatnie

for i in range(1000):
    x1=(a+b)/2
    if function(x1)>0:
        b=x1
    elif function(x1)==0:
        print(x1)
    else:
        a=x1
    print(x1)
