class DynArray:
    MIN_CAPACITY = 20011
    MAGNIFICATION_BUFFER = 2
    DECREASE_BUFFER = 1.5

    def __init__(self):
        self.count = 0
        self.capacity = self.MIN_CAPACITY
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return [None] * new_capacity

    def __getitem__(self, i):
        if i < 0 or i >= self.capacity:
            raise IndexError('Index is out of bounds')

        return self.array[i]

    def resize(self, new_capacity: int):
        if not isinstance(new_capacity, int):
            raise ValueError('The parameter must be an integer')
        
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

    def insert(self, i: int, itm):
        """Добавляем объект itm в позицию i, начиная с 0."""
        if not isinstance(i, int):
            raise ValueError('The parameter must be an integer')

        if i < 0:
            raise IndexError('Index is out of bounds')

        # автоматическое увеличение буфера, если индекс за пределами
        while i >= self.capacity:
            self.resize(self.MAGNIFICATION_BUFFER * self.capacity)

        # превышение размера буфера
        if self.count == self.capacity:
            self.resize(self.MAGNIFICATION_BUFFER * self.capacity)

        self.array[i] = itm
        self.count += 1
        return

    def delete(self, i: int):
        """Удаляем объект в позиции i."""
        if not isinstance(i, int):
            raise ValueError('The parameter must be an integer')

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


class HashTable:
    def __init__(self):
        self._populate = []
        self._slots = DynArray()

    def hash_fun(self, value: str):
        if not isinstance(value, str):
            return None

        return sum(value.encode("utf-8")) % self._slots.capacity

    def put(self, value: str):
        if not isinstance(value, str):
            return None

        slot_index = self.find(value)

        if slot_index is not None:
            return slot_index

        slot_index = self.hash_fun(value)

        if self._slots[slot_index] is None:
            self._slots.insert(slot_index, [])

        self._slots[slot_index].append(value)
        self._populate.append(slot_index)

        return slot_index

    def find(self, value: str):
        if not isinstance(value, str):
            return None

        slot_index = self.hash_fun(value)

        if self._slots[slot_index] is None:
            return None

        return slot_index if value in self._slots[slot_index] else None


class PowerSet(HashTable):
    def size(self):
        # количество элементов в множестве
        return len(self._populate)

    def get(self, value: str):
        # возвращает True если value имеется в множестве,
        # иначе False
        if self.find(value) is not None:
            return True

        return False

    def remove(self, value: str):
        # возвращает True если value удалено
        # иначе False
        if not isinstance(value, str):
            raise ValueError('The parameter must be a string')

        slot_index = self.find(value)

        if slot_index is not None:
            self._slots[slot_index].remove(value)
            self._populate.remove(slot_index)

            if len(self._slots[slot_index]) == 0:
                self._slots.insert(slot_index, None)

            return True

        return False

    def intersection(self, set2: PowerSet):
        # пересечение текущего множества и set2
        if not isinstance(set2, PowerSet):
            raise ValueError('The parameter must be a PowerSet')

        intersection = PowerSet()
        target, iterate = [self, set2] if self.size() > set2.size() else [set2, self]

        for slot_index in iterate._populate:
            values = iterate._slots[slot_index]

            for val in values:
                if target.find(val) is not None:
                    intersection.put(val)

        return intersection

    def union(self, set2: PowerSet):
        # объединение текущего множества и set2
        if not isinstance(set2, PowerSet):
            raise ValueError('The parameter must be a PowerSet')

        union = PowerSet()
        target, iterate = [self, set2] if self.size() > set2.size() else [set2, self]

        for slot_index in target._populate:
            values = target._slots[slot_index]

            for val in values:
                union.put(val)

        for slot_index in iterate._populate:
            values = iterate._slots[slot_index]

            for val in values:
                union.put(val)

        return union

    def difference(self, set2: PowerSet):
        # разница текущего множества и set2
        if not isinstance(set2, PowerSet):
            raise ValueError('The parameter must be a PowerSet')

        difference = PowerSet()

        for slot_index in self._populate:
            values = self._slots[slot_index]

            for val in values:
                if set2.find(val) is None:
                    difference.put(val)

        return difference

    def issubset(self, set2: PowerSet):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        if not isinstance(set2, PowerSet):
            raise ValueError('The parameter must be a PowerSet')

        for slot_index in set2._populate:
            values = set2._slots[slot_index]

            for val in values:
                if self.find(val) is None:
                    return False

        return True
