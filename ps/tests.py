import unittest
from ps import PowerSet


class TestPowerSetMethods(unittest.TestCase):
    def test_size(self):
        VALUES = [
            "test1",
            "test2",
            "",
        ]

        ps = PowerSet()
        self.assertEqual(ps.size(), 0)

        ps.put(VALUES[0])
        self.assertEqual(ps.size(), 1)

        ps.put(VALUES[1])
        self.assertEqual(ps.size(), 2)

        ps.put(VALUES[2])
        self.assertEqual(ps.size(), 3)

        for n in range(3, 12):
            ps.put("test" + str(n))

        self.assertEqual(ps.size(), 12)

    def test_put(self):
        VALUES = [
            "test1",
            "test2",
            "test1",
            "",
        ]
        ps = PowerSet()
        self.assertEqual(ps.size(), 0)

        # добавление отсутствующего элемента
        ps.put(VALUES[0])
        ps.put(VALUES[1])
        ps.put(VALUES[3])
        self.assertEqual(ps.size(), 3)

        # добавление присутствующего элемента
        ps.put(VALUES[2])
        self.assertEqual(ps.size(), 3)
        ps.put(VALUES[3])
        self.assertEqual(ps.size(), 3)

    def test_get(self):
        VALUES = [
            "test1",
            "test2",
            "",
        ]
        ps = PowerSet()

        ps.put(VALUES[0])
        ps.put(VALUES[1])
        ps.put(VALUES[2])

        # существующие элементы
        self.assertTrue(ps.get(VALUES[0]))
        self.assertTrue(ps.get(VALUES[1]))
        self.assertTrue(ps.get(VALUES[2]))

        index = ps.find(VALUES[0])
        self.assertIn(VALUES[0], ps._slots[index])

        index = ps.find(VALUES[1])
        self.assertIn(VALUES[1], ps._slots[index])

        index = ps.find(VALUES[2])
        self.assertIn(VALUES[2], ps._slots[index])

        # отсутствующий элемент
        self.assertFalse(ps.get("test3"))

        index = ps.find("test3")
        self.assertIsNone(index)

    def test_remove(self):
        VALUES = [
            "test1",
            "test2",
            "",
        ]
        ps = PowerSet()

        ps.put(VALUES[0])
        ps.put(VALUES[1])
        ps.put(VALUES[2])
        self.assertEqual(ps.size(), 3)

        self.assertTrue(ps.get(VALUES[0]))
        self.assertTrue(ps.get(VALUES[1]))
        self.assertTrue(ps.get(VALUES[2]))

        # удаление отсутствующего элемента
        ps.remove("test3")
        self.assertEqual(ps.size(), 3)

        # удаление существующего элемента
        ps.remove(VALUES[0])
        self.assertEqual(ps.size(), 2)
        self.assertFalse(ps.get(VALUES[0]))

        # удаление отсутствующего элемента
        ps.remove(VALUES[0])
        self.assertEqual(ps.size(), 2)

        # удаление элемента с пустой строкой
        ps.remove(VALUES[2])
        self.assertEqual(ps.size(), 1)
        self.assertFalse(ps.get(VALUES[2]))

    def test_intersection(self):
        ps1 = PowerSet()
        ps2 = PowerSet()
        ps3 = PowerSet()

        for n in range(0, 10):
            ps1.put("test" + str(n))

        for n in range(5, 15):
            ps2.put("test" + str(n))

        for n in range(10, 20):
            ps3.put("test" + str(n))

        self.assertEqual(ps1.size(), 10)
        self.assertEqual(ps2.size(), 10)
        self.assertEqual(ps3.size(), 10)

        # в результате пустое множество
        res = ps1.intersection(ps3)
        self.assertEqual(res.size(), 0)

        # в результате не пустое множество
        res = ps1.intersection(ps2)
        self.assertEqual(res.size(), 5)

        self.assertFalse(res.get("test4"))

        for n in range(5, 10):
            self.assertTrue(res.get("test" + str(n)))

        self.assertFalse(res.get("test10"))

        res = ps2.intersection(ps3)
        self.assertEqual(res.size(), 5)

        self.assertFalse(res.get("test9"))

        for n in range(10, 15):
            self.assertTrue(res.get("test" + str(n)))

        self.assertFalse(res.get("test15"))

    def test_union(self):
        ps1 = PowerSet()
        ps2 = PowerSet()
        ps3 = PowerSet()
        ps4 = PowerSet()
        ps5 = PowerSet()

        for n in range(0, 10):
            ps1.put("test" + str(n))

        for n in range(5, 15):
            ps2.put("test" + str(n))

        for n in range(15, 30):
            ps4.put("test" + str(n))

        self.assertEqual(ps1.size(), 10)
        self.assertEqual(ps2.size(), 10)
        self.assertEqual(ps3.size(), 0)
        self.assertEqual(ps4.size(), 15)
        self.assertEqual(ps5.size(), 0)

        # оба параметра непустые
        res = ps1.union(ps2)
        self.assertNotEqual(res, ps1)
        self.assertNotEqual(res, ps2)
        self.assertEqual(res.size(), 15)

        for n in range(0, 15):
            self.assertTrue(res.get("test" + str(n)))

        self.assertFalse(res.get("test15"))

        res = ps1.union(ps4)
        self.assertEqual(res.size(), 25)

        for n in range(0, 10):
            self.assertTrue(res.get("test" + str(n)))

        for n in range(10, 15):
            self.assertFalse(res.get("test" + str(n)))

        for n in range(15, 30):
            self.assertTrue(res.get("test" + str(n)))

        self.assertFalse(res.get("test30"))

        res = ps4.union(ps1)
        self.assertEqual(res.size(), 25)

        for n in range(0, 10):
            self.assertTrue(res.get("test" + str(n)))

        for n in range(10, 15):
            self.assertFalse(res.get("test" + str(n)))

        for n in range(15, 30):
            self.assertTrue(res.get("test" + str(n)))

        self.assertFalse(res.get("test30"))

        # один из параметров -- пустое множество
        res = ps1.union(ps3)
        self.assertEqual(res.size(), 10)

        for n in range(0, 10):
            self.assertTrue(res.get("test" + str(n)))

        self.assertFalse(res.get("test10"))

        res = ps3.union(ps1)
        self.assertEqual(res.size(), 10)

        for n in range(0, 10):
            self.assertTrue(res.get("test" + str(n)))

        self.assertFalse(res.get("test10"))

        # оба множества -- пустые
        res = ps3.union(ps5)
        self.assertEqual(res.size(), 0)
        res = ps5.union(ps3)
        self.assertEqual(res.size(), 0)

    def test_difference(self):
        ps1 = PowerSet()
        ps2 = PowerSet()
        ps3 = PowerSet()
        ps4 = PowerSet()

        for n in range(0, 10):
            ps1.put("test" + str(n))

        for n in range(5, 15):
            ps2.put("test" + str(n))

        for n in range(10, 20):
            ps3.put("test" + str(n))

        for n in range(0, 10):
            ps4.put("test" + str(n))

        self.assertEqual(ps1.size(), 10)
        self.assertEqual(ps2.size(), 10)
        self.assertEqual(ps3.size(), 10)

        # все элементы текущего множества не входят в множество-параметр
        res = ps1.difference(ps3)
        self.assertEqual(res.size(), 10)

        for n in range(0, 10):
            self.assertTrue(res.get("test" + str(n)))

        self.assertFalse(res.get("test10"))

        # в результате пустое множество
        res = ps1.difference(ps4)
        self.assertEqual(res.size(), 0)

        # в результате не пустое множество
        res = ps1.difference(ps2)
        self.assertEqual(res.size(), 5)

        for n in range(0, 5):
            self.assertTrue(res.get("test" + str(n)))

        for n in range(5, 10):
            self.assertFalse(res.get("test" + str(n)))

        res = ps2.difference(ps1)
        self.assertEqual(res.size(), 5)

        for n in range(10, 15):
            self.assertTrue(res.get("test" + str(n)))

        for n in range(5, 10):
            self.assertFalse(res.get("test" + str(n)))

    def test_issubset(self):
        ps1 = PowerSet()
        ps2 = PowerSet()
        ps3 = PowerSet()
        ps4 = PowerSet()
        ps5 = PowerSet()
        ps6 = PowerSet()

        for n in range(0, 10):
            ps1.put("test" + str(n))

        for n in range(5, 10):
            ps2.put("test" + str(n))

        for n in range(7, 20):
            ps3.put("test" + str(n))

        for n in range(10, 20):
            ps4.put("test" + str(n))

        self.assertEqual(ps1.size(), 10)
        self.assertEqual(ps2.size(), 5)
        self.assertEqual(ps3.size(), 13)
        self.assertEqual(ps4.size(), 10)
        self.assertEqual(ps5.size(), 0)
        self.assertEqual(ps6.size(), 0)

        # все элементы параметра входят в текущее множество
        self.assertTrue(ps1.issubset(ps2))

        # все элементы текущего множества входят в параметр
        self.assertFalse(ps2.issubset(ps1))

        # не все элементы параметра входят в текущее множество
        self.assertFalse(ps3.issubset(ps2))
        self.assertFalse(ps2.issubset(ps3))

        # множества не имеют общих элементов
        self.assertFalse(ps1.issubset(ps4))
        self.assertFalse(ps4.issubset(ps1))

        # в параметре пустое множество
        self.assertFalse(ps1.issubset(ps5))

        # текущее множество -- пустое
        self.assertFalse(ps5.issubset(ps1))

        # оба множества -- пустые
        self.assertFalse(ps5.issubset(ps6))
        self.assertFalse(ps6.issubset(ps5))

    def test_timing(self):
        from timeit import default_timer as timer
        from datetime import timedelta
        from random import randrange

        # операции над множествами из десятков тысяч элементов
        # должны укладываться в пару секунд
        REFERENCE = 2

        ps1 = PowerSet()
        ps2 = PowerSet()

        values = [self.get_random_string(100) for n in range(100)]

        print("Loop 19900: ", timedelta(seconds=timer()))
        start = timer()
        for n in range(0, 19800):
            ps1.put(self.get_random_string(randrange(10, 150)))
        for val in values:
            ps1.put(val)
        end = timer()
        print("created 19900: " + str(timedelta(seconds=end-start)))

        print("Loop 21100: ", timedelta(seconds=timer()))
        start = timer()
        for n in range(0, 21000):
            ps2.put(self.get_random_string(randrange(10, 150)))

        for val in values:
            ps2.put(val)
        end = timer()
        print("created 21100: " + str(timedelta(seconds=end-start)))

        self.assertEqual(ps1.size(), 19900)
        self.assertEqual(ps2.size(), 21100)

        # put
        start = timer()
        ps1.put(self.get_random_string(randrange(10, 150)))
        end = timer()
        print("put: " + str(timedelta(seconds=end-start)))
        self.assertTrue(end-start <= REFERENCE)

        # get
        val = self.get_random_string(randrange(10, 150))
        ps1.put(val)

        start = timer()
        ps1.get(val)
        end = timer()
        print("get: " + str(timedelta(seconds=end-start)))
        self.assertTrue(end-start <= REFERENCE)

        # remove
        val = self.get_random_string(randrange(10, 150))
        ps1.put(val)

        start = timer()
        ps1.remove(val)
        end = timer()
        print("remove: " + str(timedelta(seconds=end-start)))
        self.assertTrue(end-start <= REFERENCE)

        # intersection
        print("\nIntersection start: ", timedelta(seconds=timer()))
        start = timer()
        ps1.intersection(ps2)
        end = timer()
        print(timedelta(seconds=end-start))
        self.assertTrue(end-start <= REFERENCE)

        # union
        print("\nUnion start: ", timedelta(seconds=timer()))
        start = timer()
        ps1.union(ps2)
        end = timer()
        print(timedelta(seconds=end-start))
        self.assertTrue(end-start <= REFERENCE)

        # difference
        print("\nDifference start: ", timedelta(seconds=timer()))
        start = timer()
        ps1.difference(ps2)
        end = timer()
        print(timedelta(seconds=end-start))
        self.assertTrue(end-start <= REFERENCE)

        # issubset
        print("\nIssubset start: ", timedelta(seconds=timer()))
        start = timer()
        ps1.issubset(ps1)
        end = timer()
        print(timedelta(seconds=end-start))
        self.assertTrue(end-start <= REFERENCE)

    @staticmethod
    def get_random_string(length):
        import random
        import string

        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for i in range(length))
