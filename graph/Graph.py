class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False

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

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> list:
        if VFrom >= self.max_vertex or VTo >= self.max_vertex:
            return []

        for vertex in self.vertex:
            if vertex:
                vertex.Hit = False

        return self.__depth_first_path_search(VFrom, VTo)

    def __depth_first_path_search(self, VFrom: int, VTo: int):
        vertex_from = self.vertex[VFrom]
        vertex_to = self.vertex[VTo]

        if vertex_from is None or vertex_to is None:
            return []

        stack = []
        vertex_from.Hit = True
        stack.append(vertex_from)

        if self.m_adjacency[VFrom][VTo] == 1:
            stack.append(vertex_to)
            return stack

        next_vertex = None

        for j in range(self.max_vertex):
            if self.m_adjacency[VFrom][j] == 1 and self.vertex[j].Hit is False:
                next_vertex = j
                break

        if next_vertex is None:
            return []

        next_step = self.__depth_first_path_search(next_vertex, VTo)

        if not next_step and stack:
            next_step = self.__depth_first_path_search(stack.pop().Value, VTo)

        return stack + next_step

    def BreadthFirstSearch(self, VFrom: int, VTo: int):
        if VFrom >= self.max_vertex or VTo >= self.max_vertex:
            return []

        for vertex in self.vertex:
            if vertex:
                vertex.Hit = False

        vertex_from = self.vertex[VFrom]
        vertex_to = self.vertex[VTo]

        if vertex_from is None or vertex_to is None:
            return []

        if self.m_adjacency[VFrom][VTo] == 1:
            return [vertex_from, vertex_to]

        tour = {}
        queue = [VFrom]
        vertex_from.Hit = True

        while queue:
            i = queue.pop(0)

            if self.m_adjacency[i][VTo] == 1:
                tour[VTo] = i
                break

            for j in range(self.max_vertex):
                if self.m_adjacency[i][j] == 1 and self.vertex[j].Hit is False:
                    self.vertex[j].Hit = True
                    queue.append(j)
                    tour[j] = i

        if not queue and VTo not in tour:
            return []

        path = []
        item = VTo

        while item != VFrom:
            path.append(item)
            item = tour[item]

        path.append(VFrom)
        path = reversed(path)

        return [self.vertex[i] for i in path]
