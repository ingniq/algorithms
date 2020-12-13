class NativeDictionary:
    def __init__(self, sz):
        self._size = sz
        self._slots = [None] * self._size
        self._values = [None] * self._size

    def __hash_fun(self, key: str):
        # в качестве value поступают строки!
        if not isinstance(key, str):
            return None

        return sum(key.encode("utf-8")) % self._size

    def _seek_slot(self, value: str):
        if not isinstance(value, str):
            return None

        index = self.__hash_fun(value)

        return self._find_loop(index, None)

    def put(self, key: str, value: str):
        # гарантированно записываем
        # значение value по ключу key

        if not isinstance(key, str):
            return None

        # update value
        key_index = self.find(key)

        if key_index is None:
            key_index = self._seek_slot(key)

        if key_index is not None:
            self._slots[key_index] = key
            self._values[key_index] = value

    def get(self, key):
        # возвращает value для key,
        # или None если ключ не найден

        if not isinstance(key, str):
            return None

        key_index = self.find(key)

        return None if key_index is None else self._values[key_index]

    def find(self, key: str):
        if not isinstance(key, str):
            return None

        index = self.__hash_fun(key)

        return self._find_loop(index, key)

    def _find_loop(self, index, value):
        if self._slots[index] == value:
            return index

        next_index = index + 1

        if next_index >= self._size:
            next_index -= self._size

        while next_index != index:
            if self._slots[next_index] == value:
                return next_index

            next_index += 1

            if next_index >= self._size:
                next_index -= self._size

        return None


class NativeCache(NativeDictionary):
    def __init__(self, sz: int):
        self.__len = 0
        self._hits = [0] * sz
        self._min_hits = [0, 1]  # индексы элементов с минимальным кол-м обращений
        self.collisions = 0
        self.debug = 0
        super(NativeCache, self).__init__(sz)

    def get(self, key: str):
        if not isinstance(key, str):
            return None

        # поиск существующего элемента
        key_index = self.find(key)

        if key_index is not None:
            # если найден, то увеличиваем кол-во обращений
            self._hits[key_index] += 1

            # обновляем указатели на элементы с наименьшим кол-ом обращений
            hits = self._hits[key_index]
            min_hits_1 = self._hits[self._min_hits[0]]
            min_hits_2 = self._hits[self._min_hits[1]]

            if key_index not in self._min_hits:
                if min_hits_1 >= hits:
                    self._min_hits[0] = key_index
                elif min_hits_2 >= hits:
                    self._min_hits[1] = key_index

            if key_index == self._min_hits[1]:
                self.debug += 1
                self._min_hits[1] = self.__find_min_hits_index()

            if min_hits_2 < min_hits_1:
                self._min_hits = [self._min_hits[1], self._min_hits[0]]

        # возвращаем значение
        return None if key_index is None else self._values[key_index]

    def put(self, key: str, value: str):
        if not isinstance(key, str):
            return None

        # поиск существующего элемента
        key_index = self.find(key)

        # если не найден, то добавляем
        if key_index is None:
            if self.__len == self._size:
                # если массив заполнен, то берем элемент с наименьшим кол-ом обращений
                key_index = self._min_hits[0]
                self._hits[key_index] = 0
            else:
                # иначе берем первый пустой элемент
                key_index = self._seek_slot(key)
                self.__len += 1

        # добавляем/обновляем
        self._slots[key_index] = key
        self._values[key_index] = value

        # обновляем указатели на элементы с наименьшим кол-ом обращений
        hits = self._hits[key_index]
        min_hits_1 = self._hits[self._min_hits[0]]
        min_hits_2 = self._hits[self._min_hits[1]]

        if key_index not in self._min_hits:
            if min_hits_1 > hits:
                self._min_hits[0] = key_index
            elif min_hits_2 > hits:
                self._min_hits[1] = key_index

        if min_hits_2 < min_hits_1:
            self._min_hits = [self._min_hits[1], self._min_hits[0]]

    def remove(self, key: str):
        if not isinstance(key, str):
            return None

        # если массив пустой
        if self.__len == 0:
            return None

        # поиск существующего элемента
        key_index = self.find(key)

        # если не найден
        if key_index is None:
            return None

        # удаление
        self._slots[key_index] = None
        self._values[key_index] = None
        self._hits[key_index] = 0
        self._min_hits[0] = key_index
        self.__len -= 1

    def __len__(self):
        return self.__len

    def len(self):
        return self.__len

    def _find_loop(self, index, value):
        # Смотрим элемент с вычисленным индексом-хэшем.
        if self._slots[index] == value:
            return index

        if value is None:
            self.collisions += 1

        # Смотрим элемент с наименьшим кол-м обращений в случае поиска значения.
        if value and self._slots[self._min_hits[0]] == value:
            return self._min_hits[0]

        return super(NativeCache, self)._find_loop(index, value)

    def __find_min_hits_index(self):
        min_hits_index = self._min_hits[1]
        min_hits = self._hits[min_hits_index]

        for i, hits in enumerate(self._hits):
            if i in self._min_hits:
                continue

            if hits < min_hits:
                min_hits_index = i

            if hits == 0:
                break

        return min_hits_index