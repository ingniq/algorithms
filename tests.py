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
        NODE_VAL = 12
        node = self.linked_list.find(NODE_VAL)
        self.assertEqual(node.value, NODE_VAL)

        NODE_VAL = 128
        node = self.linked_list.find(NODE_VAL)
        self.assertIsNone(node)

        NODE_VAL = '12'
        node = self.linked_list.find(NODE_VAL)
        self.assertIsNone(node)

        NODE_VAL = None
        node = self.linked_list.find(NODE_VAL)
        self.assertIsNone(node)

        NODE_VAL = ['test', 12]
        self.linked_list.add_in_tail(Node(NODE_VAL))
        node = self.linked_list.find(NODE_VAL)
        self.assertEqual(node.value, NODE_VAL)

    def test_find_all(self):
        NODE_VAL = 12
        nodes = self.linked_list.find_all(NODE_VAL)
        self.assertEqual(len(nodes), 2)
        for node in nodes:
            self.assertEqual(node.value, NODE_VAL)

        NODE_VAL = ['test', 12]
        self.linked_list.add_in_tail(Node(NODE_VAL))
        nodes = self.linked_list.find_all(NODE_VAL)
        self.assertEqual(len(nodes), 1)
        for node in nodes:
            self.assertEqual(node.value, NODE_VAL)

        NODE_VAL = 120
        nodes = self.linked_list.find_all(NODE_VAL)
        self.assertEqual(len(nodes), 0)

        nodes = self.linked_list.find_all()
        self.assertEqual(len(nodes), 4)

        NODE_VAL = None
        nodes = self.linked_list.find_all()
        self.assertEqual(len(nodes), 4)

    def test_delete(self):
        NODE_VALUE = 12
        nodes = self.linked_list.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 2)

        self.linked_list.delete(NODE_VALUE)
        nodes = self.linked_list.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 1)

        self.linked_list.add_in_tail(Node(NODE_VALUE))
        nodes = self.linked_list.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 2)

        self.linked_list.delete(NODE_VALUE, True)
        nodes = self.linked_list.find_all(NODE_VALUE)
        self.assertEqual(len(nodes), 0)

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
        NODE_VALUE = 1200
        self.linked_list.insert(None, Node(NODE_VALUE))
        self.assertEqual(self.linked_list.head.value, NODE_VALUE)
        self.assertEqual(self.linked_list.len(), 4)

        NODE_VALUE = 55
        node = self.linked_list.find(NODE_VALUE)
        self.linked_list.insert(node, Node(NODE_VALUE + 11))
        self.assertEqual(node.next.value, NODE_VALUE + 11)
        self.assertEqual(self.linked_list.len(), 5)

        NODE_VALUE = 100
        self.linked_list.insert(node, NODE_VALUE)
        self.assertEqual(self.linked_list.len(), 5)

        NODE_VALUE = 100
        self.linked_list.insert(Node(1500), NODE_VALUE)
        self.assertEqual(self.linked_list.len(), 5)

    def test_validate_node(self):
        self.assertTrue(self.linked_list._validate_node(Node(123)))
        self.assertFalse(self.linked_list._validate_node(123))
        self.assertFalse(self.linked_list._validate_node('test'))


if __name__ == '__main__':
    unittest.main()
