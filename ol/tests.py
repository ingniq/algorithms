import unittest
from ol import Node, OrderedList, OrderedStringList


class TestOrderedListMethods(unittest.TestCase):
    def test_add(self):
        ol = OrderedList(True)

        ol.add(128)
        self.assertEqual(ol.head.value, 128)
        self.assertEqual(ol.tail.value, 128)

        ol.add(10)
        self.assertEqual(ol.head.value, 10)
        self.assertEqual(ol.head.next.value, 128)
        self.assertEqual(ol.tail.prev.value, 10)
        self.assertEqual(ol.tail.value, 128)

        ol.add(1)
        self.assertEqual(ol.head.value, 1)
        self.assertEqual(ol.head.next.value, 10)
        self.assertEqual(ol.tail.value, 128)

        ol.add(130)
        self.assertEqual(ol.head.value, 1)
        self.assertEqual(ol.tail.prev.value, 128)
        self.assertEqual(ol.tail.value, 130)

        ol.add(0)
        self.assertEqual(ol.head.value, 0)
        self.assertEqual(ol.head.next.value, 1)
        self.assertEqual(ol.tail.value, 130)

        ol.add(-1)
        self.assertEqual(ol.head.value, -1)
        self.assertEqual(ol.head.next.value, 0)
        self.assertEqual(ol.tail.value, 130)

        ol = OrderedList(False)
        ol.add(128)
        self.assertEqual(ol.head.value, 128)
        self.assertEqual(ol.tail.value, 128)

        ol.add(10)
        self.assertEqual(ol.head.value, 128)
        self.assertEqual(ol.head.next.value, 10)
        self.assertEqual(ol.tail.prev.value, 128)
        self.assertEqual(ol.tail.value, 10)

        ol.add(1)
        self.assertEqual(ol.head.value, 128)
        self.assertEqual(ol.head.next.value, 10)
        self.assertEqual(ol.tail.prev.value, 10)
        self.assertEqual(ol.tail.value, 1)

        ol.add(130)
        self.assertEqual(ol.head.value, 130)
        self.assertEqual(ol.head.next.value, 128)
        self.assertEqual(ol.head.next.next.value, 10)
        self.assertEqual(ol.tail.value, 1)

        ol.add(0)
        self.assertEqual(ol.head.value, 130)
        self.assertEqual(ol.tail.prev.value, 1)
        self.assertEqual(ol.tail.value, 0)

        ol.add(-1)
        self.assertEqual(ol.head.value, 130)
        self.assertEqual(ol.tail.prev.value, 0)
        self.assertEqual(ol.tail.value, -1)

        ol.add(55)
        self.assertEqual(ol.head.value, 130)
        self.assertEqual(ol.head.next.value, 128)
        self.assertEqual(ol.head.next.next.value, 55)
        self.assertEqual(ol.tail.prev.value, 0)
        self.assertEqual(ol.tail.value, -1)
        ol.add(33)
        self.assertEqual(ol.head.value, 130)
        self.assertEqual(ol.head.next.value, 128)
        self.assertEqual(ol.head.next.next.value, 55)
        self.assertEqual(ol.head.next.next.next.value, 33)
        self.assertEqual(ol.tail.prev.value, 0)
        self.assertEqual(ol.tail.value, -1)

    def test_compare(self):
        ol = OrderedList(True)
        self.assertEqual(ol.compare(1, 2), -1)
        self.assertEqual(ol.compare(2, 2), 0)
        self.assertEqual(ol.compare(3, 2), 1)
        self.assertEqual(ol.compare(3, -1), 1)
        self.assertEqual(ol.compare(3, 0), 1)
        self.assertEqual(ol.compare(0, 0), 0)
        self.assertEqual(ol.compare(-1, 0), -1)
        self.assertEqual(ol.compare(-1, -1), 0)
        self.assertEqual(ol.compare(0, -1), 1)
        self.assertEqual(ol.compare(0.1, 0.05), 1)

    def test_print_all_nodes(self):
        import io
        from contextlib import redirect_stdout

        ol = OrderedList(True)
        ol.add(12)
        ol.add(55)
        ol.add(12)
        ol.add(1)

        f = io.StringIO()
        with redirect_stdout(f):
            ol.print_all_nodes()

        actual = f.getvalue()
        expected = "1\n12\n12\n55\n"
        self.assertEqual(actual, expected)

        ol = OrderedList(False)
        ol.add(12)
        ol.add(55)
        ol.add(12)
        ol.add(1)

        f = io.StringIO()
        with redirect_stdout(f):
            ol.print_all_nodes()

        actual = f.getvalue()
        expected = "55\n12\n12\n1\n"
        self.assertEqual(actual, expected)

    def test_find(self):
        # asc
        ol = OrderedList(True)

        ol.add(1)
        ol.add(1)
        ol.add(33)
        ol.add(55)
        ol.add(33)

        # поиск по значению, первое совпадение
        node = ol.find(1)
        self.assertEqual(node.value, 1)
        self.assertEqual(node.next.value, 1)

        # поиск по значению, первое совпадение
        node = ol.find(33)
        self.assertEqual(node.value, 33)
        self.assertEqual(node.next.value, 33)
        self.assertEqual(node.prev.value, 1)

        # поиск несуществующего значения
        node = ol.find(128)
        self.assertIsNone(node)

        # поиск по нулевому значению
        ol.add(0)
        node = ol.find(0)
        self.assertEqual(node.value, 0)

        # поиск в пустом списке
        ol = OrderedList(True)
        node = ol.find(12)
        self.assertIsNone(node)

        # поиск в списке из одного узла
        ol.add(12)
        node = ol.find(12)
        self.assertEqual(node.value, 12)

        # поиск в списке из одного узла несуществующего элемента
        node = ol.find(10)
        self.assertIsNone(node)

        # desc
        ol = OrderedList(False)

        ol.add(1)
        ol.add(1)
        ol.add(33)
        ol.add(55)
        ol.add(33)

        node = ol.find(55)
        self.assertEqual(node.value, 55)
        self.assertEqual(node.next.value, 33)

        # поиск по значению, первое совпадение
        node = ol.find(1)
        self.assertEqual(node.value, 1)
        self.assertEqual(node.next.value, 1)
        self.assertEqual(node.prev.value, 33)

        # поиск по значению, первое совпадение
        ol.print_all_nodes()
        node = ol.find(33)
        self.assertEqual(node.value, 33)
        self.assertEqual(node.next.value, 33)
        self.assertEqual(node.prev.value, 55)

    def test_find_all(self):
        ol = OrderedList(True)

        ol.add(12)
        ol.add(55)
        ol.add(12)

        # поиск значения
        nodes = ol.find_all(12)
        self.assertEqual(len(nodes), 2)

        for node in nodes:
            self.assertEqual(node.value, 12)

        # поиск несуществующего значения
        nodes = ol.find_all(120)
        self.assertEqual(len(nodes), 0)

        # поиск по нулевому значению
        ol.add(0)
        nodes = ol.find_all(0)
        self.assertEqual(len(nodes), 1)

        # поиск в пустом списке
        ol = OrderedList(True)
        nodes = ol.find_all(12)
        self.assertEqual(len(nodes), 0)

        # поиск в списке из одного узла
        ol.add(12)
        nodes = ol.find_all(12)
        self.assertEqual(len(nodes), 1)

        for node in nodes:
            self.assertEqual(node.value, 12)

        # поиск в списке из одного узла несуществующего элемента
        nodes = ol.find_all(10)
        self.assertEqual(len(nodes), 0)

    def test_delete(self):
        ol = OrderedList(True)

        ol.add(12)
        ol.add(55)
        ol.add(12)
        self.assertEqual(ol.len(), 3)

        # удаление первого найденого элемента из нескольких найденных
        NODE_VALUE = 12
        nodes = ol.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 2)

        ol.delete(NODE_VALUE)
        nodes = ol.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(ol.len(), 2)
        self.assertEqual(ol.head.value, 12)
        self.assertEqual(ol.tail.value, 55)

        # удаление всех найденных элементов
        ol.add(NODE_VALUE)
        nodes = ol.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 2)

        ol.delete(NODE_VALUE, True)
        nodes = ol.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 0)
        self.assertEqual(ol.len(), 1)
        self.assertEqual(ol.head.value, 55)
        self.assertEqual(ol.tail.value, 55)

        # удаление единственного элемента в списке
        ol.delete(55)
        self.assertEqual(ol.len(), 0)
        self.assertIsNone(ol.head)
        self.assertIsNone(ol.tail)

        # удаление элемента из пустого списка
        self.assertEqual(ol.len(), 0)
        ol.delete(55)
        self.assertEqual(ol.len(), 0)
        self.assertIsNone(ol.head)
        self.assertIsNone(ol.tail)

        # удаление элемента из списка
        # после чего остается только один элемент в списке
        ol.add(NODE_VALUE)
        ol.add(55)
        self.assertEqual(ol.len(), 2)

        ol.delete(55)
        self.assertEqual(ol.head.value, 12)
        self.assertEqual(ol.tail.value, 12)
        self.assertIsNone(ol.head.next)
        self.assertIsNone(ol.tail.next)
        self.assertEqual(ol.len(), 1)

        ol.add(55)
        self.assertEqual(ol.len(), 2)

        ol.delete(NODE_VALUE)
        self.assertEqual(ol.head.value, 55)
        self.assertEqual(ol.tail.value, 55)
        self.assertIsNone(ol.head.next)
        self.assertIsNone(ol.tail.next)
        self.assertEqual(ol.len(), 1)

        # проверка на удаление элементов со значением 0
        ol = OrderedList(True)
        ol.add(0)
        ol.add(0)
        ol.add(1)
        ol.add(1)
        ol.add(2)
        ol.add(2)
        self.assertEqual(ol.len(), 6)

        ol.delete(1, True)
        ol.delete(2, True)
        ol.delete(0)

        self.assertEqual(ol.head.value, 0)
        self.assertEqual(ol.tail.value, 0)
        self.assertIsNone(ol.head.next)
        self.assertIsNone(ol.tail.next)
        self.assertEqual(ol.len(), 1)

    def test_len(self):
        ol = OrderedList(True)

        ol.add(12)
        ol.add(55)
        ol.add(12)

        self.assertEqual(ol.len(), 3)

        ol.delete(12, True)
        self.assertEqual(ol.len(), 1)

    def test_clean(self):
        ol = OrderedList(False)

        ol.add(1)
        ol.add(2)
        ol.add(3)

        ol.clean(True)
        self.assertIsNone(ol.head)
        self.assertIsNone(ol.tail)
        self.assertEqual(ol.len(), 0)

        ol.add(1)
        ol.add(2)
        ol.add(3)

        ol.clean(False)
        self.assertIsNone(ol.head)
        self.assertIsNone(ol.tail)
        self.assertEqual(ol.len(), 0)

    def test_validate_node(self):
        ol = OrderedList(True)

        self.assertTrue(ol._validate_node(Node(123)))
        self.assertFalse(ol._validate_node(123))
        self.assertFalse(ol._validate_node('test'))


