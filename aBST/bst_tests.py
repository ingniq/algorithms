import unittest
from bst import aBST


class TestBSTMethods(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        self.bst = None
        super().__init__(methodName)

    def test_create_tree(self):
        bst = aBST(0)
        self.assertEqual(len(bst.Tree), 1)
        bst = aBST(1)
        self.assertEqual(len(bst.Tree), 3)
        bst = aBST(2)
        self.assertEqual(len(bst.Tree), 7)
        bst = aBST(3)
        self.assertEqual(len(bst.Tree), 15)

    def __create_default_BST(self):
        self.bst = aBST(3)
        self.bst.AddKey(50)
        self.bst.AddKey(25)
        self.bst.AddKey(75)
        self.bst.AddKey(37)
        self.bst.AddKey(62)
        self.bst.AddKey(84)
        self.bst.AddKey(31)
        self.bst.AddKey(43)
        self.bst.AddKey(55)
        self.bst.AddKey(92)

        #         50
        #       /    \
        #     25      75
        #      \     /  \
        #      37   62  84
        #     / \   /    \
        #   31  43 55    92

    def test_FindKeyIndex(self):
        self.bst = aBST(3)

        # not found (empty tree)
        self.assertEqual(self.bst.FindKeyIndex(50), 0)
        self.assertEqual(self.bst.FindKeyIndex(20), 0)
        self.assertEqual(self.bst.FindKeyIndex(25), 0)

        self.__create_default_BST()

        # not found (empty slot)
        self.assertEqual(self.bst.FindKeyIndex(20), -3)
        self.assertEqual(self.bst.FindKeyIndex(83), -13)

        # found
        self.assertEqual(self.bst.FindKeyIndex(50), 0)
        self.assertEqual(self.bst.FindKeyIndex(25), 1)
        self.assertEqual(self.bst.FindKeyIndex(75), 2)
        self.assertEqual(self.bst.FindKeyIndex(37), 4)
        self.assertEqual(self.bst.FindKeyIndex(62), 5)
        self.assertEqual(self.bst.FindKeyIndex(84), 6)
        self.assertEqual(self.bst.FindKeyIndex(31), 9)
        self.assertEqual(self.bst.FindKeyIndex(43), 10)
        self.assertEqual(self.bst.FindKeyIndex(55), 11)
        self.assertEqual(self.bst.FindKeyIndex(92), 14)

        # not found (out of range)
        self.assertEqual(self.bst.FindKeyIndex(93), None)

    def test_AddKey(self):
        self.__create_default_BST()

        self.assertEqual(self.bst.Tree[0], 50)
        self.assertEqual(self.bst.Tree[1], 25)
        self.assertEqual(self.bst.Tree[2], 75)
        self.assertEqual(self.bst.Tree[4], 37)
        self.assertEqual(self.bst.Tree[5], 62)
        self.assertEqual(self.bst.Tree[6], 84)
        self.assertEqual(self.bst.Tree[9], 31)
        self.assertEqual(self.bst.Tree[10], 43)
        self.assertEqual(self.bst.Tree[11], 55)
        self.assertEqual(self.bst.Tree[14], 92)

        # isset
        self.assertEqual(self.bst.AddKey(50), 0)
        self.assertEqual(self.bst.AddKey(62), 5)

        # not isset
        self.assertEqual(self.bst.AddKey(-5), 3)
        self.assertEqual(self.bst.AddKey(-10), 7)
        self.assertEqual(self.bst.AddKey(-1), 8)
        self.assertEqual(self.bst.AddKey(64), 12)
        self.assertEqual(self.bst.AddKey(80), 13)

        # not added
        self.assertEqual(self.bst.AddKey(94), -1)

        #             50
        #           /    \
        #         25      75
        #        /  \     /  \
        #      -5   37   62   84
        #     /|   / \   / \  | \
        #  -10 -1 31 43 55 64 80 92

        self.assertEqual(self.bst.Tree[3], -5)
        self.assertEqual(self.bst.Tree[7], -10)
        self.assertEqual(self.bst.Tree[8], -1)
        self.assertEqual(self.bst.Tree[12], 64)
        self.assertEqual(self.bst.Tree[13], 80)
