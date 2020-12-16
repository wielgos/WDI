# Zadanie 17. Dane są dwie liczby naturalne z których budujemy trzecią liczbę.
# W budowanej liczbie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych.
# Wzajemna kolejność cyfr każdej z liczb wejściowych musi być zachowana.
# Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
# 75123, 17253, itd.
# Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.
def digits(n):
    counter = 0
    while n != 0:
        n -= n % 10
        n //= 10
        counter += 1
    return counter


def is_prime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** (0.5) + 1), 2):
        if n % i == 0:
            return False
    return True


def get_digit(n, p):
    q = digits(n)
    if p == q:
        return n % 10
    a = n % (10 ** q - p)
    a //= 10 ** (q - p)
    return a


def rek(a, b, n=0):
    counter = 0
    if a==0 and b==0 and is_prime(n):
        print(n)
        return 1
    if a!=0:
        counter += rek(a - (get_digit(a, 1) * 10 ** (digits(a) - 1)), b, n + get_digit(a, 1) * 10 ** (digits(a) + digits(b)-1))
    if b!=0:
        counter += rek(a , b - (get_digit(b, 1) * 10 ** (digits(b) - 1)), n + get_digit(b, 1) * 10 ** (digits(a) + digits(b)-1))

    return counter


a = 21
b = 37
print(rek(a,b))
