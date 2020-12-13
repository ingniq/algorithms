import unittest
from nc import NativeCache
from random import randrange


class TestNativeCacheMethods(unittest.TestCase):
    def test_put(self):
        size = 1000
        nc = NativeCache(size)

        nc.put("string", str(randrange(size)))
        index = nc.find("string")
        self.assertEqual(663, index)
        # указатель на элемент с минимальным кол-м обращений не изменяется
        self.assertEqual(0, nc._min_hits[0])
        self.assertEqual(0, nc.hits[nc._min_hits[0]])

        # колллизия
        nc.put("gnirts", str(randrange(size)))
        index = nc.find("gnirts")
        self.assertEqual(664, index)
        # указатель на элемент с минимальным кол-м обращений не изменяется
        self.assertEqual(0, nc._min_hits[0])
        self.assertEqual(0, nc.hits[nc._min_hits[0]])

        nc.put("string1", str(randrange(size)))
        index = nc.find("string1")
        self.assertEqual(712, index)
        # указатель на элемент с минимальным кол-м обращений не изменяется
        self.assertEqual(0, nc._min_hits[0])
        self.assertEqual(0, nc.hits[nc._min_hits[0]])

        nc.put("string2", str(randrange(size)))
        index = nc.find("string2")
        self.assertEqual(713, index)
        # указатель на элемент с минимальным кол-м обращений не изменяется
        self.assertEqual(0, nc._min_hits[0])
        self.assertEqual(0, nc.hits[nc._min_hits[0]])

        # колллизия
        nc.put("string3", str(randrange(size)))
        index = nc.find("string3")
        self.assertEqual(714, index)
        # указатель на элемент с минимальным кол-м обращений не изменяется
        self.assertEqual(0, nc._min_hits[0])
        self.assertEqual(0, nc.hits[nc._min_hits[0]])

        # обновление значения для существующего ключа
        nc.put("string3", "string31")
        index = nc.find("string3")

        self.assertEqual(0, nc.hits[index])
        value = nc.get("string3")
        self.assertEqual(714, index)
        self.assertEqual("string31", value)
        # указатель на элемент с минимальным кол-м обращений не изменяется
        self.assertEqual(0, nc._min_hits[0])
        self.assertEqual(0, nc.hits[nc._min_hits[0]])
        # кол-во обращений к текущему элементу увеличилось на 1
        self.assertEqual(1, nc.hits[index])

        n = 15
        while n:
            nc.get("string3")
            n -= 1

        # кол-во обращений к текущему элементу увеличилось на 15
        self.assertEqual(16, nc.hits[index])

    def test_get(self):
        size = 1000
        nc = NativeCache(size)

        values = {
            "string": "value 1",
            "gnirts": "value 2",
            "string1": "value 3",
            "string2": "value 4",
            "string3": "value 5"
        }

        for i in values:
            nc.put(i, values[i])

        # без коллизий
        value = nc.get("string")
        self.assertEqual("value 1", value)
        value = nc.get("string1")
        self.assertEqual("value 3", value)
        value = nc.get("string2")
        self.assertEqual("value 4", value)

        # с учетом коллизий
        value = nc.get("gnirts")
        self.assertEqual("value 2", value)
        value = nc.get("string3")
        self.assertEqual("value 5", value)

        # отсутствует
        value = nc.get("string 3")
        self.assertIsNone(value)

        # не строка
        value = 123
        value = nc.get(value)
        self.assertIsNone(value)

    def test_remove(self):
        size = 1000
        nc = NativeCache(size)

        keys = [
            "string",
            "gnirts",
            "string1",
            "string2",
            "string3"
            ]

        # удаление из пустого кэша
        self.assertIsNone(nc.remove(keys[0]))

        for v in keys:
            nc.put(v, str(randrange(size)))

        # удаление несуществующего элемента
        self.assertIsNone(nc.remove("923425"))

        # кол-во обращений к текущему элементу 0
        index = nc.find("string")
        self.assertEqual(663, index)
        self.assertEqual(0, nc.hits[index])

        n = 10
        while n:
            nc.get("string")
            n -= 1

        # кол-во обращений к текущему элементу увеличилось на 10
        self.assertEqual(10, nc.hits[index])

        nc.remove(keys[0])
        # кол-во обращений по текущему индексу обнулилось
        self.assertEqual(0, nc.hits[index])

        index = nc.find("string")
        self.assertIsNone(index)

    def test_hits(self):
        debug = NativeCacheDebugger()
        size = 1000
        nc = NativeCache(size)

        # заполнение кэша
        n = size
        while n:
            nc.put("string" + str(n), "string" + str(n))
            n -= 1

        self.assertEqual(1000, nc.len())

        # Эмуляция обращений к элементам
        n = 10000
        while n:
            nc.get("string" + str(randrange(size + 1)))
            n -= 1

        # Добавление элемента если массив заполнен. Вытеснение и обнуление кол-ва запросов для этого элемента
        index = nc._min_hits[0]
        nc.put("testing", "testing")
        new_item_index = nc.find("testing")
        self.assertTrue(index == new_item_index)
        self.assertTrue(nc.hits[index] == 0)

        # Удаление элемента и обнуление кол-ва запросов для этого элемента
        index = nc._min_hits[0]
        nc.remove("testing")
        new_item_index = nc.find("testing")
        self.assertIsNone(new_item_index)
        self.assertTrue(nc.hits[index] == 0)

        # Сбор статистики: количество операций поиска, коллизий.
        debug.collisions = nc.collisions
        print("Number of collisions:", debug.collisions)  # 954

        i = 100
        while i:
            size = 1000
            nc = NativeCache(size)

            # заполнение кэша
            n = size
            while n:
                nc.put("string" + str(n), "string" + str(n))
                n -= 1

            self.assertEqual(1000, nc.len())

            # Эмуляция обращений к элементам
            n = 10000
            while n:
                nc.get("string" + str(randrange(size)))
                n -= 1

            debug.number_of_finds.append(nc.debug)
            i -= 1

            # Проверка корректности выбора минимального значения.
            n = nc.hits[nc._min_hits[0]] - 1
            if n > 0:
                while n:
                    self.assertFalse(n in nc.hits)
                    n -= 1

        print("Number of find operations:", debug.number_of_finds)  # min -- 9, max -- 27, avg -- 15


class NativeCacheDebugger:
    def __init__(self):
        self.number_of_finds = []
        self.collisions = 0
