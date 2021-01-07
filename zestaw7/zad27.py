# 27. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.



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

def skaluj(first1,first2):
    if first1 is None: return first2
    if first2 is None: return first1
    if first1.value >= first2.value:
        q,p = first1,first2
    else:
        p,q = first1,first2
    first3 = Node(p.value)
    x = first3
    p = p.next
    while p is not None or q is not None:
        while (p is None and q is not None) or (q is not None and q.value <= p.value):
            x.next = Node(q.value)
            x = x.next
            q = q.next #dodaję q.value i przesuwam q
        if p is not None:
            x.next = Node(p.value)
            x = x.next
            p = p.next #dodaję p.value i przesuwam p
    return first3


if __name__ == '__main__':
    first1 = None
    first2 = None
    # t1=[10,9,7,5,4,4,3,2]
    # t2=[10,9,8,6,6,6,4,1]
    t1 = [5,4,3,2,1]
    t2 = [17,5,5,5,5,5,5,5,1]
    first1 = add_elements(t1,first1)
    first2 = add_elements(t2,first2)
    first3 = skaluj(first1,first2)
    wypisz(first3)
