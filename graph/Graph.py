class Vertex:

    def __init__(self, val):
        self.Value = val

class SimpleGraph:

    def __init__(self, size: int) -> None:
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v) -> None:
        pass

    def RemoveVertex(self, v: int) -> None:
        pass

    def IsEdge(self, v1: int, v2: int) -> bool:
        return False

    def AddEdge(self, v1: int, v2: int) -> None:
        pass

    def RemoveEdge(self, v1: int, v2: int) -> None:
        pass
