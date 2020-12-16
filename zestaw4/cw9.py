# Zadanie 9. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
# poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
# narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
# czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.

def funkcja(t, iloczyn):
    N = len(t)
    i = 3
    while i <= N:
        for kw in range(0, N - i + 1):
            for kk in range(0, N - i + 1):
                q = 1
                if i + kw > N:
                    continue
                if i + kk > N:
                    continue
                q = q * t[0 + kw][0 + kk] * t[i - 1 + kw][i - 1 + kk] * t[0 + kw][i - 1 + kk] * t[i - 1 + kw][0 + kk]
                if q == iloczyn:
                    return (i + kw) // 2, (i + kk) // 2, True
        i = i + 2
    return False


if __name__ == "__main__":
    t = [[1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5]]
    print(funkcja(t, 25))
