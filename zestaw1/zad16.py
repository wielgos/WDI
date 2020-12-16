def funkcja(a_n):
        return (a_n % 2) * (3 * a_n + 1) + (1 - a_n % 2) * (a_n / 2)


maxvalue=0

for i in range (2,10001):
    a_n=i
    counter=0
    while(a_n-1!=0):
        a_n=funkcja(a_n)
        counter+=1
    if(counter>maxvalue):
        maxvalue=counter
        liczba=i
print(maxvalue,liczba)