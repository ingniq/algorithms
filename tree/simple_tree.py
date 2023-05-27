class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
        self.level = 0

class SimpleTree:

    def __init__(self, root: SimpleTreeNode) -> None:
        self.Root = root

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode) -> None:
        if not ParentNode or not NewChild:
            return None

        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        self.update_node_levels(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode) -> None:
        if NodeToDelete == self.Root:
            return None

        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self) -> list:
        if self.Root is None:
            return []

        return [self.Root] + self.__find_nodes(self.Root.Children, 0, None)

    def FindNodesByValue(self, val) -> list:
        if self.Root is None:
            return []

        found = []

        if self.Root.NodeValue == val:
            found.append(self.Root)

        return found + self.__find_nodes(self.Root.Children, 0, val)

    def __find_nodes(self, nodes: list, index: int, val) -> list:
        if index >= len(nodes):
            return []

        found = []

        if val is not None and nodes[index].NodeValue == val:
            found.append(nodes[index])
        elif val is None:
            found.append(nodes[index])

        if nodes[index].Children:
            found += self.__find_nodes(nodes[index].Children, 0, val)

        return found + self.__find_nodes(nodes, index + 1, val)

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode) -> None:
        if self.Root is None or OriginalNode == self.Root:
            return None

        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
        self.update_node_levels(OriginalNode)

    def update_node_levels(self, start_node: SimpleTreeNode) -> None:
        self.__update_node_levels_recursively([start_node], 0)

    def __update_node_levels_recursively(self, nodes: list, index: int) -> None:
        if index >= len(nodes):
            return None

        if nodes[index].Parent is None:
            nodes[index].level = 0
        else:
            nodes[index].level = nodes[index].Parent.level + 1

        if nodes[index].Children:
            self.__update_node_levels_recursively(nodes[index].Children, 0)

        return self.__update_node_levels_recursively(nodes, index + 1)

    def Count(self) -> int:
        if self.Root is None:
            return 0
        return self.__items_counter(nodes=[self.Root], index=0, only_leaves=False)

    def LeafCount(self) -> int:
        if self.Root is None:
            return 0
        return self.__items_counter(nodes=[self.Root], index=0, only_leaves=True)

    def __items_counter(self, *, nodes: list, index: int, only_leaves: bool) -> int:
        if index >= len(nodes):
            return 0

        num_items = 0

        if not only_leaves or not nodes[index].Children:
            num_items += 1

        if nodes[index].Children:
            num_items += self.__items_counter(nodes=nodes[index].Children, index=0, only_leaves=only_leaves)

        return num_items + self.__items_counter(nodes=nodes, index=index + 1, only_leaves=only_leaves)

    def EvenTrees(self) -> list:
        if self.Count() % 2 != 0:
            return []

        edges_to_delete = []
        stack = [self.Root]

        while stack:
            node = stack.pop(0)

            if node.Parent and self.__items_counter(nodes=[node], index=0, only_leaves=False) % 2 == 0:
                edges_to_delete.append(node.Parent)
                edges_to_delete.append(node)

            stack.extend(node.Children)

        return edges_to_delete
