if __name__ == "__main__":
    i = 0
    t = []
    while True:
        x = int(input())
        if x == 0:
            break
        t.append(x)
        i += 1
    for j in range(10):
        max = 0
        for elem in t:
            if int(elem)>max:
                max = int(elem)
        t.remove(max)
    print(max)
