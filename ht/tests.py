import unittest
from ht import HashTable


class TestHashTableMethods(unittest.TestCase):
    def test_hash_fun(self):
        size = 17
        step = 3
        ht = HashTable(size, step)

        value = "string123"
        index = ht.hash_fun(value)
        self.assertEqual(14, index)

        # коллизия
        value = "321gnirts"
        index = ht.hash_fun(value)
        self.assertEqual(14, index)

        # не строка
        value = 123
        index = ht.hash_fun(value)
        self.assertIsNone(index)

        # не строка
        value = [123]
        index = ht.hash_fun(value)
        self.assertIsNone(index)

    def test_seek_slot(self):
        size = 17
        step = 3
        ht = HashTable(size, step)

        values = [
            "string",
            "gnirts",
            "string1",
            "string2",
            "string3"
            ]

        for v in values:
            ht.put(v)

        # без коллизий
        index = ht.seek_slot("string4")
        self.assertEqual(1, index)

        # с учетом коллизий
        index = ht.seek_slot(values[0])
        self.assertEqual(9, index)
        index = ht.seek_slot(values[1])
        self.assertEqual(9, index)
        index = ht.seek_slot(values[2])
        self.assertEqual(1, index)
        index = ht.seek_slot(values[3])
        self.assertEqual(2, index)
        index = ht.seek_slot(values[4])
        self.assertEqual(9, index)

        ht.put("string15")

        index = ht.seek_slot(values[0])
        self.assertEqual(12, index)
        index = ht.seek_slot(values[1])
        self.assertEqual(12, index)
        index = ht.seek_slot(values[4])
        self.assertEqual(12, index)

        # не строка
        value = 123
        index = ht.seek_slot(value)
        self.assertIsNone(index)

    def test_put(self):
        size = 17
        step = 3
        ht = HashTable(size, step)

        index = ht.put("string")
        self.assertEqual(0, index)
        # колллизия
        index = ht.put("gnirts")
        self.assertEqual(3, index)
        index = ht.put("string1")
        self.assertEqual(15, index)
        index = ht.put("string2")
        self.assertEqual(16, index)
        # колллизия
        index = ht.put("string3")
        self.assertEqual(6, index)

        # не строка
        value = 123
        index = ht.put(value)
        self.assertIsNone(index)

    def test_find(self):
        size = 17
        step = 3
        ht = HashTable(size, step)

        values = [
            "string",
            "gnirts",
            "string1",
            "string2",
            "string3"
            ]

        for v in values:
            ht.put(v)

        # без коллизий
        index = ht.find(values[0])
        self.assertEqual(0, index)
        index = ht.find(values[2])
        self.assertEqual(15, index)
        index = ht.find(values[3])
        self.assertEqual(16, index)

        # с учетом коллизий
        index = ht.find(values[1])
        self.assertEqual(3, index)
        index = ht.find(values[4])
        self.assertEqual(6, index)

        # не строка
        value = 123
        index = ht.find(value)
        self.assertIsNone(index)
