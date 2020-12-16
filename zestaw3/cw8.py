def jump(start, step):
    if start % 2 == 0:
        print("Tak")
        exit()
    if start < 2 or start == 3 or step == 0: return False
    return jump(start-step,f(start-step))



def f(n):
    for i in range (2,n+1):
        for j in range(2,i+1):
            if n%j == 0:
                jump(n,j)
    return 0





if __name__ == "__main__":
    n = 999972
    print(jump(n, f(n)))