class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise Exception("Source list is empty")

    start = source
    source = source.next
    start.next = dest
    dest = start
    return Context(source, dest)