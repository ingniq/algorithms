class Heap:

    def __init__(self):
        self.HeapArray = [] # non-negative numbers

    def MakeHeap(self, a: list, depth: int) -> None:
        self.size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * self.size

        for key in a:
            if not self.Add(key):
                return

    def GetMax(self) -> int:
        if not self.HeapArray or not self.HeapArray[0]:
    	    return -1

        last_item_index = self.size - 1
        max_key = self.HeapArray[0]

        while self.HeapArray[last_item_index] is None and last_item_index >= 0:
            last_item_index -= 1

        self.HeapArray[0], self.HeapArray[last_item_index] = self.HeapArray[last_item_index], None
        self.__sifting_down(0)
        return max_key

    def __sifting_down(self, item_index):
        if item_index is None:
            return

        left_child_index = 2 * item_index + 1
        right_child_index = 2 * item_index + 2

        child_index = left_child = right_child = None

        if left_child_index <= self.size - 1:
            left_child = self.HeapArray[left_child_index]
        else:
            left_child_index = None

        if right_child_index <= self.size - 1:
            right_child = self.HeapArray[right_child_index]
        else:
            right_child_index = None

        if left_child and right_child:
            child_index = left_child_index if left_child >= right_child else right_child_index
        elif not left_child and right_child_index and self.HeapArray[right_child_index]:
            child_index = right_child_index
        elif not right_child and left_child_index and self.HeapArray[left_child_index]:
            child_index = left_child_index

        if child_index and self.HeapArray[child_index] > self.HeapArray[item_index]:
            self.HeapArray[item_index], self.HeapArray[child_index] = self.HeapArray[child_index], self.HeapArray[item_index]

        self.__sifting_down(child_index)

    def Add(self, key: int) -> bool:
        new_item_index = self.size - 1

        if self.HeapArray[new_item_index]:
            return False

        while self.HeapArray[new_item_index] is None and new_item_index >= 0:
            new_item_index -= 1

        new_item_index += 1
        self.HeapArray[new_item_index] = key

        self.__sifting_up(new_item_index)

        return True

    def __sifting_up(self, item_index: int) -> None:
        if item_index <= 0:
            return

        if item_index % 2 == 0:
            parent_index = (item_index - 2) // 2
        else:
            parent_index = (item_index - 1) // 2

        if self.HeapArray[parent_index] < self.HeapArray[item_index]:
            self.HeapArray[item_index], self.HeapArray[parent_index] = self.HeapArray[parent_index], self.HeapArray[item_index]

        self.__sifting_up(parent_index)

