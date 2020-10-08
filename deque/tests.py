import unittest
from deque import Deque


class TestDequeMethods(unittest.TestCase):
    def test_deque(self):
        deq = Deque()
        test_values = [0, 1, "2", 3.14]
        count_test_values = len(test_values)

        # add in head
        new_size = deq.size()
        for val in test_values:
            deq.addFront(val)
            new_size += 1

            self.assertEqual(deq.size(), new_size)
            self.assertEqual(deq.queue[deq.HEAD_INDEX], val)  # head
            self.assertEqual(deq.queue[new_size - 1], test_values[0])  # tail

            if new_size == 1:
                self.assertEqual(deq.queue[new_size - 1], deq.queue[deq.HEAD_INDEX])

        # add in tail
        new_size = deq.size()
        head_value = deq.queue[deq.HEAD_INDEX]

        for val in test_values:
            deq.addTail(val)
            new_size += 1

            self.assertEqual(deq.size(), new_size)
            self.assertEqual(deq.queue[deq.HEAD_INDEX], head_value)  # head
            self.assertEqual(deq.queue[new_size - 1], val)  # tail

            if new_size == count_test_values * 2:
                self.assertEqual(deq.queue[new_size - 1], deq.queue[deq.HEAD_INDEX])

        # remove front
        test_values.reverse()
        new_size = deq.size()
        tail_value = deq.queue[deq.size() - 1]

        for i in range(count_test_values):
            self.assertEqual(deq.queue[deq.HEAD_INDEX], test_values[i])  # head

            deq.removeFront()
            new_size -= 1

            self.assertEqual(deq.size(), new_size)
            self.assertEqual(deq.queue[new_size - 1], tail_value)  # tail

            if i != count_test_values - 1:
                self.assertEqual(deq.queue[deq.HEAD_INDEX], test_values[i + 1])  # head
            else:
                self.assertEqual(deq.queue[deq.HEAD_INDEX], test_values[i])  # head

        # remove tail
        new_size = deq.size()
        head_value = deq.queue[deq.HEAD_INDEX]

        for i in range(count_test_values):
            new_size -= 1
            self.assertEqual(deq.queue[new_size], test_values[i])  # head

            deq.removeTail()
            self.assertEqual(deq.size(), new_size)

            if new_size == 0:
                break

            if new_size == 1:
                self.assertEqual(deq.queue[new_size - 1], deq.queue[deq.HEAD_INDEX])  # tail
            else:
                self.assertEqual(deq.queue[new_size - 1], test_values[i + 1])  # tail

            self.assertEqual(deq.queue[deq.HEAD_INDEX], head_value)  # head

        # удаление из пустой очереди
        deq.removeTail()
        self.assertEqual(deq.size(), 0)
        deq.removeFront()
        self.assertEqual(deq.size(), 0)

        # вставка в хвост в пустую очередь
        deq.addTail(0) 
        self.assertEqual(deq.size(), 1)
        self.assertEqual(deq.queue[deq.HEAD_INDEX], 0)  # head
        self.assertEqual(deq.queue[deq.size() - 1], 0)
        self.assertEqual(deq.queue[deq.size() - 1], deq.queue[deq.HEAD_INDEX])

        # удаление последнего элемента из головы
        deq.removeFront()
        self.assertEqual(deq.size(), 0)
