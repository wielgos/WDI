# Zadanie 15. Problem 8 Hetmanów (treść oczywista)

def h(N):
    tab_pos = [-1] * N
    t0 = [False] * N  # kolumny
    t1 = [False] * (2 * N - 1)  # 1diag
    t2 = [False] * (2 * N - 1)  # 2diag
    stop = False

    def rek(w, k):
        nonlocal stop
        if w == N:
            print(tab_pos)
            stop = True
        else:
            if t0[k] == True or t1[w + k] == True or t2[w - k + N - 1] == True:
                return
            t0[k] = t1[w + k] = t2[w - k + N - 1] = True
            tab_pos[w] = k
            for i in range(N):
                if stop:
                    return
                rek(w+1,i)
            t0[k] = t1[w + k] = t2[w - k + N - 1] = False

    for i in range(N):
        rek(0,i)



t = [[0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]]

h(20)
