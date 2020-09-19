import unittest
from queue_lesson import Queue
from func import rotate


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

    def test_rotate(self):
        q = Queue()

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(6)

        self.assertEqual(q.queue.head.value, 1)
        self.assertEqual(q.queue.tail.value, 6)

        rotate(q, 3)

        self.assertEqual(q.queue.head.value, 4)
        self.assertEqual(q.queue.tail.value, 3)

        rotate(q, 0)

        self.assertEqual(q.queue.head.value, 4)
        self.assertEqual(q.queue.tail.value, 3)

        rotate(q, -3)

        self.assertEqual(q.queue.head.value, 4)
        self.assertEqual(q.queue.tail.value, 3)

        rotate(q, 6)

        self.assertEqual(q.queue.head.value, 4)
        self.assertEqual(q.queue.tail.value, 3)

        rotate(q, 7)

        self.assertEqual(q.queue.head.value, 5)
        self.assertEqual(q.queue.tail.value, 4)

        rotate(q, 17)

        self.assertEqual(q.queue.head.value, 4)
        self.assertEqual(q.queue.tail.value, 3)

        with self.assertRaisesRegex(ValueError, '^The second argument must be of the integer type.$'):
            rotate(q, "17")

        with self.assertRaisesRegex(ValueError, '^The first argument must be of the Queue type.$'):
            rotate(q.queue, "17")
