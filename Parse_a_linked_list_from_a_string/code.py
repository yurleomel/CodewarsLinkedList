from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    res = ""
    skip = False
    head = None
    current = None

    for let in list_repr:
        if skip:
            skip = False
            continue
        if let.isdigit():
            res += let
        elif let == "-":
            res = res.strip()
            if res.isdigit():
                res = int(res)
            node = Node(res)
            if head is None:
                head = node
                current = node
            else:
                current.next = node
                current = node
            res = ""
            skip = True
    return head
