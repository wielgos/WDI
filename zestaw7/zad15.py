# 15. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.

class Node:
    def __init__(self, value=None, key=None):
        self.value = value
        self.next = None
        self.key = key

def check_key(n): #true = nalezy go usunac
    ones = 0
    twos = 0
    while n!=0:
        r = n%3
        if n%3==2: twos += 1
        elif n%3==1: ones += 1
        n = (n-r)//3
    return True if ones>twos else False

def base_3(n):
    res = []
    while n!=0:
        res += [n%3]
        n = (n-n%3)//3
    return res[::-1]

def add_elements(t,first):
    for e in t:
        q = Node(e[0],e[1])
        first, q.next = q, first
    return first

def wypisz(p):
    while p is not None:
        print("v:",p.value,"k(3):",base_3(p.key))
        print("    ↓    ")
        p = p.next
    print("==========")

def main(first):
    prev = None
    p = first
    while p is not None:
        if check_key(p.key):
            if prev is None:
                first = p.next
                prev, p = None, p.next
            else:
                prev.next = p.next
                p = p.next
        else:
            prev, p = p, p.next
    return first


if __name__ == '__main__':
    # 23(10) - 212(3)
    # 471(10) - 122110(3)
    # 213(10) - 21220(3)
    first = None
    t1=[[2,23],[3,479],[3,471]] #pierwszy nalezy usunac
    t2= [[5,471],[2,23],[3,23]] #ostatni nalezy usunac
    t3= [[4,471],[3,471],[2,471],[1,471],[7,471],[8,471],[9,471],[10,471],[11,471]] #wszystkie
    first = add_elements(t3,first)
    wypisz(first)
    first = main(first)
    wypisz(first)


