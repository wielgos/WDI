# Zadanie 16. Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli:
# mają tę samą liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne,
# na przykład "ula" → 117, 108, 97 oraz "exe" → 101, 120, 101.
# Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy
# jest możliwe zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1.
# Dodatkowo funkcja powinna wypisać znaleziony wyraz.


def waga(s1, s2):
    samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
    w1 = 0  # sumy kodów ascii wyrazu1
    w2 = 0  # sumy kodów ascii wyrazu2
    sm1 = 0  # liczba samogłosek wyrazu1
    sm2 = 0  # liczba samogłosek wyrazu2
    for letter in s1:
        w1 += ord(letter)  # chr(65) = 'A', ord('A') = 65
        if letter in samogloski:
            sm1 += 1
    for letter in s2:
        w2 += ord(letter)
        if letter in samogloski:
            sm2 += 1
    if w1 == w2 and sm1 == sm2:
        #print(s1,"-> w1=",w1,"sm1=",sm1)
        #print(s2, "-> w2=", w2, "sm2=", sm2)
        return True
    return False


def wyraz(s1, s2, p=0, podwyraz="", found=[]):
    if podwyraz not in found and waga(podwyraz, s2):
        found += [podwyraz]
        print(podwyraz)
    if p == len(s1):
        return False
    return wyraz(s1, s2, p + 1, podwyraz + s1[p], found) or wyraz(s1, s2, p + 1, podwyraz, found)


#wyraz("matrix", "exe")
wyraz("irrational","ol")
