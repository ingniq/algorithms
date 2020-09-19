import ctypes


class DynArray:
    MIN_CAPACITY = 16
    MAGNIFICATION_BUFFER = 2
    DECREASE_BUFFER = 1.5

    def __init__(self):
        self.count = 0
        self.capacity = self.MIN_CAPACITY
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        return self.array[i]

    def resize(self, new_capacity):
        """Общая сложность функции: O(self.count) -> O(N)."""
        new_array = self.make_array(new_capacity)

        for i in range(self.count):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(self.MAGNIFICATION_BUFFER * self.capacity)

        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        """Добавляем объект itm в позицию i, начиная с 0.

        Общая сложность функции: O(6*self.count+N+10) -> O(N)
        """
        if i < 0 or i > self.count:  # Операции сравнения и дизъюнкция - O(3)
            raise IndexError('Index is out of bounds')

        # превышение размера буфера
        if self.count == self.capacity:  # Операция сравнения сложностью O(1)
            self.resize(self.MAGNIFICATION_BUFFER * self.capacity)  # O(N+1)

        item_index = self.count  # Операция присваивания сложностью O(1)
        # Цикл сложностью O(6*self.count+1)
        while item_index > i:  # Операция сравнения сложностью O(1)
            self.array[item_index] = self.array[item_index - 1]  # Обращение по индексу, присваивание и вычетание - O(4)
            item_index -= 1  # Операция уменьшения индекса сложностью O(1)

        self.array[i] = itm  # Обращение по индексу и присваивание - O(2)
        self.count += 1  # Операция приращения сложностью O(1)
        return

    def delete(self, i):
        """Удаляем объект в позиции i.

        Общая сложность функции: O(6*self.count+N+23) -> O(N)
        """
        if i >= 0 and self.count == 0:  # Две операции сравнения и конъюнкция - O(3)
            raise BufferError('Buffer is empty')

        if i < 0 or i > self.count:  # Две операции сравнения и дизъюнкция - O(3)
            raise IndexError('Index is out of bounds')

        # уменьшение размера буфера
        check_limit = (int)(self.capacity / self.MAGNIFICATION_BUFFER)  # Операции деления, приведения типа и присваивания - O(3)
        if self.count >= check_limit and self.count - 1 < check_limit:  # Операции вычетания, сравнений и конъюнкция - O(4)
            new_size = (int)(self.capacity / self.DECREASE_BUFFER)  # Операции деления, приведения типа и присваивания - O(3)

            if new_size < self.MIN_CAPACITY:  # Сравнение - O(1)
                new_size = self.MIN_CAPACITY  # Присваивание - O(1)

            self.resize(new_size)  # Сравнение - O(N)

        self.count -= 1  # Операция уменьшения индекса - O(1)
        item_index = i  # Присваивание - O(1)

        # Цикл сложностью O(6*self.count+1)
        while item_index < self.count:  # Операция сравнения - O(1)
            self.array[item_index] = self.array[item_index + 1]  # Обращение по индексу, присваивание и сложение - O(4)
            item_index += 1  # Операция приращения - O(1)

        self.array[self.count] = None  # Обращение по индексу и присваивание - O(2)

        return
