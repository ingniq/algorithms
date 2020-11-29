class HashTable:
    def __init__(self, sz):
        self.__size = sz
        self._populate = []
        self._slots = [None] * self.__size

    def hash_fun(self, value: str):
        if not isinstance(value, str):
            return None

        return sum(value.encode("utf-8")) % self.__size

    def put(self, value: str):
        if not isinstance(value, str):
            return None

        exist = self.find(value)

        if exist is not None:
            return exist

        slot_index = self.hash_fun(value)

        if self._slots[slot_index] is None:
            self._slots[slot_index] = []

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
    def __init__(self):
        # реализация хранилища
        sz = 40009
        super(PowerSet, self).__init__(sz)

    def size(self):
        # количество элементов в множестве
        return len(self._populate)

    def get(self, value: str):
        # возвращает True если value имеется в множестве,
        # иначе False
        if self.find(value) is not None:
            return True

        return False

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        index = self.find(value)

        if index is not None:
            self._slots[index].remove(value)
            self._populate.remove(index)

            if len(self._slots[index]) == 0:
                self._slots[index] = None

            return True

        return False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        result = PowerSet()
        target, iterate = [self, set2] if self.size() > set2.size() else [set2, self]

        for slot_index in iterate._populate:
            values = iterate._slots[slot_index]

            for val in values:
                if target.find(val) is not None:
                    result.put(val)

        return result

    def union(self, set2):
        from copy import copy

        # объединение текущего множества и set2
        target, iterate = [self, set2] if self.size() > set2.size() else [set2, self]
        result = copy(target)

        for slot_index in iterate._populate:
            values = iterate._slots[slot_index]

            for val in values:
                if target.find(val) is None:
                    result.put(val)

        return result

    def difference(self, set2):
        # разница текущего множества и set2
        result = PowerSet()
        target, iterate = [self, set2] if self.size() > set2.size() else [set2, self]

        for slot_index in iterate._populate:
            values = iterate._slots[slot_index]

            for val in values:
                if target.find(val) is None:
                    result.put(val)

        return result

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False

        if set2.size() == 0:
            return False

        for slot_index in set2._populate:
            values = set2._slots[slot_index]

            for val in values:
                if self.find(val) is None:
                    return False

        return True
