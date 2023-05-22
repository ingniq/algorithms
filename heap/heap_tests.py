from unittest import TestCase
from Heap import Heap


class TestHeap(TestCase):

    def test_MakeHeap(self):
        heap = Heap()
        self.assertListEqual(heap.HeapArray, [])

        input = []
        expected = [None]
        depth = 0
        heap.MakeHeap(input, depth)
        self.assertEqual(len(heap.HeapArray), 2 ** (depth + 1) - 1)
        self.assertListEqual(heap.HeapArray, expected)

        input = []
        expected = [None, None, None]
        depth = 1
        heap.MakeHeap(input, depth)
        self.assertEqual(len(heap.HeapArray), 2 ** (depth + 1) - 1)
        self.assertListEqual(heap.HeapArray, expected)

        input = []
        expected = [None, None, None, None, None, None, None]
        depth = 2
        heap.MakeHeap(input, depth)
        self.assertEqual(len(heap.HeapArray), 2 ** (depth + 1) - 1)
        self.assertListEqual(heap.HeapArray, expected)

        input = [7, 8, 3, 11, 5, 1, 6, 4, 2, 9]
        expected = [11, 9, 6, 7, 8, 1, 3, 4, 2, 5, None, None, None]
        depth = 3
        heap.MakeHeap(input, depth)
        self.assertEqual(len(heap.HeapArray), 2 ** (depth + 1) - 1)

        #          11
        #        /    \
        #       9      6
        #     /   \   /  \
        #    7     8 1    3
        #   / \   /
        #  4   2 5

        self.assertListEqual(heap.HeapArray, expected)

    def test_GetMax(self):
        heap = Heap()
        self.assertEqual(heap.GetMax(), -1)
        heap.MakeHeap([], 3)
        self.assertEqual(heap.GetMax(), -1)

        input = [1, 3, 6, 7, 4, 2, 9, 11, 5, 8, 1, 2, 3, 4, 5]
        heap.MakeHeap(input, 3)
        expected = [11, 9, 7, 6, 8, 3, 5, 1, 5, 4, 1, 2, 2, 3, 4]
        self.assertListEqual(heap.HeapArray, expected)

        #         11
        #        / \
        #       9   7
        #     /  | |  \
        #    6   8 3   5
        #   /|  /| |\  |\
        #  1 5 4 1 2 2 3 4

        self.assertEqual(heap.GetMax(), 11)
        expected = [9, 8, 7, 6, 4, 3, 5, 1, 5, 4, 1, 2, 2, 3, None]
        self.assertListEqual(heap.HeapArray, expected)

        #         9
        #        / \
        #       8   7
        #     /  | |  \
        #    6   4 3   5
        #   /|  /| |\  |
        #  1 5 4 1 2 2 3

        self.assertEqual(heap.GetMax(), 9)
        expected = [8, 6, 7, 5, 4, 3, 5, 1, 3, 4, 1, 2, 2, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #         8
        #        / \
        #       6   7
        #     /  | |  \
        #    5   4 3   5
        #   /|  /| |\
        #  1 3 4 1 2 2

        self.assertEqual(heap.GetMax(), 8)
        expected = [7, 6, 5, 5, 4, 3, 2, 1, 3, 4, 1, 2, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #         7
        #        / \
        #       6   5
        #     /  | |  \
        #    5   4 3   2
        #   /|  /| |
        #  1 3 4 1 2

        self.assertEqual(heap.GetMax(), 7)
        expected = [6, 5, 5, 3, 4, 3, 2, 1, 2, 4, 1, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #         6
        #        / \
        #       5   5
        #     /  | |  \
        #    3   4 3   2
        #   /|  /|
        #  1 2 4 1

        self.assertEqual(heap.GetMax(), 6)
        expected = [5, 4, 5, 3, 4, 3, 2, 1, 2, 1, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #         5
        #        / \
        #       4   5
        #     / |  / \
        #    3  4 3   2
        #   /|  /
        #  1 2 1

        self.assertEqual(heap.GetMax(), 5)
        expected = [5, 4, 3, 3, 4, 1, 2, 1, 2, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #         5
        #        / \
        #       4   3
        #     / |  / \
        #    3  4 1   2
        #   /|
        #  1 2

        self.assertEqual(heap.GetMax(), 5)
        expected = [4, 4, 3, 3, 2, 1, 2, 1, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #         4
        #        / \
        #       4   3
        #     / |  / \
        #    3  2 1   2
        #   /
        #  1

        self.assertEqual(heap.GetMax(), 4)
        expected = [4, 3, 3, 1, 2, 1, 2, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #         4
        #        / \
        #       3   3
        #     / |  / \
        #    1  2 1   2

        self.assertEqual(heap.GetMax(), 4)
        expected = [3, 2, 3, 1, 2, 1, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #         3
        #        / \
        #       2   3
        #     / |  /
        #    1  2 1

        self.assertEqual(heap.GetMax(), 3)
        expected = [3, 2, 1, 1, 2, None, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #         3
        #        / \
        #       2   1
        #     / |
        #    1  2

        self.assertEqual(heap.GetMax(), 3)
        expected = [2, 2, 1, 2, None, None, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #        2
        #       / \
        #      2   1
        #     /
        #    2

        self.assertEqual(heap.GetMax(), 2)
        expected = [2, 2, 1, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #        2
        #       / \
        #      2   1

        self.assertEqual(heap.GetMax(), 2)
        expected = [2, 1, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #        2
        #       /
        #      1

        self.assertEqual(heap.GetMax(), 2)
        expected = [1, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        #      1

        self.assertEqual(heap.GetMax(), 1)
        expected = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertEqual(heap.GetMax(), -1)

    def test_Add(self):
        heap = Heap()
        heap.MakeHeap([], 3)

        self.assertTrue(heap.Add(1))
        expected = [1, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(3))
        expected = [3, 1, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(6))
        expected = [6, 1, 3, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(7))
        expected = [7, 6, 3, 1, None, None, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(4))
        expected = [7, 6, 3, 1, 4, None, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(2))
        expected = [7, 6, 3, 1, 4, 2, None, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(9))
        expected = [9, 6, 7, 1, 4, 2, 3, None, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(11))
        expected = [11, 9, 7, 6, 4, 2, 3, 1, None, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(5))
        expected = [11, 9, 7, 6, 4, 2, 3, 1, 5, None, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(8))
        expected = [11, 9, 7, 6, 8, 2, 3, 1, 5, 4, None, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(1))
        expected = [11, 9, 7, 6, 8, 2, 3, 1, 5, 4, 1, None, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(2))
        expected = [11, 9, 7, 6, 8, 2, 3, 1, 5, 4, 1, 2, None, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(3))
        expected = [11, 9, 7, 6, 8, 3, 3, 1, 5, 4, 1, 2, 2, None, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(4))
        expected = [11, 9, 7, 6, 8, 3, 4, 1, 5, 4, 1, 2, 2, 3, None]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertTrue(heap.Add(5))
        expected = [11, 9, 7, 6, 8, 3, 5, 1, 5, 4, 1, 2, 2, 3, 4]
        self.assertListEqual(heap.HeapArray, expected)

        self.assertFalse(heap.Add(40))
        expected = [11, 9, 7, 6, 8, 3, 5, 1, 5, 4, 1, 2, 2, 3, 4]
        self.assertListEqual(heap.HeapArray, expected)

        #         11
        #        / \
        #       9   7
        #     /  | |  \
        #    6   8 3   5
        #   /|  /| |\  |\
        #  1 5 4 1 2 2 3 4
