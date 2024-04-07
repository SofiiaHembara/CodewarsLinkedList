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
