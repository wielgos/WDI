class LL:
    def __init__(self):
        self.first = None

class Node:
    def __init__(self):
        self.value = None
        self.next = None


def print_values(first):
    q = first
    while q != None:
        print(q.value, end=" ")
        q = q.next
    print()
    return


def add_values(first):
    print("type x to stop")
    while True:
        i = input(">")
        if i == "x":
            break
        else:
            p = Node()
            p.next = first
            p.value = int(i)
            first = p
    return first


def remove_last(first):
    if first == None:
        return first
    q = first
    if q.next == None:
        first = None
        return first
    while q.next.next != None:
        q = q.next
    q.next = None
    return first


if __name__ == '__main__':
    lista = LL()
    first = lista.first
    first = remove_last(first)
    print_values(first)
    first = add_values(first)