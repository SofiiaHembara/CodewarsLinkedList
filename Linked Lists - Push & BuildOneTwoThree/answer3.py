class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head

print(push(None, 1).data)
print(push(None, 1).next)
print(push(Node(1), 2).data)
print(push(Node(1), 2).next.data)