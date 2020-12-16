# Zadanie 4. Dana jest tablica zawierająca liczby wymierne. Proszę napisać funkcję, która policzy
# występujące w tablicy ciągi arytmetyczne (LA) i geometryczne (LG) o długości większej niż 2. Funkcja powinna
# zwrócić wartość 1 gdy LA > LG, wartość -1 gdy LA < LG oraz 0 gdy LA = LG.

def podciagi_ar(t):
    N = len(t)
    ciagi = 0
    for i in range(N-2):
        a1 = t[i]
        for k in range(i+1,N-1):
            a2 = t[k]
            r = a2-a1
            dl_ciagu = 2
            for l in range(k+1,N):
                if t[l] == a2 + r:
                    dl_ciagu += 1
                    a2 = t[l]
            ciagi += dl_ciagu-2
    return ciagi

def podciagi_geo(t):
    N = len(t)
    ciagi = 0
    for i in range(N-1):
        a1 = t[i]
        for k in range(i+1,N):
            a2 = t[k]
            if a1 != 0:
                q = a2 / a1
            elif a1 == 0 and a2 == 0:
                q = 0
            dl_ciagu = 2
            for l in range(k+1,N):
                if t[l] == a2*q:
                    dl_ciagu += 1
                    a2 = t[l]
            ciagi += dl_ciagu -2
    return ciagi

def funkcja(t):
    LA = podciagi_ar(t)
    print("LA:",LA)
    LG = podciagi_geo(t)
    print("LG:", LG)
    if LA > LG:
        return 1
    elif LA < LG:
        return -1
    else:
        return 0


t1 = [5,4,3,2,1]
t2 = [1,2,4,8,16]
t3 = [1,2,4,3,16,4]
t4 = [0.25,0.5,0.75,1,1.25]
t5 = [1,2,3,0,0,0]


print(funkcja(t1))
