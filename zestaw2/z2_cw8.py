def canBeFibSum(liczba):
    fibA_1, fibA_2 = 0, 1
    fibB_1, fibB_2 = 0, 1
    suma = 0
    # while fibB_2 <= liczba:
    #     fibB_1, fibB_2 = fibB_2, fibB_2 + fibB_1
    # fibB_1, fibB_2 = fibB_2, fibB_2 - fibB_1
    while True:
        if suma > liczba:
            suma -= fibA_2
            if suma < liczba:
                return False
            fibA_1, fibA_2 = fibA_2, fibA_1 + fibA_2
        elif suma < liczba:
            suma += fibB_2
            fibB_1, fibB_2 = fibB_2, fibB_1 + fibB_2
        else:
            return True

n = int(input())

for i in range (n+1,1000+1):
    if(canBeFibSum(i)==False):
        print(i)
        break



