import unittest
from dyn_array import DynArray


class DynArrayMethods(unittest.TestCase):
    ZERO_VALUE_FOR_TESTING = 0
    NEGATIVE_VALUE_FOR_TESTING = -1
    INTEGER_VALUE_FOR_TESTING = 100
    STRING_VALUE_FOR_TESTING = "string"
    NONE_VALUE_FOR_TESTING = None
    LIST_VALUE_FOR_TESTING = ["string", 100, 0, None]

    def __init__(self, *args, **kwargs):
        self.dynamic_array_for_testing = DynArray()

        super(DynArrayMethods, self).__init__(*args, **kwargs)

    def test_insert(self):
        self.assertEqual(self.dynamic_array_for_testing.count, 0)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # проверка индекса
        # попытка вставки элемента в недопустимую позицию
        with self.assertRaisesRegex(IndexError, '^Index is out of bounds$'):
            self.dynamic_array_for_testing.insert(-1, self.ZERO_VALUE_FOR_TESTING)
        with self.assertRaisesRegex(IndexError, '^Index is out of bounds$'):
            self.dynamic_array_for_testing.insert(1, self.ZERO_VALUE_FOR_TESTING)

        # вставка элемента (размер буфера не превышен)
        # в пустой массив
        self.dynamic_array_for_testing.insert(0, self.ZERO_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[0], self.ZERO_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing.count, 1)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # в конец массива с одним элементом
        self.dynamic_array_for_testing.insert(1, self.INTEGER_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[1], self.INTEGER_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing.count, 2)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # в конец массива (строка)
        self.dynamic_array_for_testing.insert(2, self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[2], self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing.count, 3)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # в конец массива (None)
        self.dynamic_array_for_testing.insert(3, self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[3], self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing.count, 4)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # в конец массива (сложный тип данных)
        self.dynamic_array_for_testing.insert(4, self.LIST_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[4], self.LIST_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing.count, 5)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # вставка в начало
        self.dynamic_array_for_testing.insert(0, self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[0], self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[1], self.ZERO_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[2], self.INTEGER_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[3], self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[4], self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[5], self.LIST_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing.count, 6)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # вставка в середину
        self.dynamic_array_for_testing.insert(3, self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[0], self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[1], self.ZERO_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[2], self.INTEGER_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[3], self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[4], self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[5], self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[6], self.LIST_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing.count, 7)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing), 7)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # с отрицательным значением в середину
        self.dynamic_array_for_testing.insert(3, self.NEGATIVE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[0], self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[1], self.ZERO_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[2], self.INTEGER_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[3], self.NEGATIVE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[4], self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[5], self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[6], self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[7], self.LIST_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing.count, 8)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing), 8)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # заполнение буфера
        item_index = 8
        while item_index < 16:
            self.dynamic_array_for_testing.insert(item_index, self.ZERO_VALUE_FOR_TESTING)
            item_index += 1

        self.assertEqual(self.dynamic_array_for_testing[0], self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[1], self.ZERO_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[2], self.INTEGER_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[3], self.NEGATIVE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[4], self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[5], self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[6], self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[7], self.LIST_VALUE_FOR_TESTING)

        item_index = 8
        while item_index < 16:
            self.assertEqual(self.dynamic_array_for_testing[item_index], self.ZERO_VALUE_FOR_TESTING)
            item_index += 1

        self.assertEqual(self.dynamic_array_for_testing.count, 16)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # вставка элемента в конец (превышен размер буфера)
        self.dynamic_array_for_testing.insert(16, self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing.count, 17)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 32)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 32)

        # заполнение буфера
        item_index = 17
        while item_index < 32:
            self.dynamic_array_for_testing.insert(item_index, self.ZERO_VALUE_FOR_TESTING)
            item_index += 1

        self.assertEqual(self.dynamic_array_for_testing.count, 32)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 32)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 32)

        # вставка элемента в середину (превышен размер буфера)
        self.dynamic_array_for_testing.insert(18, self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[18], self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing.count, 33)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 64)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 64)

        # проверка индекса
        # попытка вставки элемента в недопустимую позицию
        with self.assertRaisesRegex(IndexError, '^Index is out of bounds$'):
            self.dynamic_array_for_testing.insert(35, self.ZERO_VALUE_FOR_TESTING)

    def test_delete(self):
        self.assertEqual(self.dynamic_array_for_testing.count, 0)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # удаление из пустого массива
        with self.assertRaisesRegex(BufferError, '^Buffer is empty$'):
            self.dynamic_array_for_testing.delete(0)
        with self.assertRaisesRegex(BufferError, '^Buffer is empty$'):
            self.dynamic_array_for_testing.delete(1)

        # *** размер буфера не меняется ***
        # из начала когда остается один элемент
        self.dynamic_array_for_testing.append(self.STRING_VALUE_FOR_TESTING)
        self.dynamic_array_for_testing.append(self.NONE_VALUE_FOR_TESTING)
        self.dynamic_array_for_testing.delete(0)

        self.assertEqual(self.dynamic_array_for_testing[0], self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing.count, 1)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # из конца когда остается один элемент
        self.dynamic_array_for_testing.append(self.STRING_VALUE_FOR_TESTING)
        self.dynamic_array_for_testing.delete(1)

        self.assertEqual(self.dynamic_array_for_testing[0], self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing.count, 1)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # когда остается пустой массив
        self.dynamic_array_for_testing.delete(0)

        self.assertEqual(self.dynamic_array_for_testing.count, 0)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # удаление из начала
        self.dynamic_array_for_testing.append(self.ZERO_VALUE_FOR_TESTING)
        self.dynamic_array_for_testing.append(self.INTEGER_VALUE_FOR_TESTING)
        self.dynamic_array_for_testing.append(self.NEGATIVE_VALUE_FOR_TESTING)
        self.dynamic_array_for_testing.append(self.STRING_VALUE_FOR_TESTING)
        self.dynamic_array_for_testing.append(self.NONE_VALUE_FOR_TESTING)
        self.dynamic_array_for_testing.append(self.LIST_VALUE_FOR_TESTING)

        self.assertEqual(self.dynamic_array_for_testing.count, 6)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        self.dynamic_array_for_testing.delete(0)
        self.assertEqual(self.dynamic_array_for_testing[0], self.INTEGER_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[1], self.NEGATIVE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[2], self.STRING_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[3], self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[4], self.LIST_VALUE_FOR_TESTING)

        self.assertEqual(self.dynamic_array_for_testing.count, 5)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # удаление из середины
        self.dynamic_array_for_testing.delete(2)
        self.assertEqual(self.dynamic_array_for_testing[0], self.INTEGER_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[1], self.NEGATIVE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[2], self.NONE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[3], self.LIST_VALUE_FOR_TESTING)

        self.assertEqual(self.dynamic_array_for_testing.count, 4)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # удаление из конца
        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing[0], self.INTEGER_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[1], self.NEGATIVE_VALUE_FOR_TESTING)
        self.assertEqual(self.dynamic_array_for_testing[2], self.NONE_VALUE_FOR_TESTING)

        self.assertEqual(self.dynamic_array_for_testing.count, 3)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # размер буфера не уменьшается с 16, если кол-во элементов стало < 16/2
        # заполнение буфера
        item_index = 3
        while item_index < 9:
            self.dynamic_array_for_testing.insert(item_index, self.ZERO_VALUE_FOR_TESTING)
            item_index += 1

        self.assertEqual(self.dynamic_array_for_testing.count, 9)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # *** размер буфера меняется ***
        # буфер уменьшается с 32 до 21, если кол-во элементов стало < 32/2
        # заполнение буфера
        item_index = 7
        while item_index < 17:
            self.dynamic_array_for_testing.insert(item_index, self.ZERO_VALUE_FOR_TESTING)
            item_index += 1

        self.assertEqual(self.dynamic_array_for_testing.count, 17)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 32)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 32)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 32)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 32)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 21)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 21)

        # буфер уменьшается с 21 до 16 (не до 14!), если кол-во элементов стало < 21/2
        self.assertEqual(self.dynamic_array_for_testing.count, 15)

        self.dynamic_array_for_testing.delete(3)
        self.dynamic_array_for_testing.delete(3)
        self.dynamic_array_for_testing.delete(3)
        self.dynamic_array_for_testing.delete(3)
        self.dynamic_array_for_testing.delete(3)

        self.assertEqual(self.dynamic_array_for_testing.count, 10)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 21)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 21)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.count, 9)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # буфер уменьшается с 64 до 42, если кол-во элементов стало < 64/2
        # заполнение буфера
        item_index = 9
        while item_index < 33:
            self.dynamic_array_for_testing.insert(item_index, self.ZERO_VALUE_FOR_TESTING)
            item_index += 1

        self.assertEqual(self.dynamic_array_for_testing.count, 33)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 64)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 64)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.count, 32)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 64)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 64)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.count, 31)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 42)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 42)

        # буфер уменьшается с 42 до 28, если кол-во элементов стало < 42/2
        # удаление лишних элементов
        item_index = 30
        while item_index > 21:
            self.dynamic_array_for_testing.delete(item_index)
            item_index -= 1
        self.assertEqual(self.dynamic_array_for_testing.count, 22)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.count, 21)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 42)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 42)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.count, 20)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 28)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 28)

        # буфер уменьшается с 28 до 18, если кол-во элементов стало < 28/2
        # удаление лишних элементов
        item_index = 19
        while item_index > 14:
            self.dynamic_array_for_testing.delete(item_index)
            item_index -= 1
        self.assertEqual(self.dynamic_array_for_testing.count, 15)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.count, 14)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 28)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 28)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.count, 13)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 18)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 18)

        # буфер уменьшается с 18 до 16 (не до 12!), если кол-во элементов стало < 18/2
        # удаление лишних элементов
        item_index = 13
        while item_index > 10:
            self.dynamic_array_for_testing.delete(item_index)
            item_index -= 1
        self.assertEqual(self.dynamic_array_for_testing.count, 10)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.count, 9)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 18)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 18)

        self.dynamic_array_for_testing.delete(3)
        self.assertEqual(self.dynamic_array_for_testing.count, 8)
        self.assertEqual(self.dynamic_array_for_testing.capacity, 16)
        self.assertEqual(len(self.dynamic_array_for_testing.array), 16)

        # попытка удаления элемента в недопустимой позиции (проверка индекса)
        with self.assertRaisesRegex(IndexError, '^Index is out of bounds$'):
            self.dynamic_array_for_testing.delete(-1)
        with self.assertRaisesRegex(IndexError, '^Index is out of bounds$'):
            self.dynamic_array_for_testing.delete(35)
