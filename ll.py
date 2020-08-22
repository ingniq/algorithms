class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        # В памяти хранятся узлы (Node). У узлов есть ссылка на другой узел или None.
        # В классе хранятся ссылки только на первый и последний узлы в памяти.
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if not self._validate_node(item):
            return

        if self.head is None:
            self.head = item
        else:
            # Если в свойстве tail хранится указатель на последний узел списка в памяти (который связан с None),
            # то связываем этот узел с узлом item вместо None
            self.tail.next = item
        # И в свойстве tail меняем указатель на узел item - так как теперь он является последним в списке.
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
        node = self.head

        if not val or not node or not self.find(val):
            pass

        if node.value == val:
            self.head = node.next
            if not all:
                return

        before_node = None
        while node is not None:
            after_node = node.next

            if node.value == val:
                if before_node:
                    before_node.next = after_node
                node.next = None
                if not all:
                    return
            else:
                before_node = node

            node = after_node

    def clean(self):
        nodes = self.find_all()
        for node in nodes:
            node.next = None

        self.head = None
        self.tail = None


    def len(self):
        nodes = self.find_all()

        return len(nodes)

    def insert(self, afterNode, newNode):
        if not self._validate_node(newNode):
            return

        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            return

        if not self._validate_node(afterNode):
            return

        if self.find(afterNode.value) is None:
            # Node not found in List
            return

        newNode.next = afterNode.next
        afterNode.next = newNode

    def _validate_node(self, node):
        """Argument must be a Node instance."""
        if not isinstance(node, Node):
            return False
        return True
