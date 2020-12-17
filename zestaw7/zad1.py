# 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
# struktury listy odsyłaczowej.
# - czy element należy do zbioru
# - wstawienie elementu do zbioru
# - usunięcie elementu ze zbioru

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


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


def wstaw(first, element):
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


def wypisz(p):
    while p is not None:
        print(p.value, end=" ")
        p = p.next
    print()


if __name__ == '__main__':
    first = None
    while True:
        num = input(">")
        if num == "x": break
        first = wstaw(first, int(num))
    first = usun(first, 5)
    first = usun(first, 6)
    first = usun(first, 7)
    first = usun(first, 8)
    wypisz(first)
