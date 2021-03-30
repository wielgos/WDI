# Mikołaj Wielgos
# Data: 22.12.2020
# Rekurencyjny algorytm dodaje liczbę do tablicy, następnie przesuwa indeks, gdy ma już 3 liczby, sprawdza ich nwd
# jeżeli się zgadza -> zwiększa "licznik" o 1

def trojki(T):
    def nwd(a, b):
        a = abs(a)
        b = abs(b)
        while b != 0:
            b, a = a % b, b
        return a

    def rek(T,numbers=[],index=0,dist=0):
        #print(numbers)
        if len(numbers)==3:
            if nwd(numbers[0],numbers[1])==1 and nwd(numbers[0],numbers[2])==1 and nwd(numbers[1],numbers[2])==1:
                return 1
            else: return 0
        if index==len(T):
            return 0
        if len(numbers)!=0:
            if dist == 2:
                return rek(T, numbers + [T[index]], index + 1, 1)
            else:
                return rek(T, numbers + [T[index]], index + 1,1) + rek(T, numbers, index + 1, dist+1)
        else:
            return rek(T, numbers, index + 1, 0) + rek(T, numbers + [T[index]], index + 1,1)
    return rek(T)