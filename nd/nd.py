class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        
    @classmethod
    def from_size(cls, *, size):
        return cls(size)

    def hash_fun(self, key: str):
        # в качестве value поступают строки!
        if not isinstance(key, str):
            return None

        return sum(key.encode("utf-8")) % self.size

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False

        if not isinstance(key, str):
            return False

        index = self.find(key)

        if index is not None:
            return True

        return False

    def seek_slot(self, value: str):
        if not isinstance(value, str):
            return None

        index = self.hash_fun(value)

        if self.slots[index] is None:
            return index

        return self.__find_loop(index, None)

    def put(self, key: str, value: str):
        # гарантированно записываем
        # значение value по ключу key

        if not isinstance(key, str):
            return None

        # update value
        if self.is_key(key):
            key_index = self.find(key)
            self.values[key_index] = value
            return

        key_index = self.seek_slot(key)

        if key_index is not None:
            self.slots[key_index] = key
            self.values[key_index] = value

    def get(self, key):
        # возвращает value для key,
        # или None если ключ не найден

        if not isinstance(key, str):
            return None

        key_index = self.find(key)

        return self.values[key_index] if key_index is not None else None

    def find(self, value: str):
        if not isinstance(value, str):
            return None

        index = self.hash_fun(value)

        return self.__find_loop(index, value)

    def __find_loop(self, index, value):
        if self.slots[index] == value:
            return index

        next_index = index + 1

        if next_index >= self.size:
            next_index -= self.size

        while next_index != index:
            if self.slots[next_index] == value:
                return next_index

            next_index += 1

            if next_index >= self.size:
                next_index -= self.size

        return None
