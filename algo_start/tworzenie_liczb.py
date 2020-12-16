def is_prime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** (0.5) + 1), 2):
        if n % i == 0:
            return False
    return True


def count(a, b, n=0):
    if a == [] and b == []:
        return 1 if is_prime(n) else 0
    c = 0
    if len(a) > 0:
        nn = n * 10 + a[0]
        c += count(a[1:], b, nn)
    if len(b) > 0:
        nn = n * 10 + b[0]
        c += count(a, b[1:], nn)

    return c


a = [2, 1]
b = [3, 7]
c,d=21,37
print(count(a, b))
