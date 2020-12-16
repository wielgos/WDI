def suma_n_poteg(n):
    nstring = str(n)
    s = 0
    for i in range (0,len(nstring)):
        s += int(nstring[i])**(len(nstring))
    return s

if __name__ == "__main__":
    ile_cyfr = int(input())
    dziewiatki = ""
    for i in range(0, ile_cyfr):
        dziewiatki += "9"
    for i in range(1 * 10 ** (ile_cyfr - 1), int(dziewiatki) + 1):
        if suma_n_poteg(i) == i:
            print(i)