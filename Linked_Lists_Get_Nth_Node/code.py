from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    i = 0

    while node:
        if index == i:
            return node

        node = node.next
        i += 1

    raise Exception("Index out of range")
