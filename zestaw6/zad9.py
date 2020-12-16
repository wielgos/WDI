# Zadanie 9. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza
# czy jest możliwe odważenie określonej masy.
# * Odważniki można umieszczać na obu szalkach.
# * Program powinien wypisywać wybrane odważniki.


def funkcja(T,do_odwaz,used =[],p = 0):
    if do_odwaz == 0: return True,used
    if p==len(T): return False
    else: return funkcja(T, do_odwaz-T[p], used + [T[p]],p+1) or funkcja(T, do_odwaz, used, p+1) or funkcja(T, do_odwaz+T[p], used+[-T[p]], p+1)

# masę do odważenia mam na prawej stronie
# 1 - kładę na lewą stronę stronę
# 2 - pomijam odważnik
# 3 - kładę na prawą stronę

T = [1,3,9,27]