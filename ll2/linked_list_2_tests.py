import unittest
from ll import Node, LinkedList2


class TestLinkedList2Methods(unittest.TestCase):
    def test_add_in_tail(self):
        ll = LinkedList2()

        ll.add_in_tail(Node(128))
        self.assertEqual(ll.tail.value, 128)

        ll.add_in_tail(Node(None))
        self.assertEqual(ll.tail.value, None)

        ll.add_in_tail(Node('text'))
        self.assertEqual(ll.tail.value, 'text')

        NODE_VAL = ['test', 12]
        ll.add_in_tail(Node(NODE_VAL))
        self.assertEqual(ll.tail.value, NODE_VAL)

    def test_print_all_nodes(self):
        import io
        from contextlib import redirect_stdout

        ll = LinkedList2()

        ll.add_in_tail(Node(12))
        ll.add_in_tail(Node(55))
        ll.add_in_tail(Node(12))

        f = io.StringIO()
        with redirect_stdout(f):
            ll.print_all_nodes()

        actual = f.getvalue()
        expected = "12\n55\n12\n"

        self.assertEqual(actual, expected)

    def test_find(self):
        ll = LinkedList2()

        ll.add_in_tail(Node(12))
        ll.add_in_tail(Node(55))
        ll.add_in_tail(Node(12))

        # поиск по значению, первое совпадение
        node = ll.find(12)
        self.assertEqual(node.value, 12)
        self.assertEqual(node.next.value, 55)

        # поиск несуществующего значения
        node = ll.find(128)
        self.assertIsNone(node)

        # поиск по None
        ll.add_in_tail(Node(None))
        node = ll.find(None)
        self.assertEqual(node.value, None)

        # поиск по "сложному" типу тданных
        NODE_VAL = ['test', 12]
        ll.add_in_tail(Node(NODE_VAL))
        node = ll.find(NODE_VAL)
        self.assertEqual(node.value, NODE_VAL)

        # поиск по нулевому значению
        ll.add_in_tail(Node(0))
        node = ll.find(0)
        self.assertEqual(node.value, 0)

        # поиск в пустом списке
        ll = LinkedList2()
        node = ll.find(12)
        self.assertIsNone(node)

        # поиск в списке из одного узла
        ll.add_in_tail(Node(12))
        node = ll.find(12)
        self.assertEqual(node.value, 12)

        # поиск в списке из одного узла несуществующего элемента
        node = ll.find(10)
        self.assertIsNone(node)

    def test_find_all(self):
        ll = LinkedList2()

        ll.add_in_tail(Node(12))
        ll.add_in_tail(Node(55))
        ll.add_in_tail(Node(12))

        # поиск значения
        nodes = ll.find_all(12)
        self.assertEqual(len(nodes), 2)

        for node in nodes:
            self.assertEqual(node.value, 12)

        # поиск по "сложному" типу тданных
        NODE_VAL = ['test', 12]
        ll.add_in_tail(Node(NODE_VAL))

        nodes = ll.find_all(NODE_VAL)
        self.assertEqual(len(nodes), 1)

        for node in nodes:
            self.assertEqual(node.value, NODE_VAL)

        # поиск несуществующего значения
        nodes = ll.find_all(120)
        self.assertEqual(len(nodes), 0)

        # получение всех узлов списка
        nodes = ll.find_all()
        self.assertEqual(len(nodes), 4)

        # поиск по None
        nodes = ll.find_all(None)
        self.assertEqual(len(nodes), 4)

        # поиск по нулевому значению
        ll.add_in_tail(Node(0))
        nodes = ll.find_all(0)
        self.assertEqual(len(nodes), 1)

        # поиск в пустом списке
        ll = LinkedList2()
        nodes = ll.find_all(12)
        self.assertEqual(len(nodes), 0)

        # поиск в списке из одного узла
        ll.add_in_tail(Node(12))
        nodes = ll.find_all(12)
        self.assertEqual(len(nodes), 1)

        for node in nodes:
            self.assertEqual(node.value, 12)

        # поиск в списке из одного узла несуществующего элемента
        nodes = ll.find_all(10)
        self.assertEqual(len(nodes), 0)

    def test_delete(self):
        ll = LinkedList2()

        ll.add_in_tail(Node(12))
        ll.add_in_tail(Node(55))
        ll.add_in_tail(Node(12))
        self.assertEqual(ll.len(), 3)

        # удаление первого найденого элемента из нескольких найденых
        NODE_VALUE = 12
        nodes = ll.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 2)

        ll.delete(NODE_VALUE)
        nodes = ll.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(ll.len(), 2)
        self.assertEqual(ll.head.value, 55)
        self.assertEqual(ll.tail.value, 12)

        # удаление всех найденых элементов
        ll.add_in_tail(Node(NODE_VALUE))
        nodes = ll.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 2)

        ll.delete(NODE_VALUE, True)
        nodes = ll.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 0)
        self.assertEqual(ll.len(), 1)
        self.assertEqual(ll.head.value, 55)
        self.assertEqual(ll.tail.value, 55)

        # удаление единственного элемента в списке
        ll.delete(55)
        self.assertEqual(ll.len(), 0)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

        # удаление элемента из пустого списка
        self.assertEqual(ll.len(), 0)
        ll.delete(55)
        self.assertEqual(ll.len(), 0)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

        # удаление элемента из списка
        # после чего остается только один элемент в списке
        ll.add_in_tail(Node(NODE_VALUE))
        ll.add_in_tail(Node(55))
        self.assertEqual(ll.len(), 2)

        ll.delete(55)
        self.assertEqual(ll.head.value, 12)
        self.assertEqual(ll.tail.value, 12)
        self.assertIsNone(ll.head.next)
        self.assertIsNone(ll.tail.next)
        self.assertEqual(ll.len(), 1)

        ll.add_in_tail(Node(55))
        self.assertEqual(ll.len(), 2)

        ll.delete(NODE_VALUE)
        self.assertEqual(ll.head.value, 55)
        self.assertEqual(ll.tail.value, 55)
        self.assertIsNone(ll.head.next)
        self.assertIsNone(ll.tail.next)
        self.assertEqual(ll.len(), 1)

        # проверка на удаление элементов со значением 0
        # и проверка связей для всех узлов в памяти
        n1 = Node(0)
        n2 = Node(0)
        n3 = Node(1)
        n4 = Node(1)
        n5 = Node(2)
        n6 = Node(2)
        ll = LinkedList2()
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)
        ll.add_in_tail(n4)
        ll.add_in_tail(n5)
        ll.add_in_tail(n6)
        self.assertEqual(ll.len(), 6)

        ll.delete(1, True)
        ll.delete(2, True)
        ll.delete(0)

        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.tail.value, 0)
        self.assertIsNone(ll.head.next)
        self.assertIsNone(ll.tail.next)
        self.assertEqual(ll.len(), 1)

        self.assertIsNone(n1.next)
        self.assertIsNone(n2.next)
        self.assertIsNone(n3.next)
        self.assertIsNone(n4.next)
        self.assertIsNone(n5.next)
        self.assertIsNone(n6.next)

        self.assertIsNone(n1.prev)
        self.assertIsNone(n2.prev)
        self.assertIsNone(n3.prev)
        self.assertIsNone(n4.prev)
        self.assertIsNone(n5.prev)
        self.assertIsNone(n6.prev)

    def test_len(self):
        ll = LinkedList2()

        ll.add_in_tail(Node(12))
        ll.add_in_tail(Node(55))
        ll.add_in_tail(Node(12))

        self.assertEqual(ll.len(), 3)

        ll.delete(12, True)
        self.assertEqual(ll.len(), 1)

    def test_clean(self):
        ll = LinkedList2()

        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)

        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)

        ll.clean()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.len(), 0)

        self.assertIsNone(n1.next)
        self.assertIsNone(n2.next)
        self.assertIsNone(n3.next)

        self.assertIsNone(n1.prev)
        self.assertIsNone(n2.prev)
        self.assertIsNone(n3.prev)

    def test_insert(self):
        # вставка в список со многими элементами в конец списка
        ll = LinkedList2()
        ll.add_in_tail(Node(12))
        ll.add_in_tail(Node(55))
        ll.add_in_tail(Node(12))

        ll.insert(None, Node(1200))
        self.assertEqual(ll.head.value, 12)
        self.assertEqual(ll.head.next.value, 55)
        self.assertEqual(ll.len(), 4)
        self.assertEqual(ll.tail.value, 1200)
        self.assertEqual(ll.tail.prev.value, 12)

        # вставка в список со многими элементами
        ll = LinkedList2()
        ll.add_in_tail(Node(12))
        ll.add_in_tail(Node(55))
        ll.add_in_tail(Node(12))

        node = ll.find(55)
        ll.insert(node, Node(66))
        self.assertEqual(node.next.value, 66)
        self.assertEqual(node.next.prev.value, 55)
        self.assertEqual(ll.len(), 4)
        self.assertEqual(ll.head.value, 12)
        self.assertEqual(ll.tail.value, 12)

        # вставка в список отличного от типа Node элемента
        ll.insert(node, 100)
        self.assertEqual(node.next.value, 66)
        self.assertEqual(node.next.prev.value, 55)
        self.assertEqual(ll.len(), 4)
        self.assertEqual(ll.head.value, 12)
        self.assertEqual(ll.tail.value, 12)

        # вставка в список после несуществующего элемента
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.insert(Node(1500), Node(100))
        self.assertEqual(ll.len(), 3)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 3)

        # вставка в пустой список
        ll = LinkedList2()
        ll.insert(None, Node(100))
        node = ll.find(100)
        self.assertEqual(ll.len(), 1)
        self.assertEqual(node.value, 100)
        self.assertEqual(node.next, None)
        self.assertEqual(node.prev, None)
        self.assertEqual(ll.head.value, 100)
        self.assertEqual(ll.tail.value, 100)

        # вставка в пустой список после несуществующего элемента
        ll = LinkedList2()
        ll.insert(Node(10), Node(10))
        self.assertEqual(ll.len(), 0)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

        # вставка в список в конец с одним элементом
        # и проверка на нулевое значение
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        ll.insert(None, Node(0))
        node = ll.find(0)
        self.assertEqual(ll.len(), 2)
        self.assertEqual(node.value, 0)
        self.assertIsNone(node.next)
        self.assertEqual(node.prev.value, 1)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 0)

    def test_add_in_head(self):
        # вставка в список со многими элементами
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))

        ll.add_in_head(Node(1200))
        self.assertEqual(ll.len(), 4)
        self.assertEqual(ll.head.value, 1200)
        self.assertEqual(ll.head.next.value, 1)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.tail.prev.value, 2)

        # вставка в список отличного от типа Node элемента
        ll.add_in_head(1200)
        self.assertEqual(ll.len(), 4)
        self.assertEqual(ll.head.value, 1200)
        self.assertEqual(ll.head.next.value, 1)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.tail.prev.value, 2)

        # вставка в пустой список
        ll = LinkedList2()
        ll.add_in_head(Node(1200))

        self.assertEqual(ll.len(), 1)
        self.assertEqual(ll.head.value, 1200)
        self.assertEqual(ll.tail.value, 1200)
        self.assertIsNone(ll.head.prev)
        self.assertIsNone(ll.head.next)
        self.assertIsNone(ll.tail.prev)
        self.assertIsNone(ll.tail.next)

        # вставка в список с одним элементом и проверка на нулевое значение
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        node = ll.find(1)

        ll.add_in_head(Node(0))
        node = ll.find(0)
        self.assertEqual(ll.len(), 2)
        self.assertEqual(node.value, 0)
        self.assertEqual(node.next.value, 1)
        self.assertEqual(node.next.prev.value, 0)
        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.tail.value, 1)

    def test_validate_node(self):
        ll = LinkedList2()

        self.assertTrue(ll._validate_node(Node(123)))
        self.assertFalse(ll._validate_node(123))
        self.assertFalse(ll._validate_node('test'))


if __name__ == '__main__':
    unittest.main()
