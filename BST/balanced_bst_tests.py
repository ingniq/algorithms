import unittest
from balanced_bst import BalancedBST, BSTNode

class TestBalancedBST(unittest.TestCase):

    def test_GenerateTree(self):
        bst = BalancedBST()

        input = []
        bst.GenerateTree(input)
        self.assertIsNone(bst.Root)

        input = [1]
        bst.GenerateTree(input)
        self.assertEqual(bst.Root.NodeKey, 1)
        self.assertEqual(bst.Root.Level, 0)
        self.assertIsNone(bst.Root.Parent)
        self.assertIsNone(bst.Root.LeftChild)
        self.assertIsNone(bst.Root.RightChild)

        input = [10, 5, 9]

        bst.GenerateTree(input)
        self.assertEqual(bst.Root.NodeKey, 9)
        self.assertEqual(bst.Root.Level, 0)
        self.assertIsNone(bst.Root.Parent)

        self.assertTrue(bst.Root.LeftChild.NodeKey < bst.Root.NodeKey)
        self.assertTrue(bst.Root.RightChild.NodeKey >= bst.Root.NodeKey)

        self.assertEqual(bst.Root.LeftChild.NodeKey, 5)
        self.assertEqual(bst.Root.RightChild.NodeKey, 10)
        self.assertEqual(bst.Root.LeftChild.Level, 1)
        self.assertIsNone(bst.Root.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild)
        self.assertEqual(bst.Root.RightChild.Level, 1)
        self.assertIsNone(bst.Root.RightChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.RightChild)
        self.assertEqual(bst.Root.LeftChild.Parent, bst.Root)
        self.assertEqual(bst.Root.RightChild.Parent, bst.Root)

        input = [10, 5, 9, 8]

        bst.GenerateTree(input)
        self.assertEqual(bst.Root.NodeKey, 9)
        self.assertEqual(bst.Root.Level, 0)
        self.assertIsNone(bst.Root.Parent)

        self.assertTrue(bst.Root.LeftChild.NodeKey < bst.Root.NodeKey)
        self.assertTrue(bst.Root.RightChild.NodeKey >= bst.Root.NodeKey)

        self.assertEqual(bst.Root.LeftChild.NodeKey, 8)
        self.assertEqual(bst.Root.RightChild.NodeKey, 10)
        self.assertEqual(bst.Root.LeftChild.Level, 1)
        self.assertIsNone(bst.Root.LeftChild.RightChild)
        self.assertEqual(bst.Root.RightChild.Level, 1)
        self.assertIsNone(bst.Root.RightChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.RightChild)
        self.assertEqual(bst.Root.LeftChild.Parent, bst.Root)
        self.assertEqual(bst.Root.RightChild.Parent, bst.Root)

        self.assertTrue(bst.Root.LeftChild.LeftChild.NodeKey < bst.Root.LeftChild.NodeKey)

        self.assertEqual(bst.Root.LeftChild.LeftChild.NodeKey, 5)
        self.assertEqual(bst.Root.LeftChild.LeftChild.Level, 2)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.RightChild)
        self.assertEqual(bst.Root.LeftChild.LeftChild.Parent, bst.Root.LeftChild)

        input = [10, 5, 9, 4, 6, 8, 7]

        bst.GenerateTree(input)
        self.assertEqual(bst.Root.NodeKey, 7)
        self.assertEqual(bst.Root.Level, 0)
        self.assertIsNone(bst.Root.Parent)

        self.assertTrue(bst.Root.LeftChild.NodeKey < bst.Root.NodeKey)
        self.assertTrue(bst.Root.RightChild.NodeKey >= bst.Root.NodeKey)

        self.assertEqual(bst.Root.LeftChild.NodeKey, 5)
        self.assertEqual(bst.Root.RightChild.NodeKey, 9)
        self.assertEqual(bst.Root.LeftChild.Level, 1)
        self.assertEqual(bst.Root.RightChild.Level, 1)
        self.assertEqual(bst.Root.LeftChild.Parent, bst.Root)
        self.assertEqual(bst.Root.RightChild.Parent, bst.Root)

        self.assertTrue(bst.Root.LeftChild.LeftChild.NodeKey < bst.Root.LeftChild.NodeKey)
        self.assertTrue(bst.Root.LeftChild.RightChild.NodeKey >= bst.Root.LeftChild.NodeKey)
        self.assertTrue(bst.Root.RightChild.LeftChild.NodeKey < bst.Root.RightChild.NodeKey)
        self.assertTrue(bst.Root.RightChild.RightChild.NodeKey >= bst.Root.RightChild.NodeKey)

        self.assertEqual(bst.Root.LeftChild.LeftChild.NodeKey, 4)
        self.assertEqual(bst.Root.LeftChild.RightChild.NodeKey, 6)
        self.assertEqual(bst.Root.LeftChild.LeftChild.Level, 2)
        self.assertEqual(bst.Root.LeftChild.RightChild.Level, 2)
        self.assertEqual(bst.Root.LeftChild.LeftChild.Parent, bst.Root.LeftChild)
        self.assertEqual(bst.Root.LeftChild.RightChild.Parent, bst.Root.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.RightChild)

        self.assertEqual(bst.Root.RightChild.LeftChild.NodeKey, 8)
        self.assertEqual(bst.Root.RightChild.RightChild.NodeKey, 10)
        self.assertEqual(bst.Root.RightChild.LeftChild.Level, 2)
        self.assertEqual(bst.Root.RightChild.RightChild.Level, 2)
        self.assertEqual(bst.Root.RightChild.LeftChild.Parent, bst.Root.RightChild)
        self.assertEqual(bst.Root.RightChild.RightChild.Parent, bst.Root.RightChild)
        self.assertIsNone(bst.Root.RightChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.RightChild)

        input = [62, -5, 25, 64, 92, 50, -10, -1, 75, 80, 37, 84, 43, 55, 31]
        bst.GenerateTree(input)

        #             50
        #           /    \
        #         25      75
        #        /  \     /  \
        #      -5   37   62   84
        #     /|   / \   / \  | \
        #  -10 -1 31 43 55 64 80 92

        self.assertEqual(bst.Root.NodeKey, 50)
        self.assertEqual(bst.Root.Level, 0)
        self.assertIsNone(bst.Root.Parent)

        self.assertTrue(bst.Root.LeftChild.NodeKey < bst.Root.NodeKey)
        self.assertTrue(bst.Root.RightChild.NodeKey >= bst.Root.NodeKey)

        self.assertEqual(bst.Root.LeftChild.NodeKey, 25)
        self.assertEqual(bst.Root.RightChild.NodeKey, 75)

        self.assertEqual(bst.Root.LeftChild.Level, 1)
        self.assertEqual(bst.Root.RightChild.Level, 1)

        self.assertEqual(bst.Root.LeftChild.Parent, bst.Root)
        self.assertEqual(bst.Root.RightChild.Parent, bst.Root)

        self.assertTrue(bst.Root.LeftChild.LeftChild.NodeKey < bst.Root.LeftChild.NodeKey)
        self.assertTrue(bst.Root.LeftChild.RightChild.NodeKey >= bst.Root.LeftChild.NodeKey)
        self.assertTrue(bst.Root.RightChild.LeftChild.NodeKey < bst.Root.RightChild.NodeKey)
        self.assertTrue(bst.Root.RightChild.RightChild.NodeKey >= bst.Root.RightChild.NodeKey)

        self.assertEqual(bst.Root.LeftChild.LeftChild.NodeKey, -5)
        self.assertEqual(bst.Root.LeftChild.RightChild.NodeKey, 37)
        self.assertEqual(bst.Root.RightChild.LeftChild.NodeKey, 62)
        self.assertEqual(bst.Root.RightChild.RightChild.NodeKey, 84)

        self.assertEqual(bst.Root.LeftChild.LeftChild.Level, 2)
        self.assertEqual(bst.Root.LeftChild.RightChild.Level, 2)
        self.assertEqual(bst.Root.RightChild.LeftChild.Level, 2)
        self.assertEqual(bst.Root.RightChild.RightChild.Level, 2)

        self.assertEqual(bst.Root.LeftChild.LeftChild.Parent, bst.Root.LeftChild)
        self.assertEqual(bst.Root.LeftChild.RightChild.Parent, bst.Root.LeftChild)
        self.assertEqual(bst.Root.RightChild.LeftChild.Parent, bst.Root.RightChild)
        self.assertEqual(bst.Root.RightChild.RightChild.Parent, bst.Root.RightChild)

        self.assertTrue(bst.Root.LeftChild.LeftChild.LeftChild.NodeKey < bst.Root.LeftChild.LeftChild.NodeKey)
        self.assertTrue(bst.Root.LeftChild.LeftChild.RightChild.NodeKey >= bst.Root.LeftChild.LeftChild.NodeKey)
        self.assertTrue(bst.Root.LeftChild.RightChild.LeftChild.NodeKey < bst.Root.LeftChild.RightChild.NodeKey)
        self.assertTrue(bst.Root.LeftChild.RightChild.RightChild.NodeKey >= bst.Root.LeftChild.RightChild.NodeKey)
        self.assertTrue(bst.Root.RightChild.LeftChild.LeftChild.NodeKey < bst.Root.RightChild.LeftChild.NodeKey)
        self.assertTrue(bst.Root.RightChild.LeftChild.RightChild.NodeKey >= bst.Root.RightChild.LeftChild.NodeKey)
        self.assertTrue(bst.Root.RightChild.RightChild.LeftChild.NodeKey < bst.Root.RightChild.RightChild.NodeKey)
        self.assertTrue(bst.Root.RightChild.RightChild.RightChild.NodeKey >= bst.Root.RightChild.RightChild.NodeKey)

        self.assertEqual(bst.Root.LeftChild.LeftChild.LeftChild.NodeKey, -10)
        self.assertEqual(bst.Root.LeftChild.LeftChild.RightChild.NodeKey, -1)
        self.assertEqual(bst.Root.LeftChild.RightChild.LeftChild.NodeKey, 31)
        self.assertEqual(bst.Root.LeftChild.RightChild.RightChild.NodeKey, 43)
        self.assertEqual(bst.Root.RightChild.LeftChild.LeftChild.NodeKey, 55)
        self.assertEqual(bst.Root.RightChild.LeftChild.RightChild.NodeKey, 64)
        self.assertEqual(bst.Root.RightChild.RightChild.LeftChild.NodeKey, 80)
        self.assertEqual(bst.Root.RightChild.RightChild.RightChild.NodeKey, 92)

        self.assertEqual(bst.Root.LeftChild.LeftChild.LeftChild.Level, 3)
        self.assertEqual(bst.Root.LeftChild.LeftChild.RightChild.Level, 3)
        self.assertEqual(bst.Root.LeftChild.RightChild.LeftChild.Level, 3)
        self.assertEqual(bst.Root.LeftChild.RightChild.RightChild.Level, 3)
        self.assertEqual(bst.Root.RightChild.LeftChild.LeftChild.Level, 3)
        self.assertEqual(bst.Root.RightChild.LeftChild.RightChild.Level, 3)
        self.assertEqual(bst.Root.RightChild.RightChild.LeftChild.Level, 3)
        self.assertEqual(bst.Root.RightChild.RightChild.RightChild.Level, 3)

        self.assertEqual(bst.Root.LeftChild.LeftChild.LeftChild.Parent, bst.Root.LeftChild.LeftChild)
        self.assertEqual(bst.Root.LeftChild.LeftChild.RightChild.Parent, bst.Root.LeftChild.LeftChild)
        self.assertEqual(bst.Root.LeftChild.RightChild.LeftChild.Parent, bst.Root.LeftChild.RightChild)
        self.assertEqual(bst.Root.LeftChild.RightChild.RightChild.Parent, bst.Root.LeftChild.RightChild)
        self.assertEqual(bst.Root.RightChild.LeftChild.LeftChild.Parent, bst.Root.RightChild.LeftChild)
        self.assertEqual(bst.Root.RightChild.LeftChild.RightChild.Parent, bst.Root.RightChild.LeftChild)
        self.assertEqual(bst.Root.RightChild.RightChild.LeftChild.Parent, bst.Root.RightChild.RightChild)
        self.assertEqual(bst.Root.RightChild.RightChild.RightChild.Parent, bst.Root.RightChild.RightChild)

        self.assertIsNone(bst.Root.LeftChild.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.LeftChild.RightChild.RightChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.LeftChild.RightChild.RightChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.LeftChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.LeftChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.LeftChild.RightChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.LeftChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.LeftChild.RightChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.RightChild.LeftChild)
        self.assertIsNone(bst.Root.RightChild.RightChild.RightChild.RightChild)

    def test_IsBalanced(self):
        bst = BalancedBST()

        input = [1]
        bst.GenerateTree(input)
        self.assertTrue(bst.IsBalanced(bst.Root))

        input = [10, 5]

        #  5
        #   \
        #   10

        bst.GenerateTree(input)
        self.assertTrue(bst.IsBalanced(bst.Root))

        root = BSTNode(5, None)
        node_10 = BSTNode(10, root)
        node_6 = BSTNode(6, node_10)
        root.RightChild = node_10
        root.RightChild.RightChild = node_6
        root.Level = 0
        root.RightChild.Level = 1
        root.RightChild.RightChild.Level = 2

        #  5
        #   \
        #   10
        #     \
        #      6

        self.assertFalse(bst.IsBalanced(root))

        input = [10, 5, 9]

        #    9
        #   / \
        #  5  10

        bst.GenerateTree(input)
        self.assertTrue(bst.IsBalanced(bst.Root))

        input = [10, 5, 9, 8]

        #       9
        #      / \
        #     8  10
        #    /
        #   5

        bst.GenerateTree(input)
        self.assertTrue(bst.IsBalanced(bst.Root))

        root = BSTNode(5, None)
        node_10 = BSTNode(10, root)
        node_1 = BSTNode(1, root)
        node_4 = BSTNode(4, node_1)

        root.LeftChild = node_1
        root.RightChild = node_10
        root.LeftChild.RightChild = node_4

        root.Level = 0
        root.LeftChild.Level = 1
        root.RightChild.Level = 1
        root.LeftChild.RightChild.Level = 2

        #       5
        #      / \
        #     1   10
        #      \
        #       4

        self.assertTrue(bst.IsBalanced(root))

        node_3 = BSTNode(3, node_4)
        node_2 = BSTNode(2, node_3)

        root.LeftChild.RightChild.LeftChild = node_3
        root.LeftChild.RightChild.LeftChild.LeftChild = node_2
        root.LeftChild.RightChild.LeftChild.Level = 3
        root.LeftChild.RightChild.LeftChild.LeftChild.Level = 4

        #       5
        #      / \
        #     1   10
        #      \
        #       4
        #      /
        #     3
        #    /
        #   2

        self.assertFalse(bst.IsBalanced(root))

        node_6 = BSTNode(6, node_10)
        node_7 = BSTNode(7, node_6)
        node_8 = BSTNode(8, node_7)

        root.RightChild.LeftChild = node_6
        root.RightChild.LeftChild.RightChild = node_7
        root.RightChild.LeftChild.RightChild.RightChild = node_8

        root.RightChild.LeftChild.Level = 2
        root.RightChild.LeftChild.RightChild.Level = 3
        root.RightChild.LeftChild.RightChild.RightChild.Level = 4

        #        5
        #      /   \
        #     1     10
        #      \    /
        #       4  6
        #      /    \
        #     3      7
        #    /        \
        #   2          8

        self.assertFalse(bst.IsBalanced(root))
