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


class BaseOrderedList:
    GREATER = 1
    LESS = -1
    EQUAL = 0

    def __init__(self):
        self._head = _DummyNode()
        self._tail = _DummyNode()

        self._head._next = self._tail
        self._tail._prev = self._head


class OrderedList(BaseOrderedList):
    def __init__(self, asc):
        self.__ascending = asc
        super(OrderedList, self).__init__()

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

    def compare(self, v1, v2):
        if not isinstance(v1, (int, float)):
            return None

        if not isinstance(v2, (int, float)):
            return None

        if v1 < v2:
            return self.LESS
        elif v1 > v2:
            return self.GREATER
        else:
            return self.EQUAL

    def add(self, value):
        in_head = False

        if self.head is None:
            in_head = True
        elif self.__ascending and self.compare(value, self.head.value) in [self.LESS, self.EQUAL]:
            in_head = True
        elif not self.__ascending and self.compare(value, self.head.value) in [self.GREATER, self.EQUAL]:
            in_head = True
            
        newNode = Node(value)
        # insert in the head or in an empty list
        if in_head:
            newNode._prev = self._head
            newNode._next = self._head._next
            self._head._next._prev = newNode
            self._head._next = newNode
            return
        
        del in_head

        in_tail = False

        if self.__ascending and self.compare(value, self.tail.value) in [self.GREATER, self.EQUAL]:
            in_tail = True
        elif not self.__ascending and self.compare(value, self.tail.value) in [self.LESS, self.EQUAL]:
            in_tail = True

        # insert in the tail
        if in_tail:
            newNode._next = self.tail._next
            newNode._prev = self.tail
            self.tail._next = newNode
            self._tail._prev = newNode
            return
        
        del in_tail

        if self.__ascending:
            find_condition = self.GREATER
        else:
            find_condition = self.LESS

        node = self.head
        while node is not None and self.compare(value, node.value) == find_condition:
            node = node.next

        newNode._next = node
        newNode._prev = node._prev
        node._prev._next = newNode
        node._prev = newNode

        return

    def print_all_nodes(self):
        node = self.head
        while isinstance(node, Node):
            print(node.value)
            node = node.next

    # O(n)
    def find(self, val):
        # list is empty
        if self.head is None:
            return None

        # one item in list
        if self.head == self.tail:
            if val == self.head.value:
                return self.head
            return None

        if self.__ascending:
            find_condition = [self.GREATER, self.EQUAL]
        else:
            find_condition = [self.LESS, self.EQUAL]

        node = self.head
        while node is not None and self.compare(val, node.value) in find_condition:
            if val == node.value:
                return node
            node = node.next

        return None

    # O(n)
    def get_all(self):
        r = []
        node = self._head._next

        while isinstance(node, Node):
            r.append(node)
            node = node.next
        return r

    # O(n)
    def find_all(self, val):
        r = []
        # list is empty
        if self.head is None:
            return r

        # one item in list
        if self.head == self.tail:
            if val == self.head.value:
                r.append(self.head)
            return r

        if self.__ascending:
            find_condition = [self.GREATER, self.EQUAL]
        else:
            find_condition = [self.LESS, self.EQUAL]

        node = self.head
        while node is not None and self.compare(val, node.value) in find_condition:
            if val == node.value:
                r.append(node)
            node = node.next

        return r

    def delete(self, val, all=False):
        if not isinstance(self._head._next, Node):
            return

        nodes = self.find_all(val)

        if len(nodes) == 0:
            return

        node = self._head._next

        for node in nodes:
            node._prev._next = node._next
            node._next._prev = node._prev

            node._next = None
            node._prev = None

            if not all:
                return

    def clean(self, asc):
        nodes = self.get_all()

        for node in nodes:
            node._next = None
            node._prev = None

        self._head._next = self._tail
        self._tail._prev = self._head
        self.__ascending = asc

    # O(n)
    def len(self):
        nodes = self.get_all()

        return len(nodes)

    def _validate_node(self, node):
        """Argument must be a Node instance."""
        if not isinstance(node, Node):
            return False
        return True


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str):
        if not isinstance(v1, str):
            return None

        if not isinstance(v2, str):
            return None

        v1 = v1.strip()
        v2 = v2.strip()

        if v1 < v2:
            return self.LESS
        elif v1 > v2:
            return self.GREATER
        else:
            return self.EQUAL
