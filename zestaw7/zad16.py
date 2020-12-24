# 16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, przenosi na początek listy te z nich,
# które mają parzystą ilość piątek w zapisie ósemkowym.

class Node:
    def __init__(self, value=None, key=None):
        self.value = value
        self.next = None
        self.key = key

def check(n):
    fives = 0
    while n!=0:
        r = n%8
        if n%8==5: fives += 1
        n = (n-r)//8
    return True if fives%2==0 else False

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
    while p is not None:
        if check(p.value) and prev is not None:
            prev.next = p.next
            p.next = first
            first = p
            p = prev.next
        else: prev, p = p, p.next
    return first

if __name__ == '__main__':
    t = [2,5,1,5,5,5]
    first = add_elements(t,None)
    wypisz(first)
    first = f(first)
    wypisz(first)




