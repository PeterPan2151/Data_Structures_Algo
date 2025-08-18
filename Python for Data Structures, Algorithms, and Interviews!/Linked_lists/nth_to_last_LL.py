class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def nth_to_last(nth, node):
    slow = node
    fast = node

    for i in range(nth):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    return slow

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)


a.next = b
b.next = c
c.next = d
d.next = e

print(nth_to_last(2, a))
