def digits(n):
    counter = 0
    while n != 0:
        n -= n % 10
        n //= 10
        counter += 1
    return counter


# zamiana ostatnich 2 liczb miejscami
def A(n):
    last_dig = n % 10
    sec_last_dig = (n % 100) // 10
    n = n - n%100
    n = n + last_dig*10+sec_last_dig
    return n


def B(n):
    return n * 3


# usuniecie ostatniej cyfry
def C(n):
    a = n % (10 ** (digits(n) - 1))
    return a


def transform(x, y, steps_remain=7, chain=""):
    if x == y:
        return chain
    if steps_remain == 0:
        return False
    if digits(x) >= 2:
        return transform(A(x), y, steps_remain - 1, chain + "A") or transform(C(x), y, steps_remain - 1, chain + "C")
    return transform(B(x), y, steps_remain - 1, chain + "B")


if __name__ == '__main__':
    print(A(43))
