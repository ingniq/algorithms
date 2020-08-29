class _DummyNode:
    def __init__(self):
        self.prev = None
        self.next = None


class Node():
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class BaseLinkedList2:
    def __init__(self):
        self._head = _DummyNode()
        self._tail = _DummyNode()

        self._head.next = self._tail
        self._tail.prev = self._head


class LinkedList2(BaseLinkedList2):
    def __init__(self):
        super(LinkedList2, self).__init__()

    @property
    def head(self):
        if isinstance(self._head.next, _DummyNode):
            head = None
        else:
            head = self._head.next

        return head

    @property
    def tail(self):
        if isinstance(self._tail.prev, _DummyNode):
            tail = None
        else:
            tail = self._tail.prev

        return tail

    def add_in_tail(self, item):
        item.next = self._tail
        item.prev = self._tail.prev
        self._tail.prev.next = item
        self._tail.prev = item

    def print_all_nodes(self):
        node = self._head.next
        while not isinstance(node, _DummyNode):
            print(node.value)
            node = node.next

    def find(self, val):
        node = self._head.next

        while not isinstance(node, _DummyNode):
            if node.value == val:
                return node
            node = node.next

        return None

    def find_all(self, val=None):
        result = []
        node = self._head.next

        while not isinstance(node, _DummyNode):
            if node.value == val or val is None:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False):
        if isinstance(self._head.next, _DummyNode) or not self.find(val):
            return

        node = self._head.next

        while not isinstance(node, _DummyNode):
            next_node = node.next

            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev

                node.next = None
                node.prev = None

                if not all:
                    return

            node = next_node

    def insert(self, afterNode, newNode):
        if not self._validate_node(newNode):
            return

        if afterNode is not None and not self._validate_node(afterNode):
            return

        if afterNode is not None and self.find(afterNode.value) is None:
            # Node not found in List
            return

        if afterNode is None:
            afterNode = self._tail.prev

        newNode.next = afterNode.next
        newNode.prev = afterNode
        afterNode.next.prev = newNode
        afterNode.next = newNode

    def add_in_head(self, newNode):
        if not self._validate_node(newNode):
            return

        newNode.next = self._head.next
        newNode.prev = self._head
        self._head.next.prev = newNode
        self._head.next = newNode

    def clean(self):
        nodes = self.find_all()

        for node in nodes:
            node.next = None
            node.prev = None

        self._head.next = self._tail
        self._tail.prev = self._head

    def len(self):
        nodes = self.find_all()

        return len(nodes)

    def _validate_node(self, node):
        """Argument must be a Node instance."""
        if not isinstance(node, Node):
            return False
        return True
