import unittest
from bst import BST, BSTNode


class TestBSTMethods(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        self.bst = BST(None)
        super().__init__(methodName)

    def __create_default_BST(self):
        self.bst.AddKeyValue(8, 8)
        self.bst.AddKeyValue(4, 4)
        self.bst.AddKeyValue(2, 2)
        self.bst.AddKeyValue(12, 12)
        self.bst.AddKeyValue(6, 6)
        self.bst.AddKeyValue(1, 1)
        self.bst.AddKeyValue(3, 3)
        self.bst.AddKeyValue(5, 5)
        self.bst.AddKeyValue(7, 7)
        self.bst.AddKeyValue(10, 10)
        self.bst.AddKeyValue(14, 14)
        self.bst.AddKeyValue(9, 9)
        self.bst.AddKeyValue(11, 11)
        self.bst.AddKeyValue(13, 13)
        self.bst.AddKeyValue(15, 15)
        self.bst.AddKeyValue(20, 20)

        #        8
        #       / \
        #      4  12
        #     / | |   \
        #   2   6 10    14
        #  /|  /| | \   | \
        # 1 3 5 7 9 11 13 15
        #                   \
        #                   20

    def test_create_BST(self):
        # create binary search tree
        root_node = BSTNode(8, 8, None)
        bst = BST(root_node)
        self.assertEqual(bst.Root, root_node)
        self.assertEqual(bst.Root.NodeKey, 8)
        self.assertEqual(bst.Root.NodeValue, 8)
        self.assertIsNone(bst.Root.Parent)

        bst = BST(None)

        self.assertIsNone(bst.Root)
        bst.AddKeyValue(8, 8)
        self.assertIsNotNone(bst.Root)
        self.assertEqual(bst.Root.NodeKey, 8)

    def test_AddKeyValue(self):
        self.bst.AddKeyValue(8, 8)
        self.assertIsNone(self.bst.Root.LeftChild)
        self.assertIsNone(self.bst.Root.RightChild)

        # Adding a node to the left
        self.assertTrue(self.bst.AddKeyValue(4, 4))
        self.assertEqual(self.bst.Root.LeftChild.NodeKey, 4)
        self.assertIsNone(self.bst.Root.RightChild)

        # Adding a node to the left
        self.assertTrue(self.bst.AddKeyValue(2, 2))
        self.assertEqual(self.bst.Root.LeftChild.NodeKey, 4)
        self.assertIsNone(self.bst.Root.RightChild)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertIsNone(self.bst.Root.LeftChild.RightChild)

        # Adding a node with an existing key. The tree does not change.
        self.assertFalse(self.bst.AddKeyValue(2, 2))
        self.assertEqual(self.bst.Root.LeftChild.NodeKey, 4)
        self.assertIsNone(self.bst.Root.RightChild)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertIsNone(self.bst.Root.LeftChild.RightChild)

        # Adding a node to the right
        self.bst.AddKeyValue(12, 12)
        self.assertEqual(self.bst.Root.LeftChild.NodeKey, 4)
        self.assertEqual(self.bst.Root.RightChild.NodeKey, 12)

        # Adding a node to the right
        self.bst.AddKeyValue(6, 6)
        self.assertEqual(self.bst.Root.LeftChild.NodeKey, 4)
        self.assertEqual(self.bst.Root.RightChild.NodeKey, 12)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.NodeKey, 6)

        self.bst.AddKeyValue(1, 1)
        self.bst.AddKeyValue(3, 3)
        self.bst.AddKeyValue(5, 5)
        self.bst.AddKeyValue(7, 7)
        self.bst.AddKeyValue(10, 10)
        self.bst.AddKeyValue(14, 14)
        self.bst.AddKeyValue(9, 9)
        self.bst.AddKeyValue(11, 11)
        self.bst.AddKeyValue(13, 13)
        self.bst.AddKeyValue(15, 15)

        self.assertEqual(self.bst.Root.NodeKey, 8)
        # left branch
        self.assertEqual(self.bst.Root.LeftChild.NodeKey, 4)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.NodeKey, 6)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.LeftChild.NodeKey, 1)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.RightChild.NodeKey, 3)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.LeftChild.NodeKey, 5)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.RightChild.NodeKey, 7)

        self.assertEqual(self.bst.Root.LeftChild.Parent.NodeKey, 8)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.Parent.NodeKey, 4)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.Parent.NodeKey, 4)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.LeftChild.Parent.NodeKey, 2)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.RightChild.Parent.NodeKey, 2)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.LeftChild.Parent.NodeKey, 6)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.RightChild.Parent.NodeKey, 6)


        self.assertIsNone(self.bst.Root.LeftChild.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(self.bst.Root.LeftChild.LeftChild.LeftChild.RightChild)
        self.assertIsNone(self.bst.Root.LeftChild.LeftChild.RightChild.RightChild)
        self.assertIsNone(self.bst.Root.LeftChild.LeftChild.RightChild.LeftChild)
        self.assertIsNone(self.bst.Root.LeftChild.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.bst.Root.LeftChild.RightChild.LeftChild.RightChild)
        self.assertIsNone(self.bst.Root.LeftChild.RightChild.RightChild.LeftChild)
        self.assertIsNone(self.bst.Root.LeftChild.RightChild.RightChild.RightChild)

        # right branch
        self.assertEqual(self.bst.Root.RightChild.NodeKey, 12)
        self.assertEqual(self.bst.Root.RightChild.LeftChild.NodeKey, 10)
        self.assertEqual(self.bst.Root.RightChild.RightChild.NodeKey, 14)
        self.assertEqual(self.bst.Root.RightChild.LeftChild.LeftChild.NodeKey, 9)
        self.assertEqual(self.bst.Root.RightChild.LeftChild.RightChild.NodeKey, 11)
        self.assertEqual(self.bst.Root.RightChild.RightChild.LeftChild.NodeKey, 13)
        self.assertEqual(self.bst.Root.RightChild.RightChild.RightChild.NodeKey, 15)

        self.assertEqual(self.bst.Root.RightChild.Parent.NodeKey, 8)
        self.assertEqual(self.bst.Root.RightChild.LeftChild.Parent.NodeKey, 12)
        self.assertEqual(self.bst.Root.RightChild.RightChild.Parent.NodeKey, 12)
        self.assertEqual(self.bst.Root.RightChild.LeftChild.LeftChild.Parent.NodeKey, 10)
        self.assertEqual(self.bst.Root.RightChild.LeftChild.RightChild.Parent.NodeKey, 10)
        self.assertEqual(self.bst.Root.RightChild.RightChild.LeftChild.Parent.NodeKey, 14)
        self.assertEqual(self.bst.Root.RightChild.RightChild.RightChild.Parent.NodeKey, 14)

        self.assertIsNone(self.bst.Root.RightChild.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(self.bst.Root.RightChild.LeftChild.LeftChild.RightChild)
        self.assertIsNone(self.bst.Root.RightChild.LeftChild.RightChild.RightChild)
        self.assertIsNone(self.bst.Root.RightChild.LeftChild.RightChild.LeftChild)
        self.assertIsNone(self.bst.Root.RightChild.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.bst.Root.RightChild.RightChild.LeftChild.RightChild)
        self.assertIsNone(self.bst.Root.RightChild.RightChild.RightChild.LeftChild)
        self.assertIsNone(self.bst.Root.RightChild.RightChild.RightChild.RightChild)

        # Adding a node to the right
        self.bst.AddKeyValue(20, 20)
        self.assertEqual(self.bst.Root.RightChild.RightChild.RightChild.RightChild.NodeKey, 20)
        self.assertEqual(self.bst.Root.RightChild.RightChild.RightChild.RightChild.Parent.NodeKey, 15)

        #        8
        #       / \
        #      4  12
        #     / | |   \
        #   2   6 10    14
        #  /|  /| | \   | \
        # 1 3 5 7 9 11 13 15
        #                   \
        #                   20

    def test_FindNodeByKey(self):
        # empty tree
        found = self.bst.FindNodeByKey(8)
        self.assertIsNone(found.Node)
        self.assertFalse(found.NodeHasKey)
        self.assertFalse(found.ToLeft)

        self.__create_default_BST()

        # node found
        found = self.bst.FindNodeByKey(8)
        self.assertTrue(found.NodeHasKey)
        self.assertEqual(found.Node.NodeKey, 8)
        self.assertFalse(found.ToLeft)

        # node found
        found = self.bst.FindNodeByKey(10)
        self.assertTrue(found.NodeHasKey)
        self.assertEqual(found.Node.NodeKey, 10)
        self.assertFalse(found.ToLeft)

        # node not found (inserting to left)
        found = self.bst.FindNodeByKey(17)
        self.assertFalse(found.NodeHasKey)
        self.assertEqual(found.Node.NodeKey, 20)
        self.assertTrue(found.ToLeft)

        # node not found (inserting to right)
        found = self.bst.FindNodeByKey(21)
        self.assertFalse(found.NodeHasKey)
        self.assertEqual(found.Node.NodeKey, 20)
        self.assertFalse(found.ToLeft)

        # node not found (inserting to left)
        found = self.bst.FindNodeByKey(-5)
        self.assertFalse(found.NodeHasKey)
        self.assertEqual(found.Node.NodeKey, 1)
        self.assertTrue(found.ToLeft)

    def test_FinMinMax(self):
        # try search in empty tree from root
        max_node = self.bst.FinMinMax(self.bst.Root, True)
        min_node = self.bst.FinMinMax(self.bst.Root, False)
        self.assertIsNone(max_node)
        self.assertIsNone(min_node)

        # try searching in an empty tree from a node that does not belong to the tree
        node = BSTNode(8, 8, None)
        max_node = self.bst.FinMinMax(node, True)
        min_node = self.bst.FinMinMax(node, False)
        self.assertIsNone(max_node)
        self.assertIsNone(min_node)


        self.__create_default_BST()

        # start from root
        max_node = self.bst.FinMinMax(self.bst.Root, True)
        self.assertEqual(max_node.NodeKey, 20)

        min_node = self.bst.FinMinMax(self.bst.Root, False)
        self.assertEqual(min_node.NodeKey, 1)

        # start from NOT root
        from_node = self.bst.FindNodeByKey(12).Node
        max_node = self.bst.FinMinMax(from_node, True)
        self.assertEqual(max_node.NodeKey, 20)

        min_node = self.bst.FinMinMax(from_node, False)
        self.assertEqual(min_node.NodeKey, 9)

        # start from leaf
        max_node = self.bst.FinMinMax(max_node, True)
        self.assertEqual(max_node.NodeKey, 20)

        min_node = self.bst.FinMinMax(min_node, False)
        self.assertEqual(min_node.NodeKey, 9)

    def test_DeleteNodeByKey(self):
        # prepare tree
        self.__create_default_BST()
        self.bst.AddKeyValue(17, 17)
        self.bst.AddKeyValue(18, 18)
        self.bst.AddKeyValue(25, 25)

        #        8
        #       / \
        #      4  12
        #     / | |   \
        #   2   6 10    14
        #  /|  /| | \   | \
        # 1 3 5 7 9 11 13 15
        #                   \
        #                   20
        #                  /  \
        #                 17   25
        #                  \
        #                   18

        # delete node (not found)
        found_node = self.bst.FindNodeByKey(30)
        self.assertFalse(found_node.NodeHasKey)
        self.assertFalse(self.bst.DeleteNodeByKey(30))

        # delete node with children (successor node is left child)
        found_node = self.bst.FindNodeByKey(12)
        self.assertTrue(found_node.NodeHasKey)
        parent = found_node.Node.Parent
        right_child = found_node.Node.RightChild
        self.assertEqual(parent.RightChild.NodeKey, 12)
        self.assertEqual(right_child.LeftChild.NodeKey, 13)

        self.assertTrue(self.bst.DeleteNodeByKey(12))
        self.assertEqual(parent.RightChild.NodeKey, 13)
        self.assertIsNone(right_child.LeftChild)

        found_node = self.bst.FindNodeByKey(12)
        self.assertFalse(found_node.NodeHasKey)

        # delete leaf
        found_node = self.bst.FindNodeByKey(11)
        self.assertTrue(found_node.NodeHasKey)
        self.assertIsNone(found_node.Node.LeftChild)
        self.assertIsNone(found_node.Node.RightChild)

        parent = found_node.Node.Parent
        self.assertEqual(parent.RightChild.NodeKey, 11)

        self.assertTrue(self.bst.DeleteNodeByKey(11))
        self.assertIsNone(parent.RightChild)

        # delete node with children (successor node is node with right child only)
        found_node = self.bst.FindNodeByKey(15)
        self.assertTrue(found_node.NodeHasKey)
        parent = found_node.Node.Parent
        right_child = found_node.Node.RightChild
        self.assertEqual(parent.RightChild.NodeKey, 15)
        self.assertEqual(right_child.LeftChild.NodeKey, 17)
        self.assertEqual(right_child.LeftChild.RightChild.NodeKey, 18)
        self.assertIsNone(right_child.LeftChild.LeftChild)

        self.bst.DeleteNodeByKey(15)
        self.assertEqual(parent.RightChild.NodeKey, 17)
        self.assertEqual(right_child.LeftChild.NodeKey, 18)

        # delete root
        found_node = self.bst.FindNodeByKey(8)
        self.assertTrue(found_node.NodeHasKey)
        self.assertTrue(self.bst.DeleteNodeByKey(8))
        self.assertIsNone(self.bst.Root.Parent)
        self.assertEqual(self.bst.Root.LeftChild.NodeKey, 4)
        self.assertEqual(self.bst.Root.RightChild.NodeKey, 13)
        self.assertEqual(self.bst.Root.LeftChild.Parent.NodeKey, self.bst.Root.NodeKey)
        self.assertEqual(self.bst.Root.RightChild.Parent.NodeKey, self.bst.Root.NodeKey)


        #        9
        #       / \
        #      4  13
        #     / | |  \
        #   2   6 10  14
        #  /|  /|       \
        # 1 3 5 7        17
        #                  \
        #                   20
        #                  /  \
        #                 18   25

        # check all tree
        self.assertEqual(self.bst.Root.NodeKey, 9)
        # left branch
        self.assertEqual(self.bst.Root.LeftChild.NodeKey, 4)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.NodeKey, 6)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.LeftChild.NodeKey, 1)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.RightChild.NodeKey, 3)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.LeftChild.NodeKey, 5)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.RightChild.NodeKey, 7)

        self.assertEqual(self.bst.Root.LeftChild.RightChild.RightChild.Parent.NodeKey, 6)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.LeftChild.Parent.NodeKey, 6)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.LeftChild.Parent.NodeKey, 2)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.RightChild.Parent.NodeKey, 2)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.Parent.NodeKey, 4)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.Parent.NodeKey, 4)
        self.assertEqual(self.bst.Root.LeftChild.Parent.NodeKey, 9)


        self.assertIsNone(self.bst.Root.LeftChild.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(self.bst.Root.LeftChild.LeftChild.LeftChild.RightChild)
        self.assertIsNone(self.bst.Root.LeftChild.LeftChild.RightChild.RightChild)
        self.assertIsNone(self.bst.Root.LeftChild.LeftChild.RightChild.LeftChild)
        self.assertIsNone(self.bst.Root.LeftChild.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.bst.Root.LeftChild.RightChild.LeftChild.RightChild)
        self.assertIsNone(self.bst.Root.LeftChild.RightChild.RightChild.LeftChild)
        self.assertIsNone(self.bst.Root.LeftChild.RightChild.RightChild.RightChild)

        # right branch
        self.assertEqual(self.bst.Root.RightChild.NodeKey, 13)
        self.assertEqual(self.bst.Root.RightChild.LeftChild.NodeKey, 10)
        self.assertEqual(self.bst.Root.RightChild.RightChild.NodeKey, 14)
        self.assertEqual(self.bst.Root.RightChild.RightChild.RightChild.NodeKey, 17)
        self.assertEqual(self.bst.Root.RightChild.RightChild.RightChild.RightChild.NodeKey, 20)
        self.assertEqual(self.bst.Root.RightChild.RightChild.RightChild.RightChild.LeftChild.NodeKey, 18)
        self.assertEqual(self.bst.Root.RightChild.RightChild.RightChild.RightChild.RightChild.NodeKey, 25)

        self.assertEqual(self.bst.Root.RightChild.RightChild.RightChild.RightChild.RightChild.Parent.NodeKey, 20)
        self.assertEqual(self.bst.Root.RightChild.RightChild.RightChild.RightChild.LeftChild.Parent.NodeKey, 20)
        self.assertEqual(self.bst.Root.RightChild.RightChild.RightChild.RightChild.Parent.NodeKey, 17)
        self.assertEqual(self.bst.Root.RightChild.RightChild.RightChild.Parent.NodeKey, 14)
        self.assertEqual(self.bst.Root.RightChild.RightChild.Parent.NodeKey, 13)
        self.assertEqual(self.bst.Root.RightChild.LeftChild.Parent.NodeKey, 13)
        self.assertEqual(self.bst.Root.RightChild.Parent.NodeKey, 9)

        self.assertIsNone(self.bst.Root.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.bst.Root.RightChild.LeftChild.RightChild)
        self.assertIsNone(self.bst.Root.RightChild.RightChild.LeftChild)
        self.assertIsNone(self.bst.Root.RightChild.RightChild.RightChild.LeftChild)
        self.assertIsNone(self.bst.Root.RightChild.RightChild.RightChild.RightChild.RightChild.RightChild)
        self.assertIsNone(self.bst.Root.RightChild.RightChild.RightChild.RightChild.RightChild.LeftChild)
        self.assertIsNone(self.bst.Root.RightChild.RightChild.RightChild.RightChild.LeftChild.RightChild)
        self.assertIsNone(self.bst.Root.RightChild.RightChild.RightChild.RightChild.LeftChild.LeftChild)

    def test_Count(self):
        self.assertEqual(self.bst.Count(), 0)
        self.bst.AddKeyValue(8, 8)
        self.assertEqual(self.bst.Count(), 1)
        self.__create_default_BST()
        self.assertEqual(self.bst.Count(), 16)
