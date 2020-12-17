class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

def wstaw(first,element):
    prev = None
    p = first
    while p is not None and p.value < element:
        prev = p
        p = p.next
    if p is not None and p.value == element: return first

    q = Node(element)

    if prev is None:
        q.next = p
        return q

    prev.next = q
    q.next = p
    return first


def czy_nalezy(first, element):
    p = first
    while p is not None:
        if p.value == element:
            return True
        p = p.next
    return False


def usun(first, element):
    p = first
    prev = None
    if p is not None and p.value == element:
        return p.next
    while p is not None:
        if element == p.value:
            prev.next = p.next
            return first
        prev = p
        p = p.next
    return first


def wypisz(q):
    while q is not None:
        print(q.value, end=" ")
        q = q.next
    print()


if __name__ == '__main__':
    first = None
    while True:
        num = input(">")
        if num == "x": break
        first = wstaw(first, int(num))
    print(czy_nalezy(first,7))
    first = usun(first,7)
    print(czy_nalezy(first, 7))
    first = usun(first, 6)
    print(czy_nalezy(first, 10))
    wypisz(first)
