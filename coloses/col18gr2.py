# Mikołaj Wielgos
# Data: 18.12.2020
# probwalem zamieniac sobie na listy i patrzec po listach
# wypisuje mi dobrze dane liczby

def divide(n):
    def is_prime(n):
        if n == 2: return True
        if n % 2 == 0: return False
        for i in range(3, int(n ** (0.5) + 1), 2):
            if n % i == 0:
                return False
        return True

    def digits(n):
        counter = 0
        while n != 0:
            n -= n % 10
            n //= 10
            counter += 1
        return counter
    
    def get_digit(n, p):  # indeksowanie od 1
        q = digits(n)
        if p == q:
            return n % 10
        n = n - n % (10 ** (q - p))
        a = n % (10 ** (q - p + 1))
        a //= 10 ** (q - p)
        return a

    def conv_to_list(n):
        digs = digits(n)
        l = []
        c = 1
        while digs > 0:
            l += [get_digit(n, c)]
            digs -= 1
            c += 1
        return l

    def conv_to_int(n):
        s = 0
        length = len(n) - 1
        for e in n:
            s += e * 10 ** (length)
            length -= 1
        return s

    def conv_index1_index2(l, index1, index2):
        p = []
        for i in range(index1, index2):
            p += [l[i]]
        return p

    def rek(nlist, index1=0, index2=1, slices=0, numbers=[]):
        if index2 == len(nlist) + 1:
            print(numbers)
            if is_prime(slices):
                for e in numbers:
                    if is_prime(conv_to_int(e)) == False:
                        return False
                return True
            return False
        else:
            if index2 != len(nlist) and index2 != 1:
                if rek(nlist, index1, index2 + 1, slices, numbers):
                    return True
            if rek(nlist, index2, index2 + 1, slices + 1, numbers + [conv_index1_index2(nlist, index1, index2)]):
                    return True

    number = conv_to_list(n)
    if rek(number):
        return True
    else:
        return False


print(divide(22222))

# do wyjebania to:
# *
# 64        elif index2==len(nlist) and len(numbers)==1:
# 65          return False
# *
# przed ifem pierwszym po else: dodac:
# if index2!=len(nlist):
# *
# i na koniec dodac *else: return False
