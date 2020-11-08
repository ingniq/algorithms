import unittest
from nd import NativeDictionary
from random import randrange


class TestNativeDictionaryMethods(unittest.TestCase):
    def test_hash_fun(self):
        size = 17
        nd = NativeDictionary(size)

        value = "string 123"
        index = nd.hash_fun(value)
        self.assertEqual(12, index)

        # коллизия
        value = "321 gnirts"
        index = nd.hash_fun(value)
        self.assertEqual(12, index)

        # не строка
        value = 123
        index = nd.hash_fun(value)
        self.assertIsNone(index)

        # не строка
        value = [123]
        index = nd.hash_fun(value)
        self.assertIsNone(index)

    def test_seek_slot(self):
        size = 17
        nd = NativeDictionary(size)

        keys = [
            "string",
            "gnirts",
            "string1",
            "string2",
            "string3"
            ]

        for v in keys:
            nd.put(v, v + " " + str(randrange(nd.size)))

        # без коллизий
        index = nd.seek_slot("string4")
        self.assertEqual(3, index)

        # с учетом коллизий
        index = nd.seek_slot(keys[0])
        self.assertEqual(3, index)
        index = nd.seek_slot(keys[1])
        self.assertEqual(3, index)
        index = nd.seek_slot(keys[2])
        self.assertEqual(3, index)
        index = nd.seek_slot(keys[3])
        self.assertEqual(3, index)
        index = nd.seek_slot(keys[4])
        self.assertEqual(3, index)

        nd.put("string15", "string15 Test")

        index = nd.seek_slot(keys[0])
        self.assertEqual(4, index)
        index = nd.seek_slot(keys[1])
        self.assertEqual(4, index)
        index = nd.seek_slot(keys[4])
        self.assertEqual(4, index)

        # не строка
        value = 123
        index = nd.seek_slot(value)
        self.assertIsNone(index)

    def test_put(self):
        size = 17
        nd = NativeDictionary(size)

        nd.put("string", str(randrange(nd.size)))
        index = nd.find("string")
        self.assertEqual(0, index)
        # колллизия
        nd.put("gnirts", str(randrange(nd.size)))
        index = nd.find("gnirts")
        self.assertEqual(1, index)
        nd.put("string1", str(randrange(nd.size)))
        index = nd.find("string1")
        self.assertEqual(15, index)
        nd.put("string2", str(randrange(nd.size)))
        index = nd.find("string2")
        self.assertEqual(16, index)
        # колллизия
        nd.put("string3", str(randrange(nd.size)))
        index = nd.find("string3")
        self.assertEqual(2, index)

        # не строка
        value = 123
        nd.put(value, str(randrange(nd.size)))
        index = nd.find(value)
        self.assertIsNone(index)

        # обновление значения для существующего ключа
        nd.put("string3", "string3")
        index = nd.find("string3")
        value = nd.get("string3")
        self.assertEqual(2, index)
        self.assertEqual("string3", value)

    def test_get(self):
        size = 17
        nd = NativeDictionary(size)

        values = {
            "string": "value 1",
            "gnirts": "value 2",
            "string1": "value 3",
            "string2": "value 4",
            "string3": "value 5"
        }

        for i in values:
            nd.put(i, values[i])

        # без коллизий
        value = nd.get("string")
        self.assertEqual("value 1", value)
        value = nd.get("string1")
        self.assertEqual("value 3", value)
        value = nd.get("string2")
        self.assertEqual("value 4", value)

        # с учетом коллизий
        value = nd.get("gnirts")
        self.assertEqual("value 2", value)
        value = nd.get("string3")
        self.assertEqual("value 5", value)

        # отсутствует
        value = nd.get("string 3")
        self.assertIsNone(value)

        # не строка
        value = 123
        value = nd.get(value)
        self.assertIsNone(value)

    def test_find(self):
        size = 17
        nd = NativeDictionary(size)

        keys = [
            "string",
            "gnirts",
            "string1",
            "string2",
            "string3"
            ]

        for v in keys:
            nd.put(v, str(randrange(nd.size)))

        # без коллизий
        index = nd.find(keys[0])
        self.assertEqual(0, index)
        index = nd.find(keys[2])
        self.assertEqual(15, index)
        index = nd.find(keys[3])
        self.assertEqual(16, index)

        # с учетом коллизий
        index = nd.find(keys[1])
        self.assertEqual(1, index)
        index = nd.find(keys[4])
        self.assertEqual(2, index)

        # не строка
        value = 123
        index = nd.find(value)
        self.assertIsNone(index)

    def test_is_key(self):
        size = 17
        nd = NativeDictionary(size)

        keys = [
            "string",
            "gnirts",
            "string1",
            "string2",
            "string3",
            "string 3"
            ]

        for v in keys:
            nd.put(v, str(randrange(nd.size)))

        # без коллизий
        self.assertTrue(nd.is_key(keys[0]))
        self.assertTrue(nd.is_key(keys[2]))
        self.assertTrue(nd.is_key(keys[3]))
        self.assertTrue(nd.is_key(keys[5]))

        nd.slots[5] = "string 23"
        self.assertTrue(nd.is_key("string 23"))

        # с учетом коллизий
        self.assertTrue(nd.is_key(keys[1]))
        self.assertTrue(nd.is_key(keys[4]))

        # отсутствует
        self.assertFalse(nd.is_key("test string"))

        # key не строка
        self.assertFalse(nd.is_key(123))

        # value не строка
        nd = NativeDictionary(17)
        s = "0123456789"
        nd.put(s, 123456789)
        self.assertTrue(nd.is_key(s))
