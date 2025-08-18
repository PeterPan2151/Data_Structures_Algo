class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def cycle_check(node):
    slow = node
    fast = node

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next 

        if slow == fast:
            return True
    
    return False


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

print(cycle_check(a))
