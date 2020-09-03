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
        """Добавляем объект itm в позицию i, начиная с 0."""
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        # превышение размера буфера
        if self.count == self.capacity:
            self.resize(self.MAGNIFICATION_BUFFER * self.capacity)

        item_index = self.count
        while item_index > i:
            self.array[item_index] = self.array[item_index - 1]
            item_index -= 1

        self.array[i] = itm
        self.count += 1
        return

    def delete(self, i):
        """Удаляем объект в позиции i."""
        if i >= 0 and self.count == 0:
            raise BufferError('Buffer is empty')

        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        # уменьшение размера буфера
        check_limit = (int)(self.capacity / self.MAGNIFICATION_BUFFER)
        if self.count >= check_limit and self.count - 1 < check_limit:
            new_size = (int)(self.capacity / self.DECREASE_BUFFER)

            if new_size < self.MIN_CAPACITY:
                new_size = self.MIN_CAPACITY

            self.resize(new_size)

        self.count -= 1

        item_index = i
        while item_index < self.count:
            self.array[item_index] = self.array[item_index + 1]
            item_index += 1

        self.array[self.count] = None

        return
