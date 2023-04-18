class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        
    @classmethod
    def create_by_parameters(cls, *, size, step):
        return cls(size, step)

    def hash_fun(self, value: str):
        # в качестве value поступают строки!
        if not isinstance(value, str):
            return None

        return sum(value.encode("utf-8")) % self.size

    def seek_slot(self, value: str):
        if not isinstance(value, str):
            return None

        slot_index = self.hash_fun(value)

        if self.slots[slot_index] is None:
            return slot_index

        return self.__find_loop(slot_index, None)

    def put(self, value: str):
        # записываем значение по хэш-функции
        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся разместить

        if not isinstance(value, str):
            return None

        slot_index = self.find(value)

        if slot_index is not None:
            return slot_index

        slot_index = self.seek_slot(value)

        if slot_index is not None:
            self.slots[slot_index] = value

        return slot_index

    def find(self, value: str):
        if not isinstance(value, str):
            return None

        slot_index = self.hash_fun(value)

        if self.slots[slot_index] is None:
            return None

        if self.slots[slot_index] == value:
            return slot_index

        return self.__find_loop(slot_index, value)

    def __find_loop(self, index, value):
        next_index = index + self.step

        if next_index >= self.size:
            next_index -= self.size

        while next_index != index:
            if self.slots[next_index] == value:
                return next_index

            next_index += self.step

            if next_index >= self.size:
                next_index -= self.size

        return None
