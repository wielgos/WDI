# 32. Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w
# liście ułożone są według rosnących potęg. Proszę napisać funkcję
# obliczającą różnicę dwóch dowolnych wielomianów. Wielomiany reprezentowane
# są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo
# utworzonej listy reprezentującej wielomian wynikowy. Listy wejściowe
# powinny pozostać niezmienione.


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def add_elements(t, first):
    for i in range(len(t) - 1, -1, -1):
        q = Node(t[i])
        first, q.next = q, first
    return first


def wypisz(p):
    while p is not None:
        print(p.value)
        print("↓")
        p = p.next
    print("==========")


def main(first1, first2):
    p = first1
    q = first2
    if p and q is not None:
        first3 = x = Node(p.value - q.value)
        p, q = p.next, q.next
    elif p is None:
        first3 = x = Node(-q.value)
        q = q.next
    else:
        first3 = x = Node(p.value)
        p = p.next
    while p is not None or q is not None:
        if p is not None and q is not None:
            x.next = Node(p.value - q.value)
            p, q = p.next, q.next
        elif p is None:
            x.next = Node(-q.value)
            q = q.next
        else:
            x.next = Node(p.value)
            p = p.next
        x = x.next
    return first3


if __name__ == '__main__':
    first1 = None
    first2 = None
    # t1=[10,9,7,5,4,4,3,2]
    # t2=[10,9,8,6,6,6,4,1]
    t1 = [1, 2, 3, 4]
    t2 = [0, 0, 0, 0, 0, 0, 6]
    first1 = add_elements(t1, first1)
    first2 = add_elements(t2, first2)
    first3 = main(first1, first2)
    wypisz(first3)
