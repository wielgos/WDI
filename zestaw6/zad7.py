# Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza
# czy jest możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.


def funkcja(T,do_odwaz,p = 0):
    if do_odwaz == 0: return True
    if p==len(T): return False
    else: return funkcja(T,do_odwaz-T[p],p+1) or funkcja(T,do_odwaz,p+1)

T = [4,7,12,24,1]
print(funkcja(T,32))