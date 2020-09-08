import unittest
from stack import Stack
from brackets import brackets_are_balanced


class TestStackMethods(unittest.TestCase):
    def test_methods(self):
        stack = Stack()
        # test push
        stack.push(1)
        # test peek
        self.assertEqual(stack.peek(), 1)
        # test size
        self.assertEqual(stack.size(), 1)

        stack.push("2")
        self.assertEqual(stack.peek(), "2")
        self.assertEqual(stack.size(), 2)

        stack.push(3.14)
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 3.14)

        # test pop
        self.assertEqual(stack.pop(), 3.14)
        self.assertEqual(stack.peek(), "2")
        self.assertEqual(stack.size(), 2)

        self.assertEqual(stack.pop(), "2")
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.size(), 1)

        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.size(), 0)

    def test_brackets(self):
        result = brackets_are_balanced("(()((())()))")
        self.assertTrue(result)

        result = brackets_are_balanced("(()()(()")
        self.assertFalse(result)
        result = brackets_are_balanced("())(")
        self.assertFalse(result)
        result = brackets_are_balanced("))((")
        self.assertFalse(result)
        result = brackets_are_balanced("((())")
        self.assertFalse(result)
        result = brackets_are_balanced("((((((())")
        self.assertFalse(result)
        result = brackets_are_balanced("((())))")
        self.assertFalse(result)
        result = brackets_are_balanced("((()))))))")
        self.assertFalse(result)
