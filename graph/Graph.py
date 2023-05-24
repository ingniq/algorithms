class Vertex:

    def __init__(self, val):
        self.Value = val

class SimpleGraph:

    def __init__(self, size: int) -> None:
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v: int) -> None:
        if not self.vertex:
            return

        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return

    def RemoveVertex(self, v: int) -> None:
        if not self.vertex or v >= len(self.vertex) or v < 0:
            return

        if self.vertex[v]:
            self.vertex[v] = None
            self.m_adjacency[v] = [0] * self.max_vertex

            for i in range(self.max_vertex):
                self.m_adjacency[i][v] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        if not self.vertex:
            return False

        if v1 >= self.max_vertex or v2 >= self.max_vertex:
            return False

        if v1 < 0 or v2 < 0:
            return False

        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1: int, v2: int) -> None:
        if not self.vertex:
            return

        if v1 >= self.max_vertex or v2 >= self.max_vertex:
            return

        if v1 < 0 or v2 < 0:
            return

        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        if not self.vertex:
            return

        if v1 >= self.max_vertex or v2 >= self.max_vertex:
            return

        if v1 < 0 or v2 < 0:
            return

        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