class TestOrderedStringListMethods(unittest.TestCase):
    def test_add(self):
        # asc
        ol = OrderedStringList(True)

        ol.add("aaaa")
        self.assertEqual(ol.head.value, "aaaa")
        self.assertEqual(ol.tail.value, "aaaa")

        ol.add("AaaAa")
        self.assertEqual(ol.head.value, "AaaAa")
        self.assertEqual(ol.head.next.value, "aaaa")
        self.assertEqual(ol.tail.prev.value, "AaaAa")
        self.assertEqual(ol.tail.value, "aaaa")

        ol.add("bbbb")
        self.assertEqual(ol.head.value, "AaaAa")
        self.assertEqual(ol.head.next.value, "aaaa")
        self.assertEqual(ol.tail.value, "bbbb")

        ol.add("130")
        self.assertEqual(ol.head.value, "130")
        self.assertEqual(ol.head.next.value, "AaaAa")
        self.assertEqual(ol.tail.prev.value, "aaaa")
        self.assertEqual(ol.tail.value, "bbbb")

        ol.add("")
        self.assertEqual(ol.head.value, "")
        self.assertEqual(ol.head.next.value, "130")
        self.assertEqual(ol.tail.value, "bbbb")

        ol.add("-1")
        self.assertEqual(ol.head.value, "")
        self.assertEqual(ol.head.next.value, "-1")
        self.assertEqual(ol.tail.value, "bbbb")

        ol.add("128")
        self.assertEqual(ol.head.value, "")
        self.assertEqual(ol.head.next.value, "-1")
        self.assertEqual(ol.head.next.next.value, "128")
        self.assertEqual(ol.head.next.next.next.value, "130")
        self.assertEqual(ol.tail.value, "bbbb")

        ol.add("10")
        self.assertEqual(ol.head.value, "")
        self.assertEqual(ol.head.next.value, "-1")
        self.assertEqual(ol.head.next.next.value, "10")
        self.assertEqual(ol.tail.value, "bbbb")

        ol.add("1")
        self.assertEqual(ol.head.value, "")
        self.assertEqual(ol.head.next.value, "-1")
        self.assertEqual(ol.head.next.next.value, "1")
        self.assertEqual(ol.head.next.next.next.value, "10")
        self.assertEqual(ol.tail.value, "bbbb")

        ol.add("130")
        self.assertEqual(ol.head.value, "")
        self.assertEqual(ol.head.next.value, "-1")
        self.assertEqual(ol.head.next.next.value, "1")
        self.assertEqual(ol.head.next.next.next.value, "10")
        self.assertEqual(ol.head.next.next.next.next.value, "128")
        self.assertEqual(ol.head.next.next.next.next.next.value, "130")
        self.assertEqual(ol.head.next.next.next.next.next.next.value, "130")
        self.assertEqual(ol.tail.value, "bbbb")

        ol.add("")
        self.assertEqual(ol.head.value, "")
        self.assertEqual(ol.head.next.value, "")
        self.assertEqual(ol.head.next.next.value, "-1")
        self.assertEqual(ol.tail.value, "bbbb")

        ol.add("-1")
        self.assertEqual(ol.head.value, "")
        self.assertEqual(ol.head.next.value, "")
        self.assertEqual(ol.head.next.next.value, "-1")
        self.assertEqual(ol.head.next.next.next.value, "-1")
        self.assertEqual(ol.tail.value, "bbbb")

        # desc
        ol = OrderedStringList(False)
        ol.add("128")
        self.assertEqual(ol.head.value, "128")
        self.assertEqual(ol.tail.value, "128")

        ol.add("10")
        self.assertEqual(ol.head.value, "128")
        self.assertEqual(ol.head.next.value, "10")
        self.assertEqual(ol.tail.prev.value, "128")
        self.assertEqual(ol.tail.value, "10")

        ol.add("1")
        self.assertEqual(ol.head.value, "128")
        self.assertEqual(ol.head.next.value, "10")
        self.assertEqual(ol.tail.value, "1")

        ol.add("130")
        self.assertEqual(ol.head.value, "130")
        self.assertEqual(ol.head.next.value, "128")
        self.assertEqual(ol.head.next.next.value, "10")
        self.assertEqual(ol.tail.value, "1")

        ol.add("")
        self.assertEqual(ol.head.value, "130")
        self.assertEqual(ol.head.next.value, "128")
        self.assertEqual(ol.head.next.next.value, "10")
        self.assertEqual(ol.tail.prev.value, "1")
        self.assertEqual(ol.tail.value, "")

        ol.add("-1")
        self.assertEqual(ol.head.value, "130")
        self.assertEqual(ol.head.next.value, "128")
        self.assertEqual(ol.head.next.next.value, "10")
        self.assertEqual(ol.head.next.next.next.value, "1")
        self.assertEqual(ol.tail.prev.value, "-1")
        self.assertEqual(ol.tail.value, "")

    def test_print_all_nodes(self):
        import io
        from contextlib import redirect_stdout

        ol = OrderedStringList(True)
        ol.add("12")
        ol.add("55")
        ol.add("12")
        ol.add("1")

        f = io.StringIO()
        with redirect_stdout(f):
            ol.print_all_nodes()

        actual = f.getvalue()
        expected = "1\n12\n12\n55\n"
        self.assertEqual(actual, expected)

        ol = OrderedStringList(False)
        ol.add("12")
        ol.add("55")
        ol.add("12")
        ol.add("1")

        f = io.StringIO()
        with redirect_stdout(f):
            ol.print_all_nodes()

        actual = f.getvalue()
        expected = "55\n12\n12\n1\n"
        self.assertEqual(actual, expected)

    def test_find(self):
        # asc
        ol = OrderedStringList(True)

        ol.add("1")
        ol.add("1")
        ol.add("33")
        ol.add("55")
        ol.add("33")

        # поиск по значению, первое совпадение
        node = ol.find("1")
        self.assertEqual(node.value, "1")
        self.assertEqual(node.next.value, "1")

        # поиск по значению, первое совпадение
        node = ol.find("33")
        self.assertEqual(node.value, "33")
        self.assertEqual(node.next.value, "33")
        self.assertEqual(node.prev.value, "1")

        # поиск несуществующего значения
        node = ol.find("128")
        self.assertIsNone(node)

        # поиск по пустой строке
        ol.add("")
        node = ol.find("")
        self.assertEqual(node.value, "")

        # поиск в пустом списке
        ol = OrderedStringList(True)
        node = ol.find("12")
        self.assertIsNone(node)

        # поиск в списке из одного узла
        ol.add("12")
        node = ol.find("12")
        self.assertEqual(node.value, "12")

        # поиск в списке из одного узла несуществующего элемента
        node = ol.find("10")
        self.assertIsNone(node)

        # desc
        ol = OrderedStringList(False)

        ol.add("1")
        ol.add("1")
        ol.add("33")
        ol.add("55")
        ol.add("33")

        node = ol.find("55")
        self.assertEqual(node.value, "55")
        self.assertEqual(node.next.value, "33")

        # поиск по значению, первое совпадение
        node = ol.find("1")
        self.assertEqual(node.value, "1")
        self.assertEqual(node.next.value, "1")
        self.assertEqual(node.prev.value, "33")

        # поиск по значению, первое совпадение
        node = ol.find("33")
        self.assertEqual(node.value, "33")
        self.assertEqual(node.next.value, "33")
        self.assertEqual(node.prev.value, "55")

    def test_find_all(self):
        ol = OrderedStringList(True)

        ol.add("12")
        ol.add("55")
        ol.add("12")

        # поиск значения
        nodes = ol.find_all("12")
        self.assertEqual(len(nodes), 2)

        for node in nodes:
            self.assertEqual(node.value, "12")

        # поиск несуществующего значения
        nodes = ol.find_all("120")
        self.assertEqual(len(nodes), 0)

        # поиск по нулевому значению
        ol.add("")
        nodes = ol.find_all("")
        self.assertEqual(len(nodes), 1)

        # поиск в пустом списке
        ol = OrderedStringList(True)
        nodes = ol.find_all("12")
        self.assertEqual(len(nodes), 0)

        # поиск в списке из одного узла
        ol.add("12")
        nodes = ol.find_all("12")
        self.assertEqual(len(nodes), 1)

        for node in nodes:
            self.assertEqual(node.value, "12")

        # поиск в списке из одного узла несуществующего элемента
        nodes = ol.find_all("10")
        self.assertEqual(len(nodes), 0)

    def test_delete(self):
        ol = OrderedStringList(True)

        ol.add("12")
        ol.add("55")
        ol.add("12")
        self.assertEqual(ol.len(), 3)

        # удаление первого найденого элемента из нескольких найденных
        NODE_VALUE = "12"
        nodes = ol.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 2)

        ol.delete(NODE_VALUE)
        nodes = ol.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(ol.len(), 2)
        self.assertEqual(ol.head.value, "12")
        self.assertEqual(ol.tail.value, "55")

        # удаление всех найденных элементов
        ol.add(NODE_VALUE)
        nodes = ol.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 2)

        ol.delete(NODE_VALUE, True)
        nodes = ol.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 0)
        self.assertEqual(ol.len(), 1)
        self.assertEqual(ol.head.value, "55")
        self.assertEqual(ol.tail.value, "55")

        # удаление единственного элемента в списке
        ol.delete("55")
        self.assertEqual(ol.len(), 0)
        self.assertIsNone(ol.head)
        self.assertIsNone(ol.tail)

        # удаление элемента из пустого списка
        self.assertEqual(ol.len(), 0)
        ol.delete(55)
        self.assertEqual(ol.len(), 0)
        self.assertIsNone(ol.head)
        self.assertIsNone(ol.tail)

        # удаление элемента из списка
        # после чего остается только один элемент в списке
        ol.add(NODE_VALUE)
        ol.add("55")
        self.assertEqual(ol.len(), 2)

        ol.delete("55")
        self.assertEqual(ol.head.value, "12")
        self.assertEqual(ol.tail.value, "12")
        self.assertIsNone(ol.head.next)
        self.assertIsNone(ol.tail.next)
        self.assertEqual(ol.len(), 1)

        ol.add("55")
        self.assertEqual(ol.len(), 2)

        ol.delete(NODE_VALUE)
        self.assertEqual(ol.head.value, "55")
        self.assertEqual(ol.tail.value, "55")
        self.assertIsNone(ol.head.next)
        self.assertIsNone(ol.tail.next)
        self.assertEqual(ol.len(), 1)

        # проверка на удаление элементов с пустой строкой
        ol = OrderedStringList(True)
        ol.add("")
        ol.add("")
        ol.add("1")
        ol.add("1")
        ol.add("2")
        ol.add("2")
        self.assertEqual(ol.len(), 6)

        ol.delete("1", True)
        ol.delete("2", True)
        ol.delete("")

        self.assertEqual(ol.head.value, "")
        self.assertEqual(ol.tail.value, "")
        self.assertIsNone(ol.head.next)
        self.assertIsNone(ol.tail.next)
        self.assertEqual(ol.len(), 1)

    def test_len(self):
        ol = OrderedStringList(True)

        ol.add("12")
        ol.add("55")
        ol.add("12")

        self.assertEqual(ol.len(), 3)

        ol.delete("12", True)
        self.assertEqual(ol.len(), 1)

    def test_clean(self):
        ol = OrderedStringList(False)

        ol.add(1)
        ol.add(2)
        ol.add(3)

        ol.clean(True)
        self.assertIsNone(ol.head)
        self.assertIsNone(ol.tail)
        self.assertEqual(ol.len(), 0)

        ol.add(1)
        ol.add(2)
        ol.add(3)

        ol.clean(False)
        self.assertIsNone(ol.head)
        self.assertIsNone(ol.tail)
        self.assertEqual(ol.len(), 0)

    def test_validate_node(self):
        ol = OrderedStringList(True)

        self.assertTrue(ol._validate_node(Node(123)))
        self.assertFalse(ol._validate_node(123))
        self.assertFalse(ol._validate_node('test'))


if __name__ == '__main__':
    unittest.main()
