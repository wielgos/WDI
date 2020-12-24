# 20. Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
# Krańce przedziałów określa uporządkowana para liczb całkowitych. Proszę
# napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
# Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
# powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def add_elements(t,first):
    for e in t:
        q = Node(e)
        first, q.next = q, first
    return first

def wypisz(p):
    while p is not None:
        print(p.value)
        print("↓")
        p = p.next
    print("==========")

def f(first):
    p = first
    przedzialy = []
    while p is not None:
        modified = False
        for e in przedzialy:
            if e[0]<=p.value[0]<=e[1] or e[0]<=p.value[1]<=e[1]:
                modified = True
                if p.value[0]<=e[0]:
                    e[0] = p.value[0]
                if p.value[1]>=e[1]:
                    e[1] = p.value[1]
                break
            if p.value[0]<=e[0]<=p.value[1] or p.value[0]<=e[1]<=p.value[1]:
                modified = True
                if p.value[0]<=e[0]:
                    e[0] = p.value[0]
                if p.value[1]>=e[1]:
                    e[1] = p.value[1]
                break
        if modified == False:
            print("adding...", p.value)
            przedzialy += [p.value]
        p = p.next

    first2 = None
    for e in przedzialy:
        q = Node(e)
        first2, q.next = q, first2
    return first2

if __name__ == '__main__':
    t=[[15,19],[2,5],[7,11],[8,12],[5,6],[13,17]]
    t2=[[3,9],[5,7],[11,14]]
    first = add_elements(t2,None)
    first2 = f(first)
    wypisz(first2)