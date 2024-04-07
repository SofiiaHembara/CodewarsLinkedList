class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    probe = node
    count = 0
    while probe:
        if count == index:
            return probe
        count += 1
        probe = probe.next
    raise IndexError("Index out of bounds")


linked_list = Node(1, Node(2, Node(3, None)))


print(get_nth(linked_list, 0).data)
print(get_nth(linked_list, 1).data)
print(get_nth(linked_list, 2).data)