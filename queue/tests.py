import unittest
from queue_lesson import Queue


class TestQueueMethods(unittest.TestCase):
    def test_queue(self):
        queue = Queue()

        # test enqueue
        queue.enqueue(1)
        self.assertEqual(queue.queue.head.value, 1)
        self.assertEqual(queue.queue.tail.value, 1)
        self.assertEqual(queue.queue.tail.prev, None)
        self.assertEqual(queue.queue.tail.next, None)
        # test size
        self.assertEqual(queue.size(), 1)

        queue.enqueue("2")
        self.assertEqual(queue.queue.head.value, 1)
        self.assertEqual(queue.queue.tail.value, "2")
        self.assertEqual(queue.queue.tail.prev.value, 1)
        self.assertEqual(queue.queue.tail.next, None)
        self.assertEqual(queue.size(), 2)

        queue.enqueue(3.14)
        self.assertEqual(queue.queue.head.value, 1)
        self.assertEqual(queue.queue.tail.value, 3.14)
        self.assertEqual(queue.queue.tail.prev.value, "2")
        self.assertEqual(queue.queue.tail.prev.prev.value, 1)
        self.assertEqual(queue.size(), 3)

        # test dequeue
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.queue.head.value, "2")
        self.assertEqual(queue.queue.tail.value, 3.14)
        self.assertEqual(queue.queue.tail.prev.value, "2")
        self.assertEqual(queue.size(), 2)

        # one element remains
        self.assertEqual(queue.dequeue(), "2")
        self.assertEqual(queue.queue.head.value, 3.14)
        self.assertEqual(queue.queue.tail.value, 3.14)
        self.assertEqual(queue.queue.tail.prev, None)
        self.assertEqual(queue.size(), 1)

        # the queue is being emptied
        self.assertEqual(queue.dequeue(), 3.14)
        self.assertEqual(queue.queue.head, None)
        self.assertEqual(queue.queue.tail, None)
        self.assertEqual(queue.size(), 0)

        # dequeue from empty
        self.assertEqual(queue.dequeue(), None)
        self.assertEqual(queue.queue.head, None)
        self.assertEqual(queue.queue.tail, None)
        # test size empty queue
        self.assertEqual(queue.size(), 0)
