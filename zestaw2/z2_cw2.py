a = 2378
b = 19
n = 1000000

if a>b:
    k = a//b
    liczba = ""+str(k)+"."
    a = a-k*b
else:
    liczba="0."
poprzecinku =""

while len(poprzecinku)<n:
    poprzecinku = poprzecinku+str(a*10//b)
    a = a*10 - (a*10//b) * b
liczba = liczba + poprzecinku
print(liczba)