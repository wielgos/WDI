# Zadanie 32. Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
# na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
# jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.


def funkcja(T,k,u1=[],u2=[],p=0,s1=0,s2=0,m1=0,m2=0):
    if m1 + m2 == k and s1 == s2:
        print(u1)
        print(u2)
        return True
    if p==len(T):
        return False
    return funkcja(T,k,u1 + [T[p]],u2,p+1,s1+T[p],s2,m1+1,m2) or funkcja(T,k,u1,u2 + [T[p]],p+1,s1,s2+T[p],m1,m2+1) or funkcja(T,k,u1,u2,p+1,s1,s2,m1,m2)



T=[1,2,3,2,2,9,9,9]
T2=[6,19,2,14,6,20,2,15,8,10]
print(funkcja(T,6))