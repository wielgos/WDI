def binarnie(n):
    if n == 0: return 0
    if n == 1: return 1
    a = 2
    while a <= n:
        a = a * 2
    a = a / 2
    binary = ""
    while True:
        if n >= a:
            n = n - a
            binary = binary + "1"
        else:
            binary = binary + "0"
        a = a / 2
        if (n == 0 and a == 0.5):
            break
    print(binary)
    return int(binary)


def palindrom(n):
    liczbastr = str(n)
    if len(liczbastr) % 2 == 0:
        for i in range(0, (len(liczbastr) // 2)):
            if liczbastr[i] != liczbastr[len(liczbastr) - 1 - i]:
                return False
        return True
    elif len(liczbastr) % 2 == 1:
        for i in range(0, (len(liczbastr) // 2)):
            if liczbastr[i] != liczbastr[len(liczbastr) - 1 - i]:
                return False
        return True


liczba = 784321123487

print(palindrom(liczba))
print(palindrom(binarnie(liczba)))
