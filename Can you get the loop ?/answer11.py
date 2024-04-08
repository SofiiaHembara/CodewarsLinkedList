def loop_size(node):
    if not node:
        return 0
    
    slow = fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            loop_size = 1
            fast = fast.next

            while slow != fast:
                fast = fast.next
                loop_size += 1

            return loop_size
    return 0