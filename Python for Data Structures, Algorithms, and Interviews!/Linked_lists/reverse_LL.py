class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(node):
    temp = node
    before = None
    after = temp.next

    while temp:
        after = temp.next
        temp.next = before
        before = temp
        temp = after
    return before

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

reverse(a)

print(c.next.value)
print(b.next.value)


