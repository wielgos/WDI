# Zadanie 20. Dana jest N-elementowa tablica t zawierająca liczby naturalne
# mniejsze od 1000. Proszę napisać funkcję, która zwraca długość najdłuższego,
# spójnego fragmentu tablicy, dla którego w iloczynie jego elementów każdy czynniki
# pierwszy występuje co najwyżej raz. Na przykład dla
# tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22] wynikiem jest wartość 5.

def czynniki_pierwsze(n):
    if n == 1 : return -1
    s = set()
    while n!=1:
        for i in range(2,n+1):
            if n%i==0:
                s.add(i)
                n = n//i
                break
    return s



if __name__ == "__main__":
    N = 12
    t = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]
    x = []   
    czynniki = set ()
    podciagi = []
    for j in range(0,N):
        for i in range(j,N):
            s = czynniki_pierwsze(t[i])
            if (bool)(s.intersection(czynniki)) == False:  #s.intersection(czynniki) część wspólna z s i czynniki
                czynniki = czynniki.union(s) #łączę zbiory czynniki i zbiór s
                x.append(t[i])
            elif (bool)(s.intersection(czynniki)) == True or i == N-1:
                podciagi.append(x.copy())
                x.clear()
                czynniki.clear()
                break
    maxlen = 0
    print(podciagi)
    for i in range(0,len(podciagi)):
        if len(podciagi[i]) > maxlen:
            maxlen = len(podciagi[i])
    print(maxlen)