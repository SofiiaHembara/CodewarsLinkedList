class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    parts = s.split(' -> ')
    head = None
    probe = None
    for part in reversed(parts):
        if part == 'None':
            continue
        if head is None:
            head = Node(int(part))
            probe = head
        else:
            new_node = Node(int(part))
            new_node.next = probe
            probe = new_node
    return probe

print(linked_list_from_string('0 -> 1 -> 4 -> 9 -> 16 -> None'))