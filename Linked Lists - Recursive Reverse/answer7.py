class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def reverse(head):
    def recursive_reverse(current, prev=None):
        if not current:
            return prev
        next_node = current.next
        current.next = prev
        return recursive_reverse(next_node, current)
    return recursive_reverse(head)


