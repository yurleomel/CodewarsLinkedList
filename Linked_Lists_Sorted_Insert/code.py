from preloaded import Node

""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    new_node = Node(data)
    if not head:
        return new_node
    if data <= head.data:
        new_node.next = head
        head = new_node
        return head
    current = head
    while current.next:
        if current.next.data >= data:
            new_node.next = current.next
            current.next = new_node
            return head
        current = current.next

    current.next = new_node
    return head
