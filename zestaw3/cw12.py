# Zadanie 12. Proszę napisać program, który wypełnia N-elementową tablicę t pseudolosowymi liczbami
# nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
# znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego
# ciągu arytmetycznego o ujemnej różnicy, przy założeniu, że kolejnymi
# wyrazami ciągu są elementy tablicy o kolejnych indeksach.

from random import randint

def losowa_nieparzyste(a,b):
    losowa = randint(a,b)
    if losowa % 2 == 0:
        if randint(0,1) == 0:
            losowa -= 1
        else:
            losowa += 1
    return losowa

def najdluzszy_ciag_arytmetyczny(ciag,r_dodatnie):
    dl = len(ciag)
    x = []
    podciagi_dod = []
    podciagi_ujem = []
    if r_dodatnie == True:
        for i in range(1,dl-1):
            r1 = ciag[i] - ciag[i-1]
            r2 = ciag[i+1] - ciag[i]
            if r1 == r2 and r1 > 0 and len(x)<3:
                x.append(ciag[i-1])
                x.append(ciag[i])
                x.append(ciag[i+1])
            elif len(x)>=3 and r1 == r2:
                x.append(ciag[i+1])
            elif len(x)>=3:
                podciagi_dod.append(x.copy())
                x.clear()
            if i == dl - 2 and len(x)>2:
                podciagi_ujem.append(x.copy())
                x.clear()
        print(podciagi_dod)
        maxlen = 0
        for list in podciagi_dod:
            if len(list) > maxlen:
                maxlen = len(list)
        return maxlen
    else:
        for i in range(1,dl-1):
            r1 = ciag[i] - ciag[i-1]
            r2 = ciag[i+1] - ciag[i]
            if r1 == r2 and r1 < 0 and len(x)<3:
                x.append(ciag[i-1])
                x.append(ciag[i])
                x.append(ciag[i+1])
            elif len(x)>=3 and r1 == r2:
                x.append(ciag[i+1])
            elif len(x)>=3:
                podciagi_ujem.append(x.copy())
                x.clear()
            if i == dl - 2 and len(x)>2:
                podciagi_ujem.append(x.copy())
                x.clear()
        print(podciagi_ujem)
        maxlen = 0
        for list in podciagi_ujem:
            if len(list) > maxlen:
                maxlen = len(list)
        return maxlen


if __name__ == "__main__":
    N = 1000
    t = [losowa_nieparzyste(1,99) for i in range(0,N)]
    maxlen_dod = najdluzszy_ciag_arytmetyczny(t,True)
    maxlen_ujem = najdluzszy_ciag_arytmetyczny(t,False)
    print("najdluzszy_dod ma dlugosc:",maxlen_dod)
    print("najdluzszy_ujem ma dlugosc:",maxlen_ujem)
    print("roznica: ",maxlen_dod-maxlen_ujem)
