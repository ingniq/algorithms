import unittest
from bst import BST, BSTNode


class TestBSTMethods(unittest.TestCase):
    def test_methods(self):
        # create binary search tree
        root_node = BSTNode(8, 8, None)
        bst = BST(root_node)
        self.assertEqual(bst.Root, root_node)
        self.assertEqual(bst.Root.NodeKey, 8)
        self.assertEqual(bst.Root.NodeValue, 8)
        self.assertIsNone(bst.Root.Parent)

        bst = BST(None)
        self.assertIsNone(bst.Root)

        bst.Root = root_node

        # AddKeyValue
        self.assertIsNone(bst.Root.LeftChild)
        self.assertIsNone(bst.Root.RightChild)

        # Adding a node to the left
        self.assertTrue(bst.AddKeyValue(4, 4))
        self.assertEqual(bst.Root.LeftChild.NodeKey, 4)
        self.assertIsNone(bst.Root.RightChild)

        # Adding a node to the left
        self.assertTrue(bst.AddKeyValue(2, 2))
        self.assertEqual(bst.Root.LeftChild.NodeKey, 4)
        self.assertIsNone(bst.Root.RightChild)
        self.assertEqual(bst.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertIsNone(bst.Root.LeftChild.RightChild)

        # Adding a node with an existing key. The tree does not change.
        self.assertFalse(bst.AddKeyValue(2, 2))
        self.assertEqual(bst.Root.LeftChild.NodeKey, 4)
        self.assertIsNone(bst.Root.RightChild)
        self.assertEqual(bst.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertIsNone(bst.Root.LeftChild.RightChild)

        # Adding a node to the right
        bst.AddKeyValue(12, 12)
        self.assertEqual(bst.Root.LeftChild.NodeKey, 4)
        self.assertEqual(bst.Root.RightChild.NodeKey, 12)

        # Adding a node to the right
        bst.AddKeyValue(6, 6)
        self.assertEqual(bst.Root.LeftChild.NodeKey, 4)
        self.assertEqual(bst.Root.RightChild.NodeKey, 12)
        self.assertEqual(bst.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertEqual(bst.Root.LeftChild.RightChild.NodeKey, 6)

        bst.AddKeyValue(1, 1)
        bst.AddKeyValue(3, 3)
        bst.AddKeyValue(5, 5)
        bst.AddKeyValue(7, 7)
        bst.AddKeyValue(10, 10)
        bst.AddKeyValue(14, 14)
        bst.AddKeyValue(9, 9)
        bst.AddKeyValue(11, 11)
        bst.AddKeyValue(13, 13)
        bst.AddKeyValue(15, 15)

        self.assertEqual(bst.Root.NodeKey, 8)
        # left branch
        self.assertEqual(bst.Root.LeftChild.NodeKey, 4)
        self.assertEqual(bst.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertEqual(bst.Root.LeftChild.RightChild.NodeKey, 6)
        self.assertEqual(bst.Root.LeftChild.LeftChild.LeftChild.NodeKey, 1)
        self.assertEqual(bst.Root.LeftChild.LeftChild.RightChild.NodeKey, 3)
        self.assertEqual(bst.Root.LeftChild.RightChild.LeftChild.NodeKey, 5)
        self.assertEqual(bst.Root.LeftChild.RightChild.RightChild.NodeKey, 7)


        self.assertIsNone(bst.Root.LeftChild.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.RightChild.RightChild)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.RightChild.RightChild)

        # right branch
        self.assertEqual(bst.Root.RightChild.NodeKey, 12)
        self.assertEqual(bst.Root.RightChild.LeftChild.NodeKey, 10)
        self.assertEqual(bst.Root.RightChild.RightChild.NodeKey, 14)
        self.assertEqual(bst.Root.RightChild.LeftChild.LeftChild.NodeKey, 9)
        self.assertEqual(bst.Root.RightChild.LeftChild.RightChild.NodeKey, 11)
        self.assertEqual(bst.Root.RightChild.RightChild.LeftChild.NodeKey, 13)
        self.assertEqual(bst.Root.RightChild.RightChild.RightChild.NodeKey, 15)

        self.assertIsNone(bst.Root.RightChild.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.LeftChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.LeftChild.RightChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.LeftChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.RightChild.RightChild)

        # Adding a node to the right
        bst.AddKeyValue(20, 20)
        self.assertEqual(bst.Root.RightChild.RightChild.RightChild.RightChild.NodeKey, 20)

        #        8
        #       / \
        #      4  12
        #     / | |   \
        #   2   6 10    14
        #  /|  /| | \   | \
        # 1 3 5 7 9 11 13 15
        #                   \
        #                   20

        # FindNodeByKey
        # node found
        found = bst.FindNodeByKey(8)
        self.assertTrue(found.NodeHasKey)
        self.assertEqual(found.Node.NodeKey, 8)
        self.assertFalse(found.ToLeft)

        # node found
        found = bst.FindNodeByKey(10)
        self.assertTrue(found.NodeHasKey)
        self.assertEqual(found.Node.NodeKey, 10)
        self.assertFalse(found.ToLeft)

        # node not found (inserting to left)
        found = bst.FindNodeByKey(17)
        self.assertFalse(found.NodeHasKey)
        self.assertEqual(found.Node.NodeKey, 20)
        self.assertTrue(found.ToLeft)

        # node not found (inserting to right)
        found = bst.FindNodeByKey(21)
        self.assertFalse(found.NodeHasKey)
        self.assertEqual(found.Node.NodeKey, 20)
        self.assertFalse(found.ToLeft)

        # node not found (inserting to left)
        found = bst.FindNodeByKey(-5)
        self.assertFalse(found.NodeHasKey)
        self.assertEqual(found.Node.NodeKey, 1)
        self.assertTrue(found.ToLeft)

        # FinMinMax
        # start from root
        max_node = bst.FinMinMax(bst.Root, True)
        self.assertEqual(max_node.NodeKey, 20)

        min_node = bst.FinMinMax(bst.Root, False)
        self.assertEqual(min_node.NodeKey, 1)

        # start from NOT root
        from_node = bst.FindNodeByKey(12).Node
        max_node = bst.FinMinMax(from_node, True)
        self.assertEqual(max_node.NodeKey, 20)

        min_node = bst.FinMinMax(from_node, False)
        self.assertEqual(min_node.NodeKey, 9)

        # start from leaf
        max_node = bst.FinMinMax(max_node, True)
        self.assertEqual(max_node.NodeKey, 20)

        min_node = bst.FinMinMax(min_node, False)
        self.assertEqual(min_node.NodeKey, 9)

        # DeleteNodeByKey
        # prepare tree
        bst.AddKeyValue(17, 17)
        bst.AddKeyValue(18, 18)
        bst.AddKeyValue(25, 25)

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
        found_node = bst.FindNodeByKey(30)
        self.assertFalse(found_node.NodeHasKey)
        self.assertFalse(bst.DeleteNodeByKey(30))

        # delete node with children (successor node is left child)
        found_node = bst.FindNodeByKey(12)
        self.assertTrue(found_node.NodeHasKey)
        parent = found_node.Node.Parent
        right_child = found_node.Node.RightChild
        self.assertEqual(parent.RightChild.NodeKey, 12)
        self.assertEqual(right_child.LeftChild.NodeKey, 13)

        self.assertTrue(bst.DeleteNodeByKey(12))
        self.assertEqual(parent.RightChild.NodeKey, 13)
        self.assertIsNone(right_child.LeftChild)

        found_node = bst.FindNodeByKey(12)
        self.assertFalse(found_node.NodeHasKey)

        # delete leaf
        found_node = bst.FindNodeByKey(11)
        self.assertTrue(found_node.NodeHasKey)
        self.assertIsNone(found_node.Node.LeftChild)
        self.assertIsNone(found_node.Node.RightChild)

        parent = found_node.Node.Parent
        self.assertEqual(parent.RightChild.NodeKey, 11)

        self.assertTrue(bst.DeleteNodeByKey(11))
        self.assertIsNone(parent.RightChild)

        # delete node with children (successor node is node with right child only)
        found_node = bst.FindNodeByKey(15)
        self.assertTrue(found_node.NodeHasKey)
        parent = found_node.Node.Parent
        right_child = found_node.Node.RightChild
        self.assertEqual(parent.RightChild.NodeKey, 15)
        self.assertEqual(right_child.LeftChild.NodeKey, 17)
        self.assertEqual(right_child.LeftChild.RightChild.NodeKey, 18)
        self.assertIsNone(right_child.LeftChild.LeftChild)

        bst.DeleteNodeByKey(15)
        self.assertEqual(parent.RightChild.NodeKey, 17)
        self.assertEqual(right_child.LeftChild.NodeKey, 18)

        #        8
        #       / \
        #      4  13
        #     / | |  \
        #   2   6 10  14
        #  /|  /| |     \
        # 1 3 5 7 9      17
        #                  \
        #                   20
        #                  /  \
        #                 18   25


        # check all tree
        self.assertEqual(bst.Root.NodeKey, 8)
        # left branch
        self.assertEqual(bst.Root.LeftChild.NodeKey, 4)
        self.assertEqual(bst.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertEqual(bst.Root.LeftChild.RightChild.NodeKey, 6)
        self.assertEqual(bst.Root.LeftChild.LeftChild.LeftChild.NodeKey, 1)
        self.assertEqual(bst.Root.LeftChild.LeftChild.RightChild.NodeKey, 3)
        self.assertEqual(bst.Root.LeftChild.RightChild.LeftChild.NodeKey, 5)
        self.assertEqual(bst.Root.LeftChild.RightChild.RightChild.NodeKey, 7)


        self.assertIsNone(bst.Root.LeftChild.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.RightChild.RightChild)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.RightChild.RightChild)

        # right branch
        self.assertEqual(bst.Root.RightChild.NodeKey, 13)
        self.assertEqual(bst.Root.RightChild.LeftChild.NodeKey, 10)
        self.assertEqual(bst.Root.RightChild.RightChild.NodeKey, 14)
        self.assertEqual(bst.Root.RightChild.LeftChild.LeftChild.NodeKey, 9)
        self.assertEqual(bst.Root.RightChild.RightChild.RightChild.NodeKey, 17)
        self.assertEqual(bst.Root.RightChild.RightChild.RightChild.RightChild.NodeKey, 20)
        self.assertEqual(bst.Root.RightChild.RightChild.RightChild.RightChild.LeftChild.NodeKey, 18)
        self.assertEqual(bst.Root.RightChild.RightChild.RightChild.RightChild.RightChild.NodeKey, 25)

        self.assertIsNone(bst.Root.RightChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.LeftChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.RightChild.RightChild.RightChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.RightChild.RightChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.RightChild.RightChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.RightChild.RightChild.LeftChild.LeftChild)

        # Count
        self.assertEqual(bst.Count(), 16)
