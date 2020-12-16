# Zadanie 25. Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać na pola
# o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz funkcję,
# która sprawdza, czy da się przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie da, zwraca
# -1.

def funkcja(t):
    def is_prime(n):
        if n == 1: return False
        if n == 2: return True
        if n % 2 == 0: return False
        for i in range(3, int(n ** (0.5) + 1), 2):
            if n % i == 0:
                return False
        return True

    def czynniki(n):
        l=[]
        c = 2
        while n!=1 and c <= n:
            if is_prime(c) and n%c==0:
                l += [c]
                while n%c==0:
                    n //= c
            c += 1
        return l

    def rek(t,i=0,jmp=0):
        nonlocal r
        if i==len(t)-1:
            r = jmp
            return
        else:
            for e in czynniki(t[i]):
                if i + e <= len(t) - 1:
                    rek(t, i+e, jmp+1)
        return

    r = -1
    rek(t)
    return r


t = [8,7,55,8,4,9]


print(funkcja(t))