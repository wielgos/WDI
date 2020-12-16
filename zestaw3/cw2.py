if __name__ == "__main__":
    a = int(input("a="))
    b = int(input("b="))
    zbior_liczb_a = set()
    for n in str(a):
        zbior_liczb_a.add(int(n))

    # if len(str(a))!=len(str(b)):
    #     print("Nie skladaja sie z tych samych cyfr")
    #     exit()

    for n in str(b):
        if int(n) not in zbior_liczb_a:
            print("Nie skladaja sie z tych samych cyfr")
            exit()
    print("Skladaja sie z tych samych cyfr")