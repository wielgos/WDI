#2a 16 stycznia 2020

def na_system_k(number, k): #zwraca listę
    counter = 1
    while number >= k ** counter:
        counter += 1
    result = [-1]*counter
    i = counter -1
    while number != 0:
        result[i] = number % k
        number //= k
        i -= 1
    return result

def zgodnosc(n1,n2):
    c1 = c2 = 0
    for e in n1:
        if e%2==0:
            c1 += 1
    for e in n2:
        if e%2==0:
            c2 += 1


def check_on_pos(w1,k1,t1,t2):
    check = 0
    fine = 0
    for i in range(0,len(t2)):
        for j in range(0,len(t2)):
            if 0<=w1+i<=len(t1)-1 and 0<=k1+j<=len(t1)-1:
                    check +=1
                    num1 = na_system_k(t1[w1+i][k1+i],5)
                    num2 = na_system_k(t2[i][j],5)
                    if zgodnosc(num1,num2):
                        fine += 1
    if fine*100/check >=33:
        return True
    else: return False

def main(t1,t2):
    for i in range(len(t1)):
        for j in range(len(t1)):
            if check_on_pos(i,j,t1,t2):
                return True
    return False

