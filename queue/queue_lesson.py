class Queue:
    def __init__(self):
        # инициализация хранилища данных
        self.queue = LinkedList2()

    def enqueue(self, item):
        """Четыре операции сложностью O(1) (искл. создание экземпляра Node)."""
        # вставка в хвост.
        self.queue.add_in_tail(Node(item))

    def dequeue(self):
        """Шесть операций сложностью O(1). Седьмая - возврат значения."""
        # выдача из головы
        node = self.queue.head

        if node is not None:
            node._prev._next = node._next
            node._next._prev = node._prev
            node._next = None
            node._prev = None

            return node.value

        return None  # если очередь пустая

    def size(self):
        return len(self.queue)


class _DummyNode:
    def __init__(self):
        self._prev = None
        self._next = None

    @property
    def prev(self):
        return None

    @property
    def next(self):
        return None


class Node(_DummyNode):
    def __init__(self, v):
        self.value = v
        super(Node, self).__init__()

    @property
    def prev(self):
        if isinstance(self._prev, Node):
            return self._prev

        return None

    @property
    def next(self):
        if isinstance(self._next, Node):
            return self._next

        return None


class BaseLinkedList2:
    def __init__(self):
        self._head = _DummyNode()
        self._tail = _DummyNode()

        self._head._next = self._tail
        self._tail._prev = self._head


class LinkedList2(BaseLinkedList2):
    def __init__(self):
        super(LinkedList2, self).__init__()

    @property
    def head(self):
        if isinstance(self._head._next, Node):
            head = self._head._next
        else:
            head = None

        return head

    @property
    def tail(self):
        if isinstance(self._tail._prev, Node):
            tail = self._tail._prev
        else:
            tail = None

        return tail

    def __len__(self):
        return self.len()

    def add_in_tail(self, item):
        item._next = self._tail
        item._prev = self._tail._prev
        self._tail._prev._next = item
        self._tail._prev = item

    def print_all_nodes(self):
        node = self._head._next
        while isinstance(node, Node):
            print(node.value)
            node = node._next

    def find(self, val):
        node = self._head._next

        while isinstance(node, Node):
            if node.value == val:
                return node
            node = node._next

        return None

    def find_all(self, val=None):
        result = []
        node = self._head._next

        while isinstance(node, Node):
            if node.value == val or val is None:
                result.append(node)
            node = node._next

        return result

    def delete(self, val, all=False):
        if not isinstance(self._head._next, Node) or not self.find(val):
            return

        node = self._head._next

        while isinstance(node, Node):
            next_node = node._next

            if node.value == val:
                node._prev._next = node._next
                node._next._prev = node._prev

                node._next = None
                node._prev = None

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
            afterNode = self._tail._prev

        newNode._next = afterNode._next
        newNode._prev = afterNode
        afterNode._next._prev = newNode
        afterNode._next = newNode

    def add_in_head(self, newNode):
        if not self._validate_node(newNode):
            return

        newNode._next = self._head._next
        newNode._prev = self._head
        self._head._next._prev = newNode
        self._head._next = newNode

    def clean(self):
        nodes = self.find_all()

        for node in nodes:
            node._next = None
            node._prev = None

        self._head._next = self._tail
        self._tail._prev = self._head

    def len(self):
        nodes = self.find_all()

        return len(nodes)

    def _validate_node(self, node):
        """Argument must be a Node instance."""
        if not isinstance(node, Node):
            return False
        return True
