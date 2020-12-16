def s_binarny(n):
    if n == 0: return 0
    elif n == 1: return 1
    max_binary = 1 #max_binary najwieksza 2^x mniejsza/rowna od danej liczby
    while max_binary <= n:
        max_binary *= 2
    max_binary = max_binary/2
    binarnie = ""
    while True:
        if max_binary <= n:
            n -= max_binary
            max_binary = max_binary/2
            binarnie = binarnie + "1"
        elif max_binary > n:
            max_binary = max_binary/2
            binarnie = binarnie +"0"
        if max_binary==0.5 and n==0:
            return int(binarnie)

def s_czworkowy(n):
    czworkowo = ""
    n_binarnie = s_binarny(n)
    if len(str(n_binarnie))%2 == 1:
        nstr = "0" + str(n_binarnie)
    else:
        nstr = str(n_binarnie)
    for i in range(0,len(nstr),2):
        if (nstr[i]+nstr[i-1])=="00":
            czworkowo += "0"
        elif (nstr[i]+nstr[i-1])=="01":
            czworkowo += "1"
        elif (nstr[i]+nstr[i-1])=="10":
            czworkowo += "2"
        elif (nstr[i]+nstr[i-1])=="11":
            czworkowo += "3"
    return int(czworkowo)

def s_szesnastkowy(n):
    symbole_szesnastkowe=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    n_binarnie = s_binarny(n)
    k = len(str(n_binarnie)) % 4
    nstr = ""
    if k != 0:
        for i in range(0,4-k):
            nstr += "0"
    nstr += str(n_binarnie) #nstr liczba postaci 0101 1101

    szesnastkowo = "" #string który składam
    for i in range(0,len(nstr)//4): #przelatuję przez każdy segment
        segment = 0
        power = 3
        for j in range(0,4): #przelatuję przez każdą 0,1 w segmencie
            segment += int(nstr[j+(4*i)]) * 2 ** power
            power -= 1
        szesnastkowo += str(symbole_szesnastkowe[segment]) #suma segmentu jest indexem w symbolach szesnastkowych
    return szesnastkowo

if __name__ == "__main__":
        print(s_szesnastkowy(34215))