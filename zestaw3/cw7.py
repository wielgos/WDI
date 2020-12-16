if __name__ == "__main__":
    N = 100
    tablica = [-1]*N
    t = int(input("t="))
    czy_cyfra_nieparzysta = None
    for i in range(0,t):
        x = input(f"t_{i}=")
        for number in x:
            if int(number) % 2 == 1:
                czy_cyfra_nieparzysta = True
            else:
                czy_cyfra_nieparzysta = False
        if czy_cyfra_nieparzysta == True:
            break
        tablica[i] = int(x)
    print(czy_cyfra_nieparzysta)
