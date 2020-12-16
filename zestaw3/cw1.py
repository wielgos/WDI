def konwersja(liczba,system):
    tablica_znakow = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    wynik = ""
    while liczba !=0 :
        wynik += str(tablica_znakow[liczba%system])
        liczba = liczba // system
    return wynik[::-1]



if __name__ == "__main__":


    liczba = int(input("liczba="))
    for i in range (2,17):
        print("System ",i," ",konwersja(liczba,i))
