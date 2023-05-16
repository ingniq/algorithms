class aBST:

    def __init__(self, depth: int):
        tree_size = 2 ** (depth + 1) - 1
        self.size = tree_size
        self.Tree = [None] * tree_size

    def FindKeyIndex(self, key) -> int:
        index = 0

        while index < self.size:
            if self.Tree[index] is None:
                return index * -1

            if key == self.Tree[index]:
                return index

            if key > self.Tree[index]:
                index = index * 2 + 2
            else:
                index = index * 2 + 1

        return None

    def AddKey(self, key) -> int:
        index = self.FindKeyIndex(key)

        if index == 0 and self.Tree[0] is None:
            self.Tree[index] = key

        if index is None:
            return -1

        if index < 0:
            index *= -1
            self.Tree[index] = key

        return index
