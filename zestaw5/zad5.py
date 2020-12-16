# Zadanie 5. Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury dane =
# [(x1, y1),(x2, y2),(x3, y3), ...(xN , yN )] Proszę napisać funkcję, która zwraca wartość True jeżeli
# zbiorze istnieją 4 punkty wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
# tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
# punktów.


def funkcja(dane):
    N = len(dane)
    s = set()
    for i in range(N-3):
        w1 = dane[i][0]
        k1 = dane[i][1]
        for j in range(i+1,N-2):
            w2 = dane[j][0]
            k2 = dane[j][1]
            for l in range(j + 1, N - 1):
                w3 = dane[l][0]
                k3 = dane[l][1]
                for k in range(l+1,N):
                    w4 = dane[k][0]
                    k4 = dane[k][1]
                    s.update([w1,w2,w3,w4,k1,k2,k3,k4])
                    if 4 >= len(s) >= 2:
                        a, b = min(w1,w2,w3,w4), max(k1,k2,k3,k4)
                        for element in dane:
                            found = False
                            print(element[0],element[1],a,b)
                            if (element[0] > a and element[0] < b) and (element[1] > a and element[1] < b):
                                found = True
                                break
                        if found == False:
                            return True
                    s.clear()
    return False




dane = [(2,1),(5,1),(2,4),(5,4),(4,1)]
print(funkcja(dane))
