# 22. Dana jestlista, który być może zakończona jest cyklem.
# Napisać funkcję, która sprawdza ten fakt.


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

def check_if_cycled(first):
    p = first
    used = []
    while p is not None:
        if p in used:
            return True
        used += [p]
        p = p.next
    return False

def rowerzysta(first): #cycle_a_list -> cyclist -> rowerzysta :D
    p = first
    while p.next is not None:
        p = p.next
    p.next = first
    return first

if __name__ == '__main__':
    first = None
    t=[1,1,1,1,1]
    first = add_elements(t,first)
    first = rowerzysta(first) #lista ma cykl
    print(check_if_cycled(first))