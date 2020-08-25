from ll import Node, LinkedList


def sum_linked_lists(first: LinkedList, second: LinkedList):
    if not isinstance(first, LinkedList):
        raise Exception("The first argument must be of the LinkedList type.")

    if not isinstance(second, LinkedList):
        raise Exception("The second argument must be of the LinkedList type.")

    if first.len() != second.len():
        raise Exception("Lists must be the same size.")

    result = LinkedList()
    node1 = first.head
    node2 = second.head
    while node1 is not None:
        if not isinstance(node1.value, int) or not isinstance(node2.value, int):
            del result
            raise Exception("The list should only have numeric values.")

        result.add_in_tail(Node(node1.value + node2.value))
        node1 = node1.next
        node2 = node2.next

    return result
