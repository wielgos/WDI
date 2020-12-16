def suma_cyfr(n):
    k = 10
    s = 0
    while n != 0:
        t = n % k  # t = 2
        if t != 0:
            n = n - t
            s += t / (k / 10)
            k = k * 10
        elif t == 0:
            k = k * 10
    return int(s)


if __name__ == "__main__":
    for x in range (1,10**6):
        liczba = x
        suma_cyfr_czynnikow = 0
        while int(liczba)!=1:
            for i in range(2,int(liczba)+1):
                if liczba % i == 0:
                    liczba = liczba / i
                    suma_cyfr_czynnikow += suma_cyfr(i)
                    break
        if suma_cyfr_czynnikow == suma_cyfr(x):
            print(x)

