# Zadanie 14. Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w
# grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć
# wartości prawdopodobieństwa dla N z zakresu 20-40

from random import randint

if __name__ == "__main__":
    s = set()

    N = 23
    ilosc_eksperymentow = 10000

    proby_udane = 0
    for j in range(0, ilosc_eksperymentow):
        for i in range(0, N):
            rand = randint(1, 365)
            if rand not in s:
                s.add(rand)
            else:
                proby_udane += 1
                s.clear()
                break
    print( proby_udane / ilosc_eksperymentow )
