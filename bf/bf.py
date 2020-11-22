from bitarray import bitarray


class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = bitarray(f_len)
        self.filter.setall(0)

    def hash1(self, str1):
        RAND_CONST = 17
        return self.__calc_hash(RAND_CONST, str1)

    def hash2(self, str1):
        RAND_CONST = 223
        return self.__calc_hash(RAND_CONST, str1)

    def add(self, str1):
        # добавляем строку str1 в фильтр
        hash1 = self.hash1(str1)
        hash2 = self.hash2(str1)

        self.filter[hash1] = 1
        self.filter[hash2] = 1

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        hash1 = self.hash1(str1)
        hash2 = self.hash2(str1)

        return (self.filter[hash1] == 1 and self.filter[hash2] == 1)

    def __calc_hash(self, RAND_CONST, str1):
        for c in str1:
            if str1[0] == c:
                hash = 0
            else:
                code = ord(c)
                hash = (hash * RAND_CONST + code) % self.filter_len

        return hash
