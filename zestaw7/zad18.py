# 18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
# unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.

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
    prev = None
    p = first
    unique = []
    while p is not None:
        if p.value in unique:
            if prev is None:
                first = p.next
                prev, p = None, p.next
            else:
                prev.next = p.next
                p = p.next
        else:
            unique += [p.value]
            prev, p = p, p.next
    return first

if __name__ == '__main__':
    t=[2,2,3,3,4,4,4,4,4,5,6,7,8,8,8]
    first = add_elements(t,None)
    wypisz(first)
    first = f(first)
    wypisz(first)