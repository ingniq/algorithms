import unittest
from dyn_array import DynArray


class DynArrayMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.da = DynArray()

        self.test_0 = 0
        self.test_negative = -1
        self.test_int = 100
        self.test_str = "string"
        self.test_none = None
        self.test_list = [self.test_str, self.test_int, self.test_0, self.test_none]

        super(DynArrayMethods, self).__init__(*args, **kwargs)

    def test_insert(self):
        self.assertEqual(self.da.count, 0)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # проверка индекса
        # попытка вставки элемента в недопустимую позицию
        with self.assertRaisesRegex(IndexError, '^Index is out of bounds$'):
            self.da.insert(-1, self.test_0)
        with self.assertRaisesRegex(IndexError, '^Index is out of bounds$'):
            self.da.insert(1, self.test_0)

        # вставка элемента (размер буфера не превышен)
        # в пустой массив
        self.da.insert(0, self.test_0)
        self.assertEqual(self.da[0], self.test_0)
        self.assertEqual(self.da.count, 1)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # в конец массива с одним элементом
        self.da.insert(1, self.test_int)
        self.assertEqual(self.da[1], self.test_int)
        self.assertEqual(self.da.count, 2)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # в конец массива (строка)
        self.da.insert(2, self.test_str)
        self.assertEqual(self.da[2], self.test_str)
        self.assertEqual(self.da.count, 3)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # в конец массива (None)
        self.da.insert(3, self.test_none)
        self.assertEqual(self.da[3], self.test_none)
        self.assertEqual(self.da.count, 4)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # в конец массива (сложный тип данных)
        self.da.insert(4, self.test_list)
        self.assertEqual(self.da[4], self.test_list)
        self.assertEqual(self.da.count, 5)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # вставка в начало
        self.da.insert(0, self.test_str)
        self.assertEqual(self.da[0], self.test_str)
        self.assertEqual(self.da[1], self.test_0)
        self.assertEqual(self.da[2], self.test_int)
        self.assertEqual(self.da[3], self.test_str)
        self.assertEqual(self.da[4], self.test_none)
        self.assertEqual(self.da[5], self.test_list)
        self.assertEqual(self.da.count, 6)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # вставка в середину
        self.da.insert(3, self.test_none)
        self.assertEqual(self.da[0], self.test_str)
        self.assertEqual(self.da[1], self.test_0)
        self.assertEqual(self.da[2], self.test_int)
        self.assertEqual(self.da[3], self.test_none)
        self.assertEqual(self.da[4], self.test_str)
        self.assertEqual(self.da[5], self.test_none)
        self.assertEqual(self.da[6], self.test_list)
        self.assertEqual(self.da.count, 7)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da), 7)
        self.assertEqual(len(self.da.array), 16)

        # с отрицательным значением в середину
        self.da.insert(3, self.test_negative)
        self.assertEqual(self.da[0], self.test_str)
        self.assertEqual(self.da[1], self.test_0)
        self.assertEqual(self.da[2], self.test_int)
        self.assertEqual(self.da[3], self.test_negative)
        self.assertEqual(self.da[4], self.test_none)
        self.assertEqual(self.da[5], self.test_str)
        self.assertEqual(self.da[6], self.test_none)
        self.assertEqual(self.da[7], self.test_list)
        self.assertEqual(self.da.count, 8)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da), 8)
        self.assertEqual(len(self.da.array), 16)

        # заполнение буфера
        item_index = 8
        while item_index < 16:
            self.da.insert(item_index, self.test_0)
            item_index += 1

        self.assertEqual(self.da[0], self.test_str)
        self.assertEqual(self.da[1], self.test_0)
        self.assertEqual(self.da[2], self.test_int)
        self.assertEqual(self.da[3], self.test_negative)
        self.assertEqual(self.da[4], self.test_none)
        self.assertEqual(self.da[5], self.test_str)
        self.assertEqual(self.da[6], self.test_none)
        self.assertEqual(self.da[7], self.test_list)

        item_index = 8
        while item_index < 16:
            self.assertEqual(self.da[item_index], self.test_0)
            item_index += 1

        self.assertEqual(self.da.count, 16)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # вставка элемента в конец (превышен размер буфера)
        self.da.insert(16, self.test_str)
        self.assertEqual(self.da.count, 17)
        self.assertEqual(self.da.capacity, 32)
        self.assertEqual(len(self.da.array), 32)

        # заполнение буфера
        item_index = 17
        while item_index < 32:
            self.da.insert(item_index, self.test_0)
            item_index += 1

        self.assertEqual(self.da.count, 32)
        self.assertEqual(self.da.capacity, 32)
        self.assertEqual(len(self.da.array), 32)

        # вставка элемента в середину (превышен размер буфера)
        self.da.insert(18, self.test_str)
        self.assertEqual(self.da[18], self.test_str)
        self.assertEqual(self.da.count, 33)
        self.assertEqual(self.da.capacity, 64)
        self.assertEqual(len(self.da.array), 64)

        # проверка индекса
        # попытка вставки элемента в недопустимую позицию
        with self.assertRaisesRegex(IndexError, '^Index is out of bounds$'):
            self.da.insert(35, self.test_0)

    def test_delete(self):
        self.assertEqual(self.da.count, 0)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # удаление из пустого массива
        with self.assertRaisesRegex(BufferError, '^Buffer is empty$'):
            self.da.delete(0)
        with self.assertRaisesRegex(BufferError, '^Buffer is empty$'):
            self.da.delete(1)

        # *** размер буфера не меняется ***
        # из начала когда остается один элемент
        self.da.append(self.test_str)
        self.da.append(self.test_none)
        self.da.delete(0)

        self.assertEqual(self.da[0], self.test_none)
        self.assertEqual(self.da.count, 1)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # из конца когда остается один элемент
        self.da.append(self.test_str)
        self.da.delete(1)

        self.assertEqual(self.da[0], self.test_none)
        self.assertEqual(self.da.count, 1)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # когда остается пустой массив
        self.da.delete(0)

        self.assertEqual(self.da.count, 0)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # удаление из начала
        self.da.append(self.test_0)
        self.da.append(self.test_int)
        self.da.append(self.test_negative)
        self.da.append(self.test_str)
        self.da.append(self.test_none)
        self.da.append(self.test_list)

        self.assertEqual(self.da.count, 6)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        self.da.delete(0)
        self.assertEqual(self.da[0], self.test_int)
        self.assertEqual(self.da[1], self.test_negative)
        self.assertEqual(self.da[2], self.test_str)
        self.assertEqual(self.da[3], self.test_none)
        self.assertEqual(self.da[4], self.test_list)

        self.assertEqual(self.da.count, 5)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # удаление из середины
        self.da.delete(2)
        self.assertEqual(self.da[0], self.test_int)
        self.assertEqual(self.da[1], self.test_negative)
        self.assertEqual(self.da[2], self.test_none)
        self.assertEqual(self.da[3], self.test_list)

        self.assertEqual(self.da.count, 4)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # удаление из конца
        self.da.delete(3)
        self.assertEqual(self.da[0], self.test_int)
        self.assertEqual(self.da[1], self.test_negative)
        self.assertEqual(self.da[2], self.test_none)

        self.assertEqual(self.da.count, 3)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # размер буфера не уменьшается с 16, если кол-во элементов стало < 16/2
        # заполнение буфера
        item_index = 3
        while item_index < 9:
            self.da.insert(item_index, self.test_0)
            item_index += 1

        self.assertEqual(self.da.count, 9)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        self.da.delete(3)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        self.da.delete(3)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # *** размер буфера меняется ***
        # буфер уменьшается с 32 до 21, если кол-во элементов стало < 32/2
        # заполнение буфера
        item_index = 7
        while item_index < 17:
            self.da.insert(item_index, self.test_0)
            item_index += 1

        self.assertEqual(self.da.count, 17)
        self.assertEqual(self.da.capacity, 32)
        self.assertEqual(len(self.da.array), 32)

        self.da.delete(3)
        self.assertEqual(self.da.capacity, 32)
        self.assertEqual(len(self.da.array), 32)

        self.da.delete(3)
        self.assertEqual(self.da.capacity, 21)
        self.assertEqual(len(self.da.array), 21)

        # буфер уменьшается с 21 до 16 (не до 14!), если кол-во элементов стало < 21/2
        self.assertEqual(self.da.count, 15)

        self.da.delete(3)
        self.da.delete(3)
        self.da.delete(3)
        self.da.delete(3)
        self.da.delete(3)

        self.assertEqual(self.da.count, 10)
        self.assertEqual(self.da.capacity, 21)
        self.assertEqual(len(self.da.array), 21)

        self.da.delete(3)
        self.assertEqual(self.da.count, 9)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # буфер уменьшается с 64 до 42, если кол-во элементов стало < 64/2
        # заполнение буфера
        item_index = 9
        while item_index < 33:
            self.da.insert(item_index, self.test_0)
            item_index += 1

        self.assertEqual(self.da.count, 33)
        self.assertEqual(self.da.capacity, 64)
        self.assertEqual(len(self.da.array), 64)

        self.da.delete(3)
        self.assertEqual(self.da.count, 32)
        self.assertEqual(self.da.capacity, 64)
        self.assertEqual(len(self.da.array), 64)

        self.da.delete(3)
        self.assertEqual(self.da.count, 31)
        self.assertEqual(self.da.capacity, 42)
        self.assertEqual(len(self.da.array), 42)

        # буфер уменьшается с 42 до 28, если кол-во элементов стало < 42/2
        # удаление лишних элементов
        item_index = 30
        while item_index > 21:
            self.da.delete(item_index)
            item_index -= 1
        self.assertEqual(self.da.count, 22)

        self.da.delete(3)
        self.assertEqual(self.da.count, 21)
        self.assertEqual(self.da.capacity, 42)
        self.assertEqual(len(self.da.array), 42)

        self.da.delete(3)
        self.assertEqual(self.da.count, 20)
        self.assertEqual(self.da.capacity, 28)
        self.assertEqual(len(self.da.array), 28)

        # буфер уменьшается с 28 до 18, если кол-во элементов стало < 28/2
        # удаление лишних элементов
        item_index = 19
        while item_index > 14:
            self.da.delete(item_index)
            item_index -= 1
        self.assertEqual(self.da.count, 15)

        self.da.delete(3)
        self.assertEqual(self.da.count, 14)
        self.assertEqual(self.da.capacity, 28)
        self.assertEqual(len(self.da.array), 28)

        self.da.delete(3)
        self.assertEqual(self.da.count, 13)
        self.assertEqual(self.da.capacity, 18)
        self.assertEqual(len(self.da.array), 18)

        # буфер уменьшается с 18 до 16 (не до 12!), если кол-во элементов стало < 18/2
        # удаление лишних элементов
        item_index = 13
        while item_index > 10:
            self.da.delete(item_index)
            item_index -= 1
        self.assertEqual(self.da.count, 10)

        self.da.delete(3)
        self.assertEqual(self.da.count, 9)
        self.assertEqual(self.da.capacity, 18)
        self.assertEqual(len(self.da.array), 18)

        self.da.delete(3)
        self.assertEqual(self.da.count, 8)
        self.assertEqual(self.da.capacity, 16)
        self.assertEqual(len(self.da.array), 16)

        # попытка удаления элемента в недопустимой позиции (проверка индекса)
        with self.assertRaisesRegex(IndexError, '^Index is out of bounds$'):
            self.da.delete(-1)
        with self.assertRaisesRegex(IndexError, '^Index is out of bounds$'):
            self.da.delete(35)
