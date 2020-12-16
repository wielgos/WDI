def ciag_a(n):
    if n == 0: return 0
    if n == 1: return 1
    return ciag_a(n-1) - ciag_b(n-1) * ciag_a(n-2)

def ciag_b(n):
    if n == 0: return 2
    return ciag_b(n-1) + 2 * ciag_a(n-1)

if __name__ == "__main__":
    n = 0 # our starting point
    while True:
        liczba = int(input("liczba="))
        if liczba == ciag_a(n):
            print(ciag_b(n))
        else:
            break
        n += 1