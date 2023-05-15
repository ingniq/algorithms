class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False

class BST:
    TRAVERSAL_IN_ORDER = 0
    TRAVERSAL_POST_ORDER = 1
    TRAVERSAL_PRE_ORDER = 2

    def __init__(self, node: BSTNode) -> None:
        self.Root = node

    def FindNodeByKey(self, key) -> BSTFind:
        return self.__find_node_by_key(self.Root, key)

    def __find_node_by_key(self, node: BSTNode, key) -> BSTFind:
        if node is None:
            return BSTFind()

        if node.NodeKey == key:
            found = BSTFind()
            found.Node = node
            found.NodeHasKey = True
            return found

        if node.NodeKey > key and not node.LeftChild:
            found = BSTFind()
            found.Node = node
            found.ToLeft = True
            return found

        if node.NodeKey < key and not node.RightChild:
            found = BSTFind()
            found.Node = node
            return found

        node = node.LeftChild if (node.NodeKey > key) else node.RightChild

        return self.__find_node_by_key(node, key)

    def AddKeyValue(self, key, val) -> bool:
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True

        found = self.FindNodeByKey(key)

        if found and found.NodeHasKey:
            return False

        parent = found.Node

        if found.ToLeft:
            parent.LeftChild = BSTNode(key, val, parent)
        else:
            parent.RightChild = BSTNode(key, val, parent)

        return True

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> BSTNode:
        if self.Root is None:
            return None

        return self.__find_min_max(FromNode, FindMax, FromNode.NodeKey)

    def __find_min_max(self, node: BSTNode, find_max: bool, key) -> BSTNode:
        if find_max and node.NodeKey > key:
            key = node.NodeKey
        elif not find_max and node.NodeKey < key:
            key = node.NodeKey

        if find_max and not node.RightChild:
            return node
        elif not find_max and not node.LeftChild:
            return node

        node = node.RightChild if find_max else node.LeftChild

        return self.__find_min_max(node, find_max, key)

    def DeleteNodeByKey(self, key) -> bool:
        if self.Root is None:
            return False

        to_delete = self.FindNodeByKey(key)

        if not to_delete or not to_delete.NodeHasKey:
            return False

        is_root = (to_delete.Node == self.Root)
        parent = to_delete.Node.Parent

        # leaf
        if not to_delete.Node.LeftChild and not to_delete.Node.RightChild:
            if is_root:
                self.Root = None
                return True

            if parent.LeftChild == to_delete.Node:
                parent.LeftChild = None
            else:
                parent.RightChild = None

            to_delete.Node.Parent = None

        # delete node with children (successor node is left child)
        if to_delete.Node.LeftChild and not to_delete.Node.RightChild:
            if is_root:
                self.Root = to_delete.Node.LeftChild
                self.Root.Parent = None
                return True

            if parent.LeftChild == to_delete.Node:
                parent.LeftChild = to_delete.Node.LeftChild
            else:
                parent.RightChild = to_delete.Node.LeftChild

            to_delete.Node.LeftChild.Parent = parent
            to_delete.Node.Parent = None

        if to_delete.Node.RightChild:
            successor_node = self.FinMinMax(to_delete.Node.RightChild, False)

            if is_root:
                self.Root = successor_node
            elif parent.LeftChild == to_delete.Node:
                parent.LeftChild = successor_node
            else:
                parent.RightChild = successor_node

            if successor_node.RightChild and successor_node != to_delete.Node.RightChild:
                successor_node.Parent.LeftChild = successor_node.RightChild
                successor_node.RightChild.Parent = successor_node.Parent
            else:
                successor_node.Parent.LeftChild = None

            successor_node.RightChild = to_delete.Node.RightChild
            successor_node.LeftChild = to_delete.Node.LeftChild
            successor_node.RightChild.Parent = successor_node

            if successor_node.LeftChild:
                successor_node.LeftChild.Parent = successor_node

            successor_node.Parent = parent
            to_delete.Node.Parent = None

        return True

    def Count(self) -> int:
        return self.__item_counter(self.Root)

    def __item_counter(self, node: BSTNode) -> int:
        if node is None:
            return 0

        count = 1 + self.__item_counter(node.LeftChild)

        return count + self.__item_counter(node.RightChild)

    def WideAllNodes(self)-> tuple:
        return self.__wide_traversal(self.Root)

    def __wide_traversal(self, node: BSTNode) -> tuple:
        if node is None:
            return tuple()

        nodes = tuple()
        queue = [node]

        while queue:
            node = queue.pop(0)
            nodes += (node,)

            if node.LeftChild:
                queue.append(node.LeftChild)

            if node.RightChild:
                queue.append(node.RightChild)

        return nodes

    def DeepAllNodes(self, order: int) -> tuple:
        return self.__deep_traversal(self.Root, order)

    def __deep_traversal(self, node: BSTNode, order: int) -> tuple:
        if node is None:
            return tuple()

        nodes = tuple()

        if order == self.TRAVERSAL_IN_ORDER:
            nodes += self.__deep_traversal(node.LeftChild, order)
            nodes += (node,)
            nodes += self.__deep_traversal(node.RightChild, order)
        elif order == self.TRAVERSAL_POST_ORDER:
            nodes += self.__deep_traversal(node.LeftChild, order)
            nodes += self.__deep_traversal(node.RightChild, order)
            nodes += (node,)
        elif order == self.TRAVERSAL_PRE_ORDER:
            nodes += (node,)
            nodes += self.__deep_traversal(node.LeftChild, order)
            nodes += self.__deep_traversal(node.RightChild, order)

        return nodes
