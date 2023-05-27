import unittest
from simple_tree import SimpleTree, SimpleTreeNode

class TestSimpleTreeMethods(unittest.TestCase):
    def test_methods(self):
        # create tree
        root_node = SimpleTreeNode(0, None)
        tree = SimpleTree(root_node)
        self.assertEqual(tree.Root, root_node)
        self.assertIsNone(tree.Root.Parent)

        tree = SimpleTree(None)
        tree.AddChild(tree.Root, root_node)
        self.assertIsNone(tree.Root)
        self.assertIsNone(root_node.Parent)

        tree.Root = root_node

        self.assertEqual(tree.Root, root_node)
        self.assertEqual(root_node.level, 0)
        self.assertEqual(len(root_node.Children), 0)

        # add clildren (first level)
        node_1 = SimpleTreeNode(1, None)
        node_2 = SimpleTreeNode(2, None)
        node_3 = SimpleTreeNode(3, None)
        tree.AddChild(root_node, node_1)
        tree.AddChild(root_node, node_2)
        tree.AddChild(root_node, node_3)

        self.assertIsNone(tree.Root.Parent)
        self.assertEqual(len(tree.Root.Children), 3)
        self.assertEqual(node_1.Parent, root_node)
        self.assertEqual(node_2.Parent, root_node)
        self.assertEqual(node_3.Parent, root_node)
        self.assertIn(node_1, tree.Root.Children)
        self.assertIn(node_2, tree.Root.Children)
        self.assertIn(node_3, tree.Root.Children)
        self.assertEqual(node_1.level, 1)
        self.assertEqual(node_2.level, 1)
        self.assertEqual(node_3.level, 1)

        # add clildren (second level)
        node_4 = SimpleTreeNode(4, None)
        node_5 = SimpleTreeNode(5, None)
        tree.AddChild(node_1, node_4)
        tree.AddChild(node_2, node_5)

        self.assertEqual(len(node_1.Children), 1)
        self.assertEqual(len(node_2.Children), 1)
        self.assertEqual(node_4.Parent, node_1)
        self.assertEqual(node_5.Parent, node_2)
        self.assertIn(node_4, node_1.Children)
        self.assertIn(node_5, node_2.Children)
        self.assertEqual(node_4.level, 2)
        self.assertEqual(node_5.level, 2)

        # add clildren (third level)
        node_6 = SimpleTreeNode(6, None)
        tree.AddChild(node_4, node_6)

        self.assertIn(node_6, node_4.Children)
        self.assertEqual(node_6.Parent, node_4)
        self.assertEqual(node_6.level, 3)

        # add clildren (second level)
        node_7 = SimpleTreeNode(7, None)
        node_8 = SimpleTreeNode(8, None)
        tree.AddChild(node_3, node_7)
        tree.AddChild(node_3, node_8)

        self.assertEqual(len(node_3.Children), 2)
        self.assertEqual(node_7.Parent, node_3)
        self.assertEqual(node_8.Parent, node_3)
        self.assertIn(node_7, node_3.Children)
        self.assertIn(node_8, node_3.Children)
        self.assertEqual(node_7.level, 2)

        # root
        # | \ \
        # 1 2 3
        # | | | \
        # 4 5 7 8
        # |
        # 6

        self.assertEqual(tree.EvenTrees(), [])  # EvenTrees

        # DeleteNode
        parent = node_1.Parent
        tree.DeleteNode(node_1)
        self.assertNotIn(node_1, parent.Children)
        self.assertIsNone(node_1.Parent)

        tree.DeleteNode(tree.Root)
        self.assertIsNotNone(tree.Root)
        self.assertEqual(len(tree.Root.Children), 2)

        # root
        # | \
        # 2 3
        # | | \
        # 5 7 8

        self.assertEqual(tree.EvenTrees(), [root_node, node_2])  # EvenTrees

        # GetAllNodes
        nodes = tree.GetAllNodes()
        self.assertListEqual(nodes, [tree.Root, node_2, node_5, node_3, node_7, node_8])

        # FindNodesByValue
        node_9 = SimpleTreeNode(2, None)
        node_10 = SimpleTreeNode(2, None)
        node_11 = SimpleTreeNode(-1, None)
        tree.AddChild(node_8, node_9)
        tree.AddChild(node_5, node_10)
        tree.AddChild(node_5, node_11)

        # root
        # | \
        # 2 3
        # | | \
        # 5 7 8
        # | \ |
        # 2-1 2

        self.assertEqual(tree.EvenTrees(), [])  # EvenTrees

        nodes = tree.FindNodesByValue(2)
        self.assertListEqual(nodes, [node_2, node_10, node_9])

        nodes = tree.FindNodesByValue(8)
        self.assertListEqual(nodes, [node_8])

        nodes = tree.FindNodesByValue(0)
        self.assertListEqual(nodes, [tree.Root])

        nodes = tree.FindNodesByValue(-1)
        self.assertListEqual(nodes, [node_11])

        nodes = tree.FindNodesByValue(-10)
        self.assertListEqual(nodes, [])

        # MoveNode
        tree.MoveNode(node_5, tree.Root)
        self.assertNotIn(node_5, node_2.Children)
        self.assertIn(node_5, tree.Root.Children)
        self.assertEqual(node_5.Parent, tree.Root)
        self.assertEqual(node_5.level, 1)
        self.assertEqual(node_10.level, 2)
        self.assertEqual(node_11.level, 2)

        tree.MoveNode(node_8, node_11)
        self.assertNotIn(node_8, node_3.Children)
        self.assertIn(node_8, node_11.Children)
        self.assertEqual(node_8.Parent, node_11)
        self.assertEqual(node_8.level, 3)
        self.assertEqual(node_9.level, 4)

        # root
        # | \ \
        # 2 3 5
        #   | | \
        #   7 2 -1
        #        |
        #        8
        #        |
        #        2

        # Count
        self.assertEqual(tree.Count(), 9)

        # LeafCount
        self.assertEqual(tree.LeafCount(), 4)

        # EvenTrees
        self.assertEqual(tree.EvenTrees(), [])

        root_node = SimpleTreeNode(1, None)
        tree = SimpleTree(root_node)

        node_2 = SimpleTreeNode(2, None)
        node_3 = SimpleTreeNode(3, None)
        node_4 = SimpleTreeNode(4, None)
        node_5 = SimpleTreeNode(5, None)
        node_6 = SimpleTreeNode(6, None)
        node_7 = SimpleTreeNode(7, None)
        node_8 = SimpleTreeNode(8, None)
        node_9 = SimpleTreeNode(9, None)
        node_10 = SimpleTreeNode(10, None)

        tree.AddChild(root_node, node_2)
        tree.AddChild(root_node, node_3)
        tree.AddChild(root_node, node_6)
        tree.AddChild(node_2, node_5)
        tree.AddChild(node_2, node_7)
        tree.AddChild(node_3, node_4)
        tree.AddChild(node_6, node_8)
        tree.AddChild(node_8, node_9)
        tree.AddChild(node_8, node_10)

        # root
        # |  \ \
        # 2   3 6
        # |\  | |
        # 5 7 4 8
        #       |\
        #       9 10

        self.assertEqual(tree.EvenTrees(), [root_node, node_3, root_node, node_6])
