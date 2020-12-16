
#sr 14 gr 2016zad2adwki2b


def sum_col(t,w1,k1):
    s = 0
    for i in range(8):
        if i!=w1:
            s += t[i][k1]
    return s

def f(t,w):
    largest = -1
    col1 = -1
    col2 = -1
    for i in range(7):
        for k in range(i+1,8):
            s=0
            used = []
            s += sum_col(t,w[i],i) + sum_col(t,w[k],k)
            for l in range(8):
                if l==i or l==k or w[l] in used:
                    continue
                s -= t[w[l]][i]
                s -= t[w[l]][k]
                used += [w[l]]
            if s>largest:
                print(largest)
                largest = s
                col1 = i
                col2 = k
    return col1,col2

t=[[1,2,3,4,5,9,7,8],
   [1,2,3,4,5,9,7,8],
   [1,2,3,4,5,9,7,8],
   [1,2,3,4,5,9,7,8],
   [1,2,3,4,5,9,7,8],
   [1,2,3,4,5,9,7,8],
   [1,2,3,4,5,9,7,8],
   [1,2,3,4,5,9,7,8]]

w=[1,1,1,1,1,1,1,1]

print(f(t,w))