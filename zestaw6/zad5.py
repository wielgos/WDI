# Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
# każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
# 110100 nie jest możliwe.

def digits(n):
    counter = 0
    while n != 0:
        n -= n % 10
        n //= 10
        counter += 1
    return counter


def get_digit(n,p): #potrzeba digits()
    q = digits(n)
    if p==q:
        return n%10
    n = n - n%(10**(q-p))
    b = n %(10**(q-p+1))
    b //=10**(q-p)
    return b


def is_prime(n):
    if n==2: return True
    if n%2==0: return False
    for i in range(3,int(n**(0.5)+1),2):
        if n%i == 0:
            return False
    return True


def decimal(n):
    s = 0
    d = digits(n)
    p = d-1
    print(d)
    print(get_digit(n,p))
    for i in range(1,d+1):
        print(s)
        s += get_digit(n,i)*2**(p)
        p -= 1
    return s

def to_decimal(t,start,stop):
    s = 0
    pow = 0
    for i in range(stop-1,start+1,-1):
        s += t[i]*2**pow
        pow += 1
    return s

def f(t,i1=0,i2=1):
    if i2==len(t):
        if is_prime(to_decimal(t,i1,i2)):
            return True
        return False
    if i2-i1>30:
        return False
    if is_prime(to_decimal(t,i1,i2)):
        return f(t,i2,i2+1)
    else:
        return f(t,i1,i2+1)


T = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1]
T2 = [1,1,0,1,0,0]
T3 = [1,1,1,0,1,1]
T4 = [1]*31

print(f(T4))