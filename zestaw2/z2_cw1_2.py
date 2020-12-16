a1 = 1
a2 = 1

liczba = 701946498742074906890411203788459425016826024662306600197514969264790619749846414554810186865373710052179086536350183778395661069668157255876823120

while a2 <= liczba:
    a1, a2 = a2, a1 + a2
    if a2 > liczba:
        a1, a2 = a2 - a1, a1
        break
# a2 = najwieksza liczba z ciagu fibonacci mniejsza od liczby

c1,c2=1,1
while True:
    if liczba%a2==0:
        while c2<=a2:
            if c2==liczba/a2:
                print(f"{liczba} Tak: {c2} * {a2}")
                exit()
            c1,c2=c2,c2+c1
    a1, a2 = a2 - a1, a1
    if a2==1:
        print(f"{liczba} Nie")
        break
