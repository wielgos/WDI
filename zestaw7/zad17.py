# 17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.

class Node:
    def __init__(self, value=None, key=None):
        self.value = value
        self.next = None
        self.prev = None
        self.key = key

def check_key(a):
    ile = 0
    while a != 0:
        if a % 2 == 1:
            ile += 1
        a //= 2
    return True if ile%2==1 else False

def add_elements(t,first):
    for e in t:
        q = Node(e)
        first, q.next, = q, first
        if q.next is not None: q.next.prev = q
    return first

def wypisz(p):
    while p is not None:
        print("",p.value)
        print("↓ ↑")
        p = p.next
    print("==========")

def f(first):
    p = first
    while p is not None:
        if check_key(p.value):
            if p.prev is None:
                first = p.next
                if p.next is not None:
                    p.next.prev = None
            else:
                p.prev.next = p.next
                if p.next is not None:
                    p.next.prev = p.prev
        p = p.next
    return first

if __name__ == '__main__':
    t = [1,2,3,4,5,6,7] #1,10,11,100,101,110,111 (1,2,4,7 out)
    t2 = [1,1,1,1,1,1,1,1]
    first = add_elements(t2,None)
    wypisz(first)
    first = f(first)
    wypisz(first)




