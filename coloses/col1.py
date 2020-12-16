# Mikołaj Wielgos
# 20.11.2020
# Zadanie 1.
# Najpierw sprawdzam kolejne cząstki stringa np. "A" "AB" "ABC" "ABCD"
# Nastepnie sprawdzam czy występuja po sobie cyklicznie
# Nie zdążyłem zaimplementowac w całości


def multi(T):
    N = len(T)
    max_dl = 0
    for i in range(N):
        napis = T[i]
        for k in range(1,len(napis)+1):
            czastka = napis[:k]
            if len(napis)%len(czastka)==0:
                dl = len(napis) // len(czastka)
                if czastka*dl == napis and dl>1:
                    if len(czastka)>max_dl:
                        max_dl = len(czastka)
            else:
                continue
    return(max_dl)

T = ["ABCABCA   BC"]
#T = ["ABCABCABC", "AAAA", "ABAABA"]
print(multi(T))
