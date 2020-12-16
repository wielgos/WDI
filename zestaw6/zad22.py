# Zadanie 22. Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
# według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
# czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
# możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
# skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe

def is_prime(n):
    if n==1: return False
    if n==2: return True
    if n%2==0: return False
    for i in range(3,int(n**(0.5)+1),2):
        if n%i==0:
            return False
    return True

def funkcja(t,i=0,jmp=0):
    def czynniki(n):
        l=[]
        if is_prime(n):
            return l+[n]
        c = 2
        while n!=1:
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
                if i+e <= len(t)-1 and e<t[i+e]:
                    rek(t,i+e,jmp+1)
    r = -1
    rek(t)
    return r

t = [12,7,31,8,4,4]

print(funkcja(t))
