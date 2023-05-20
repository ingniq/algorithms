class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:

    def __init__(self):
    	self.Root = None

    def GenerateTree(self, a: list) -> None:
        a = sorted(a)
        self.__generate_balanced_tree(None, a, False)

    def __generate_balanced_tree(self, parent: BSTNode, a: list, is_left: bool):
        if not a:
            return

        index = len(a) // 2
        node = BSTNode(a[index], parent)

        if parent is not None:
            node.Level = parent.Level + 1

            if is_left:
                parent.LeftChild = node
            else:
                parent.RightChild = node

        if parent is None:
            self.Root = node

        if index == 0:
            return

        self.__generate_balanced_tree(node, a[:index], True)
        self.__generate_balanced_tree(node, a[index + 1:], False)

    def IsBalanced(self, root_node: BSTNode) -> bool:
        if not root_node.LeftChild and not root_node.RightChild:
            return True

        left_depth = right_depth = 0

        if root_node.LeftChild:
            left_depth = self.__get_lowest_level_val(root_node.LeftChild) - root_node.Level

        if root_node.RightChild:
            right_depth = self.__get_lowest_level_val(root_node.RightChild) - root_node.Level

        if abs(left_depth - right_depth) > 1:
            return False

        left_is_balanced = right_is_balanced = True

        if root_node.LeftChild:
            left_is_balanced = self.IsBalanced(root_node.LeftChild)

        if root_node.RightChild:
            right_is_balanced = self.IsBalanced(root_node.RightChild)

        return left_is_balanced and right_is_balanced

    def __get_lowest_level_val(self, node: BSTNode):
        if not node.LeftChild and not node.RightChild:
            return node.Level

        depth = left_depth = right_depth = node.Level

        if node.LeftChild:
            left_depth = self.__get_lowest_level_val(node.LeftChild)

        if node.RightChild:
            right_depth = self.__get_lowest_level_val(node.RightChild)

        if left_depth >= right_depth:
            depth = left_depth
        else:
            depth = right_depth

        return depth
