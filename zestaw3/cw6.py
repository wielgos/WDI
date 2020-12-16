from random import randint

def funkcja(t):
    for element in t:
        counter = 0
        for number in str(element):
            if int(number)%2!=0:
                break
            else:
                counter += 1
        if counter == len(str(element)):
            return False
    return True


def funkcja_v2(t):
    for element in t:
        counter = 0
        for number in str(element):
            if int(number)%2!=0:
                break
            else:
                counter += 1
        if counter == len(str(element)):
            return False
    return True


if __name__ == "__main__":

    t = int(input("t="))
    tablica = [randint(1,1000) for _ in range(t)]
    print(tablica)
    print(funkcja(tablica))
