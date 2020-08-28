class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head

        while node is not None:
            if node.value == val:
                return node
            node = node.next

        return None

    def find_all(self, val=None):
        result = []
        node = self.head

        while node is not None:
            if node.value == val or val is None:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False):
        if not self.head or not self.find(val):
            return

        node = self.head

        while node is not None:
            next_node = node.next

            if node.value == val:
                if node is self.head:
                    self.head = node.next

                    if self.head is None:
                        self.tail = None
                    else:
                        self.head.prev = None

                if node.prev:
                    node.prev.next = node.next

                if node.next:
                    node.next.prev = node.prev

                if node is self.tail:
                    self.tail = node.prev

                node.next = None
                node.prev = None

                if not all:
                    return

            node = next_node

    def insert(self, afterNode, newNode):
        if not self._validate_node(newNode):
            return

        if afterNode is None:
            if self.head is None:
                self.head = newNode
            else:
                newNode.prev = self.tail
                self.tail.next = newNode

            self.tail = newNode

            return

        if not self._validate_node(afterNode):
            return

        if self.find(afterNode.value) is None:
            # Node not found in List
            return

        if afterNode.next is None:
            self.tail = newNode

        newNode.next = afterNode.next
        newNode.prev = afterNode
        afterNode.next = newNode

    def add_in_head(self, newNode):
        if not self._validate_node(newNode):
            return

        if self.head is None:
            self.tail = newNode
        else:
            self.head.prev = newNode

        newNode.next = self.head
        self.head = newNode

        return

    def clean(self):
        nodes = self.find_all()

        for node in nodes:
            node.next = None
            node.prev = None

        self.head = None
        self.tail = None

    def len(self):
        nodes = self.find_all()

        return len(nodes)

    def _validate_node(self, node):
        """Argument must be a Node instance."""
        if not isinstance(node, Node):
            return False
        return True
