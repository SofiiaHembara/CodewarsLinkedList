class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None

    dummy = Node(0)
    dummy.next = head
    
    current = head
    
    while current and current.next:
        if current.data == current.next.data:
            while current.next and current.data == current.next.data:
                current.next = current.next.next
        else:
            current = current.next

    return dummy.next
