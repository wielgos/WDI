# Zadanie 6. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
# Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
# Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.

def rek(T,s_ele,s_in,pos=0):
    if s_in==s_ele and s_ele!=0:
        return(s_ele)
    if pos==len(T):
        return False
    return rek(T,s_ele+T[pos],s_in+pos,pos+1) or rek(T,s_ele,s_in,pos+1)


def funkcja(T):
    return rek(T,0,0)

T = [ 4,7,2,6,9,2,5,3 ]
#1+5+2 //0+3+5\\
print(funkcja(T))