class Node:
    def __init__(self):
        self.value = None
        self.next = None


def wstaw(first, element):
    if czy_nalezy(first,element):
        return first
    if first is None:
        first = Node()
        first.value = element
        first.next = None
        return first
    p = Node()
    p.value = element
    p.next = first
    first = p
    return first


def czy_nalezy(first, element):
    if first is None: return False
    q = first
    if q.value == element:
        return True
    while q.next is not None:
        q = q.next
        if q.value == element:
            return True
    return False


def wypisz(first):
    if first is None: return first
    q = first
    while True:
        print(q.value, end=" ")
        if q.next is not None:
            q = q.next
        else:
            break
    print()
    return


def usun(first, element):
    if first is None: return first
    q = first
    if q.value == element:
        return q.next
    while True:
        if q.next is not None:
            if q.next.next is None and q.next.value == element:
                q.next = None
                return first
            if q.next.value == element:
                q.next = q.next.next
                return first
            q = q.next
        else:
            break
    return first


if __name__ == '__main__':
    first = None
    while True:
        num = input(">")
        if num == "x": break
        first = wstaw(first,int(num))
    wypisz(first)
