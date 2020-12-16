# 2b 16sty 2020

def A(x):
    return x + 3


def B(x):
    return 2 * x


def C(x):
    n = str(x)
    r = ""
    for num in n:
        if int(num) % 2 != 0:
            r += str(int(num) - 1)
        else:
            r += num
    return int(r)


def rek(x,y,n):
    def rek2(x,y,n,last,chain=""):
        if x == y:
            return len(chain)
        if n == 0:
            return 999999
        if last=="A":
            return min(rek2(B(x),y,n-1,"B",chain+"B"),rek2(C(x), y, n - 1, "C",chain+"C"))
        elif last=="B":
            return min(rek2(A(x),y,n-1,"A",chain+"A"),rek2(C(x), y, n - 1, "C",chain+"C"))
        elif last == "C":
            return min(rek2(A(x),y,n-1,"A",chain+"A"),rek2(B(x), y, n - 1, "B",chain+"B"))
        else:
            return min(min(rek2(B(x),y,n-1,"B",chain+"B"),rek2(C(x), y, n - 1, "C",chain+"C")),rek2(A(x),y,n-1,"A",chain+"A"))
    res = rek2(x,y,n,"E")
    return -1 if res==999999 else res


# def rek(x, y, n):
#     def rek2(x, y, n, last="none", chain=""):
#         nonlocal length
#         if x == y:
#             return len(chain)
#         if n == 0:
#             return n+1
#         if last == "A":
#             rek2(B(x), y, n - 1, "B", chain + "B")
#             rek2(C(x), y, n - 1, "C", chain + "C")
#         elif last == "B":
#             rek2(A(x), y, n - 1, "A", chain + "A")
#             rek2(C(x), y, n - 1, "C", chain + "C")
#         elif last == "C":
#             rek2(A(x), y, n - 1, "A", chain + "A")
#             rek2(B(x), y, n - 1, "B", chain + "B")
#         else:
#             rek2(B(x), y, n - 1, "B", chain + "B")
#             rek2(C(x), y, n - 1, "C", chain + "C")
#             rek2(A(x), y, n - 1, "A", chain + "A")
#
#
#
#     rek2(x, y, n)


print(rek(23, 39, 4))
