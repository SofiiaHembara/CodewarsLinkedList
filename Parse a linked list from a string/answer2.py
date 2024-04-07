class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    
    parts = s.split(" -> ")
    if parts[-1] == "None":
        parts.pop()

    if not parts:
        return None

    head = Node(int(parts[0]))
    current = head
    for value in parts[1:]:
        new_node = Node(int(value))
        current.next = new_node
        current = new_node
    return head