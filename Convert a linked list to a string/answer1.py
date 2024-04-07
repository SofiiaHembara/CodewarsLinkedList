class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    if node is None:
        return 'None'
    
    result = ''
    while node is not None:
        if node.next:
            result += f'{node.data} -> '
        else:
            result += f'{node.data} -> None'
        node = node.next
    return result

print(stringify(Node(0, Node(1, Node(2, Node(3))))))
print(stringify(None))
print(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))))