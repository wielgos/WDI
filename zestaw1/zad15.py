x = (0.5)**(0.5)
wynik = x
for i in range(200000):
    x = (0.5 + 0.5 * x)**(0.5)
    wynik *= x
pi=2/wynik
print(f"Pi to: {pi}")