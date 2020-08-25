import unittest
from ll import Node, LinkedList


class TestLinkedListMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        n1 = Node(12)
        n2 = Node(55)
        n3 = Node(12)
        n1.next = n2
        n2.next = n3

        self.linked_list = LinkedList()
        self.linked_list.head = n1
        self.linked_list.tail = n3

        super(TestLinkedListMethods, self).__init__(*args, **kwargs)

    def test_add_in_tail(self):
        NODE_VAL = 128
        self.linked_list.add_in_tail(Node(NODE_VAL))
        node = self.linked_list.tail
        self.assertEqual(node.value, NODE_VAL)

        NODE_VAL = None
        self.linked_list.add_in_tail(Node(NODE_VAL))
        node = self.linked_list.tail
        self.assertEqual(node.value, NODE_VAL)

        NODE_VAL = 'text'
        self.linked_list.add_in_tail(Node(NODE_VAL))
        node = self.linked_list.tail
        self.assertEqual(node.value, NODE_VAL)

        NODE_VAL = ['test', 12]
        self.linked_list.add_in_tail(Node(NODE_VAL))
        node = self.linked_list.tail
        self.assertEqual(node.value, NODE_VAL)

    def test_print_all_nodes(self):
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            self.linked_list.print_all_nodes()

        actual = f.getvalue()
        expected = "12\n55\n12\n"

        self.assertEqual(actual, expected)

    def test_find(self):
        # поиск значения
        NODE_VAL = 12
        node = self.linked_list.find(NODE_VAL)
        self.assertEqual(node.value, NODE_VAL)

        # поиск несуществующего значения
        NODE_VAL = 128
        node = self.linked_list.find(NODE_VAL)
        self.assertIsNone(node)

        # поиск по None
        NODE_VAL = None
        self.linked_list.add_in_tail(Node(NODE_VAL))
        node = self.linked_list.find(NODE_VAL)
        self.assertEqual(node.value, NODE_VAL)

        # поиск по "сложному" типу тданных
        NODE_VAL = ['test', 12]
        self.linked_list.add_in_tail(Node(NODE_VAL))
        node = self.linked_list.find(NODE_VAL)
        self.assertEqual(node.value, NODE_VAL)

        # поиск по нулевому значению
        NODE_VAL = 0
        self.linked_list.add_in_tail(Node(NODE_VAL))
        node = self.linked_list.find(NODE_VAL)
        self.assertEqual(node.value, NODE_VAL)

        # поиск в пустом списке
        linked_list = LinkedList()
        node = linked_list.find(12)
        self.assertIsNone(node)

        # поиск в списке из одного узла
        linked_list.add_in_tail(Node(12))
        node = linked_list.find(12)
        self.assertEqual(node.value, 12)

        node = linked_list.find(10)
        self.assertIsNone(node)

    def test_find_all(self):
        # поиск значения
        NODE_VAL = 12
        nodes = self.linked_list.find_all(NODE_VAL)
        self.assertEqual(len(nodes), 2)
        for node in nodes:
            self.assertEqual(node.value, NODE_VAL)

        # поиск по "сложному" типу тданных
        NODE_VAL = ['test', 12]
        self.linked_list.add_in_tail(Node(NODE_VAL))
        nodes = self.linked_list.find_all(NODE_VAL)
        self.assertEqual(len(nodes), 1)
        for node in nodes:
            self.assertEqual(node.value, NODE_VAL)

        # поиск несуществующего значения
        NODE_VAL = 120
        nodes = self.linked_list.find_all(NODE_VAL)
        self.assertEqual(len(nodes), 0)

        # получение всех узлов списка
        nodes = self.linked_list.find_all()
        self.assertEqual(len(nodes), 4)

        # поиск по None
        NODE_VAL = None
        nodes = self.linked_list.find_all(NODE_VAL)
        self.assertEqual(len(nodes), 4)

        # поиск по нулевому значению
        NODE_VAL = 0
        self.linked_list.add_in_tail(Node(NODE_VAL))
        nodes = self.linked_list.find_all(NODE_VAL)
        self.assertEqual(len(nodes), 1)

        # поиск в пустом списке
        linked_list = LinkedList()
        nodes = linked_list.find_all(12)
        self.assertEqual(len(nodes), 0)

        # поиск в списке из одного узла
        linked_list.add_in_tail(Node(12))
        nodes = linked_list.find_all(12)
        self.assertEqual(len(nodes), 1)
        for node in nodes:
            self.assertEqual(node.value, 12)

        nodes = linked_list.find_all(10)
        self.assertEqual(len(nodes), 0)

    def test_delete(self):
        # удаление первого найденого элемента из нескольких найденых
        NODE_VALUE = 12
        nodes = self.linked_list.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 2)

        self.linked_list.delete(NODE_VALUE)
        nodes = self.linked_list.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(self.linked_list.head.value, 55)
        self.assertEqual(self.linked_list.tail.value, 12)

        # удаление всех найденых элементов
        self.linked_list.add_in_tail(Node(NODE_VALUE))
        nodes = self.linked_list.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 2)

        self.linked_list.delete(NODE_VALUE, True)
        nodes = self.linked_list.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 0)
        self.assertEqual(self.linked_list.tail.value, 55)

        # удаление единственного элемента в списке
        self.linked_list.delete(55)
        self.assertEqual(self.linked_list.len(), 0)
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

        # удаление элемента из пустого списка
        self.assertEqual(self.linked_list.len(), 0)
        self.linked_list.delete(55)
        self.assertEqual(self.linked_list.len(), 0)
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

        # удаление элемента из списка после чего остается только один элемент в списке
        self.linked_list.add_in_tail(Node(NODE_VALUE))
        self.linked_list.add_in_tail(Node(55))

        self.linked_list.delete(55)
        self.assertEqual(self.linked_list.head.value, 12)
        self.assertEqual(self.linked_list.tail.value, 12)
        self.assertIsNone(self.linked_list.head.next)
        self.assertIsNone(self.linked_list.tail.next)
        self.assertEqual(self.linked_list.len(), 1)

        self.linked_list.add_in_tail(Node(55))

        self.linked_list.delete(NODE_VALUE)
        self.assertEqual(self.linked_list.head.value, 55)
        self.assertEqual(self.linked_list.tail.value, 55)
        self.assertIsNone(self.linked_list.head.next)
        self.assertIsNone(self.linked_list.tail.next)
        self.assertEqual(self.linked_list.len(), 1)

        # проверка на удаление элементов со значением 0 и проверка связей для всех узлов в памяти
        n1 = Node(0)
        n2 = Node(0)
        n3 = Node(1)
        n4 = Node(1)
        n5 = Node(2)
        n6 = Node(2)
        linked_list = LinkedList()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        linked_list.add_in_tail(n6)
        linked_list.delete(1, True)
        linked_list.delete(2, True)
        linked_list.delete(0)
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.tail.value, 0)
        self.assertIsNone(linked_list.head.next)
        self.assertIsNone(linked_list.tail.next)
        self.assertEqual(linked_list.len(), 1)

        self.assertIsNone(n1.next)
        self.assertIsNone(n2.next)
        self.assertIsNone(n3.next)
        self.assertIsNone(n4.next)
        self.assertIsNone(n5.next)
        self.assertIsNone(n6.next)

    def test_len(self):
        count_nodes = self.linked_list.len()
        self.assertEqual(count_nodes, 3)

        NODE_VALUE = 12
        self.linked_list.delete(NODE_VALUE, True)
        count_nodes = self.linked_list.len()
        self.assertEqual(count_nodes, 1)

    def test_clean(self):
        self.linked_list.clean()
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)
        self.assertEqual(self.linked_list.len(), 0)

    def test_insert(self):
        # вставка в список со многими элементами в начало списка
        self.linked_list.insert(None, Node(1200))
        self.assertEqual(self.linked_list.head.value, 1200)
        self.assertEqual(self.linked_list.head.next.value, 12)
        self.assertEqual(self.linked_list.len(), 4)
        self.assertEqual(self.linked_list.tail.value, 12)

        # вставка в список со многими элементами
        node = self.linked_list.find(55)
        self.linked_list.insert(node, Node(66))
        self.assertEqual(node.next.value, 66)
        self.assertEqual(self.linked_list.len(), 5)
        self.assertEqual(self.linked_list.head.value, 1200)
        self.assertEqual(self.linked_list.tail.value, 12)

        # вставка в список отличного от Node элемента
        NODE_VALUE = 100
        self.linked_list.insert(node, NODE_VALUE)
        self.assertEqual(self.linked_list.len(), 5)
        self.assertEqual(self.linked_list.head.value, 1200)
        self.assertEqual(self.linked_list.tail.value, 12)

        # вставка в список после несуществующего элемента
        linked_list = LinkedList()
        NODE_VALUE = 100
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(3))
        self.linked_list.insert(Node(1500), NODE_VALUE)
        self.assertEqual(linked_list.len(), 3)
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 3)

        # вставка в пустой список
        linked_list = LinkedList()
        linked_list.insert(None, Node(NODE_VALUE))
        node = linked_list.find(NODE_VALUE)
        self.assertEqual(linked_list.len(), 1)
        self.assertEqual(node.value, NODE_VALUE)
        self.assertEqual(node.next, None)
        self.assertEqual(linked_list.head.value, NODE_VALUE)
        self.assertEqual(linked_list.tail.value, NODE_VALUE)

        # вставка в пустой список после несуществующего элемента
        linked_list = LinkedList()
        linked_list.insert(Node(10), Node(10))
        self.assertEqual(linked_list.len(), 0)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

        # вставка в список с одним элементом и проверка на нулевое значение
        linked_list = LinkedList()
        linked_list.insert(None, Node(0))
        node = linked_list.find(0)
        self.assertEqual(linked_list.len(), 1)
        self.assertEqual(node.value, 0)
        self.assertEqual(node.next, None)
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.tail.value, 0)

    def test_validate_node(self):
        self.assertTrue(self.linked_list._validate_node(Node(123)))
        self.assertFalse(self.linked_list._validate_node(123))
        self.assertFalse(self.linked_list._validate_node('test'))


if __name__ == '__main__':
    unittest.main()
