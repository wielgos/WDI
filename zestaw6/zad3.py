# Zadanie 3. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi
# zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
# k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
# koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
# polu startowym i ostatnim także wliczamy do kosztu przejścia.

def rek(T,coins,posw,posk):
     global finalcosts
     if posw == 7:
          if coins not in finalcosts:
               finalcosts += [coins]
          return
     if posk<len(T)-1:
          rek(T,coins + T[posw+1][posk+1],posw+1,posk+1)
     if posk>0:
          rek(T, coins + T[posw + 1][posk - 1], posw + 1, posk - 1)
     rek(T, coins + T[posw + 1][posk], posw + 1, posk)

def funkcja(T,k):
     rek(T,T[0][k],0,k)
     for i in range(len(finalcosts)-1):
          mincoins = min(finalcosts[i],finalcosts[i+1])
     return mincoins

global finalcosts
finalcosts = []

T = [[5,5,5,5,1,5,5,5],
     [5,5,5,1,5,5,5,5],
     [5,5,1,5,5,5,5,5],
     [5,5,5,1,5,5,5,5],
     [5,5,5,5,1,5,5,5],
     [5,5,5,5,5,2,5,5],
     [5,5,5,5,5,5,1,5],
     [5,5,5,5,5,5,5,1]]

print(funkcja(T,4))