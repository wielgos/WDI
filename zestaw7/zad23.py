# 23. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów w cyklu.


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

def rowerzysta(first): #cycle_a_list -> cyclist -> rowerzysta :D
    p = first
    while p.next is not None:
        p = p.next
    p.next = first
    return first

def cycle_size(first):
    p = first
    prev = None
    used = []
    while p is not None:
        if p not in used:
            used += [p]
        else:
            break
        prev, p  = p, p.next
    c = 1
    while p != prev:
        p = p.next
        c += 1
    return c


if __name__ == '__main__':
    first = None
    t=[1,2,3,4,5]
    first = add_elements(t,first)
    first = rowerzysta(first) #lista ma cykl
    first = add_elements(t, first)
    print(cycle_size(first))