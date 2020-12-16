# Zadanie 19. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
# szachowego.

def pole_istnieje(x, y, N):
    if x >= 0 and x <= N - 1 and y >= 0 and y <= N - 1:
        return True
    else:
        return False


def check(curr, jumped, curr_value, jumped_value, iloczyn, used):
    if curr_value * jumped_value == iloczyn:
        if (curr, jumped) not in used and (jumped, curr) not in used:
            used.add((curr, jumped))
            return True
    return False


def liczba_par_ele(t, iloczyn):
    N = len(t)
    l_par = 0
    used = set()
    for i in range(N):
        for j in range(N):  # i to wiersze j to kolumny
            curr = (i, j)
            curr_value = t[i][j]
            if pole_istnieje(i - 2, j + 1, N):
                jumped_value = t[i - 2][j + 1]
                jumped = (i - 2, j + 1)
                if check(curr, jumped, curr_value, jumped_value, iloczyn, used):
                    l_par += 1
            if pole_istnieje(i - 1, j + 2, N):
                jumped_value = t[i - 1][j + 2]
                jumped = (i - 1, j + 2)
                if check(curr, jumped, curr_value, jumped_value, iloczyn, used):
                    l_par += 1
            if pole_istnieje(i + 1, j + 2, N):
                jumped_value = t[i + 1][j + 2]
                jumped = (i + 1, j + 2)
                if check(curr, jumped, curr_value, jumped_value, iloczyn, used):
                    l_par += 1
            if pole_istnieje(i + 2, j + 1, N):
                jumped_value = t[i + 2][j + 1]
                jumped = (i + 2, j + 1)
                if check(curr, jumped, curr_value, jumped_value, iloczyn, used):
                    l_par += 1
            if pole_istnieje(i + 2, j - 1, N):
                jumped_value = t[i + 2][j - 1]
                jumped = (i + 2, j - 1)
                if check(curr, jumped, curr_value, jumped_value, iloczyn, used):
                    l_par += 1
            if pole_istnieje(i + 1, j - 2, N):
                jumped_value = t[i + 1][-2]
                jumped = (i + 1, j - 2)
                if check(curr, jumped, curr_value, jumped_value, iloczyn, used):
                    l_par += 1
            if pole_istnieje(i - 2, j - 1, N):
                jumped_value = t[i - 2][j - 1]
                jumped = (i - 2, j - 1)
                if check(curr, jumped, curr_value, jumped_value, iloczyn, used):
                    l_par += 1
            if pole_istnieje(i - 1, j - 2, N):
                jumped_value = t[i - 1][j - 2]
                jumped = (i - 1, j - 2)
                if check(curr, jumped, curr_value, jumped_value, iloczyn, used):
                    l_par += 1
    return l_par


if __name__ == "__main__":
    t = [[7, 30, 21, 3], [90, 1, 3, 9], [9, 32, 41, 52], [3, 2, 3, 44]]
    for e in t:
        for e2 in e:
            print(e2, end="\t")
        print()
    print(liczba_par_ele(t, 6))
