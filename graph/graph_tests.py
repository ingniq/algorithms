from unittest import TestCase
from Graph import SimpleGraph

class GraphTests(TestCase):

    def test_create(self):
        graph = SimpleGraph(0)

        self.assertEqual(graph.max_vertex, 0)
        self.assertListEqual(graph.m_adjacency, [])
        self.assertListEqual(graph.vertex, [])

        graph = SimpleGraph(1)

        self.assertEqual(graph.max_vertex, 1)
        self.assertListEqual(graph.m_adjacency, [[0]])
        self.assertListEqual(graph.vertex, [None])

        graph = SimpleGraph(5)

        self.assertEqual(graph.max_vertex, 5)
        self.assertEqual(len(graph.m_adjacency), 5)

        self.assertListEqual(graph.m_adjacency,
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )

        self.assertListEqual(graph.vertex, [None, None, None, None, None])

    def test_AddVertex(self):
        graph = SimpleGraph(0)
        graph.AddVertex(1)

        self.assertListEqual(graph.m_adjacency, [])
        self.assertListEqual(graph.vertex, [])

        graph = SimpleGraph(1)
        vertex = 1
        graph.AddVertex(vertex)

        self.assertListEqual(graph.m_adjacency, [[0]])
        self.assertEqual(graph.vertex[0].Value, vertex)

        graph = SimpleGraph(5)
        vertex_1 = 1
        graph.AddVertex(vertex_1)

        self.assertEqual(len(graph.m_adjacency), 5)

        self.assertListEqual(graph.m_adjacency,
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )

        self.assertEqual(graph.vertex[0].Value, vertex_1)
        for i in range(1, graph.max_vertex):
            self.assertIsNone(graph.vertex[i])

        vertex_2 = 2
        graph.AddVertex(vertex_2)
        self.assertEqual(graph.vertex[0].Value, vertex_1)
        self.assertEqual(graph.vertex[1].Value, vertex_2)
        for i in range(2, graph.max_vertex):
            self.assertIsNone(graph.vertex[i])

        vertex_3 = 3
        graph.AddVertex(vertex_3)
        self.assertEqual(graph.vertex[0].Value, vertex_1)
        self.assertEqual(graph.vertex[1].Value, vertex_2)
        self.assertEqual(graph.vertex[2].Value, vertex_3)
        for i in range(3, graph.max_vertex):
            self.assertIsNone(graph.vertex[i])

        vertex_4 = 4
        graph.AddVertex(vertex_4)
        self.assertEqual(graph.vertex[0].Value, vertex_1)
        self.assertEqual(graph.vertex[1].Value, vertex_2)
        self.assertEqual(graph.vertex[2].Value, vertex_3)
        self.assertEqual(graph.vertex[3].Value, vertex_4)
        for i in range(4, graph.max_vertex):
            self.assertIsNone(graph.vertex[i])

        graph.AddVertex(vertex_4)
        self.assertEqual(graph.vertex[0].Value, vertex_1)
        self.assertEqual(graph.vertex[1].Value, vertex_2)
        self.assertEqual(graph.vertex[2].Value, vertex_3)
        self.assertEqual(graph.vertex[3].Value, vertex_4)
        self.assertEqual(graph.vertex[4].Value, vertex_4)

        vertex_6 = 6
        graph.AddVertex(vertex_6)
        self.assertEqual(graph.vertex[0].Value, vertex_1)
        self.assertEqual(graph.vertex[1].Value, vertex_2)
        self.assertEqual(graph.vertex[2].Value, vertex_3)
        self.assertEqual(graph.vertex[3].Value, vertex_4)
        self.assertEqual(graph.vertex[4].Value, vertex_4)

    def test_RemoveVertex(self):
        graph = SimpleGraph(0)
        graph.RemoveVertex(1)

        graph = SimpleGraph(1)
        vertex = 1
        graph.AddVertex(vertex)

        self.assertListEqual(graph.m_adjacency, [[0]])
        self.assertEqual(graph.vertex[0].Value, 1)

        graph.RemoveVertex(1)
        self.assertListEqual(graph.m_adjacency, [[0]])
        self.assertEqual(graph.vertex[0].Value, 1)

        graph.RemoveVertex(0)
        self.assertListEqual(graph.m_adjacency, [[0]])
        self.assertIsNone(graph.vertex[0])

        graph = SimpleGraph(5)
        vertex_0 = 0
        vertex_1 = 1
        vertex_2 = 2
        vertex_3 = 3
        vertex_4 = 4
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)
        graph.AddVertex(vertex_2)
        graph.AddVertex(vertex_3)
        graph.AddVertex(vertex_4)

        #  0   1
        #          4
        #  2   3

        self.assertListEqual(graph.m_adjacency,
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
        self.assertEqual(graph.vertex[0].Value, vertex_0)
        self.assertEqual(graph.vertex[1].Value, vertex_1)
        self.assertEqual(graph.vertex[2].Value, vertex_2)
        self.assertEqual(graph.vertex[3].Value, vertex_3)
        self.assertEqual(graph.vertex[4].Value, vertex_4)

        graph.RemoveVertex(0)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
        self.assertIsNone(graph.vertex[0])
        self.assertEqual(graph.vertex[1].Value, vertex_1)
        self.assertEqual(graph.vertex[2].Value, vertex_2)
        self.assertEqual(graph.vertex[3].Value, vertex_3)
        self.assertEqual(graph.vertex[4].Value, vertex_4)

        graph.RemoveVertex(2)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
        self.assertIsNone(graph.vertex[0])
        self.assertEqual(graph.vertex[1].Value, vertex_1)
        self.assertIsNone(graph.vertex[2])
        self.assertEqual(graph.vertex[3].Value, vertex_3)
        self.assertEqual(graph.vertex[4].Value, vertex_4)

        graph.RemoveVertex(4)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
        self.assertIsNone(graph.vertex[0])
        self.assertEqual(graph.vertex[1].Value, vertex_1)
        self.assertIsNone(graph.vertex[2])
        self.assertEqual(graph.vertex[3].Value, vertex_3)
        self.assertIsNone(graph.vertex[4])

        graph.AddVertex(vertex_4)
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_2)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(0, 3)
        graph.AddEdge(1, 3)
        graph.AddEdge(1, 4)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 3)
        graph.AddEdge(3, 4)

        #  4---1\
        #  |\  | \
        #  | \ |  2
        #  |  \| /
        #  0---3/
        #     /_\

        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 0, 1, 0]
            ]
        )
        self.assertEqual(graph.vertex[0].Value, vertex_4)
        self.assertEqual(graph.vertex[1].Value, vertex_1)
        self.assertEqual(graph.vertex[2].Value, vertex_0)
        self.assertEqual(graph.vertex[3].Value, vertex_3)
        self.assertEqual(graph.vertex[4].Value, vertex_2)

        graph.RemoveVertex(0)

        #      1\
        #      | \
        #      |  2
        #      | /
        #  0---3/
        #     /_\

        self.assertListEqual(graph.m_adjacency,
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 1, 1],
                [0, 1, 0, 1, 0]
            ]
        )
        self.assertIsNone(graph.vertex[0])
        self.assertEqual(graph.vertex[1].Value, vertex_1)
        self.assertEqual(graph.vertex[2].Value, vertex_0)
        self.assertEqual(graph.vertex[3].Value, vertex_3)
        self.assertEqual(graph.vertex[4].Value, vertex_2)

        graph.RemoveVertex(3)

        #      1\
        #        \
        #         2
        #
        #  0

        self.assertListEqual(graph.m_adjacency,
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0]
            ]
        )
        self.assertIsNone(graph.vertex[0])
        self.assertEqual(graph.vertex[1].Value, vertex_1)
        self.assertEqual(graph.vertex[2].Value, vertex_0)
        self.assertIsNone(graph.vertex[3])
        self.assertEqual(graph.vertex[4].Value, vertex_2)

    def test_IsEdge(self):
        graph = SimpleGraph(6)
        vertex_0 = 0
        vertex_1 = 1
        vertex_2 = 2
        vertex_3 = 3
        vertex_4 = 4
        vertex_5 = 5
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)
        graph.AddVertex(vertex_2)
        graph.AddVertex(vertex_3)
        graph.AddVertex(vertex_4)
        graph.AddVertex(vertex_5)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(0, 3)
        graph.AddEdge(1, 3)
        graph.AddEdge(1, 4)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 3)
        graph.AddEdge(3, 4)

        #  0---1\
        #  |\  | \
        #  | \ |  4    5
        #  |  \| /
        #  2---3/
        #     /_\

        self.assertFalse(graph.IsEdge(0, 0))
        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(0, 2))
        self.assertTrue(graph.IsEdge(0, 3))
        self.assertFalse(graph.IsEdge(0, 4))
        self.assertFalse(graph.IsEdge(0, 5))

        self.assertTrue(graph.IsEdge(1, 0))
        self.assertFalse(graph.IsEdge(1, 1))
        self.assertFalse(graph.IsEdge(1, 2))
        self.assertTrue(graph.IsEdge(1, 3))
        self.assertTrue(graph.IsEdge(1, 4))
        self.assertFalse(graph.IsEdge(1, 5))

        self.assertTrue(graph.IsEdge(2, 0))
        self.assertFalse(graph.IsEdge(2, 1))
        self.assertFalse(graph.IsEdge(2, 2))
        self.assertTrue(graph.IsEdge(2, 3))
        self.assertFalse(graph.IsEdge(2, 4))
        self.assertFalse(graph.IsEdge(2, 5))

        self.assertTrue(graph.IsEdge(3, 0))
        self.assertTrue(graph.IsEdge(3, 1))
        self.assertTrue(graph.IsEdge(3, 2))
        self.assertTrue(graph.IsEdge(3, 3))
        self.assertTrue(graph.IsEdge(3, 4))
        self.assertFalse(graph.IsEdge(3, 5))

        self.assertFalse(graph.IsEdge(4, 0))
        self.assertTrue(graph.IsEdge(4, 1))
        self.assertFalse(graph.IsEdge(4, 2))
        self.assertTrue(graph.IsEdge(4, 3))
        self.assertFalse(graph.IsEdge(4, 4))
        self.assertFalse(graph.IsEdge(4, 5))

        self.assertFalse(graph.IsEdge(5, 0))
        self.assertFalse(graph.IsEdge(5, 1))
        self.assertFalse(graph.IsEdge(5, 2))
        self.assertFalse(graph.IsEdge(5, 3))
        self.assertFalse(graph.IsEdge(5, 4))
        self.assertFalse(graph.IsEdge(5, 5))


    def test_AddEdge(self):
        vertex_0 = 0
        vertex_1 = 1
        vertex_2 = 2
        vertex_3 = 3
        vertex_4 = 4

        graph = SimpleGraph(0)
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)
        graph.AddEdge(0, 1)
        self.assertListEqual(graph.m_adjacency,[])

        graph = SimpleGraph(1)
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)

        graph.AddEdge(0, 1)
        self.assertListEqual(graph.m_adjacency, [[0]])
        graph.AddEdge(0, 0)
        self.assertListEqual(graph.m_adjacency, [[1]])

        graph = SimpleGraph(5)
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)
        graph.AddVertex(vertex_2)
        graph.AddVertex(vertex_3)
        graph.AddVertex(vertex_4)

        #  0   1
        #
        #         4
        #
        #  2   3

        self.assertListEqual(graph.m_adjacency,
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )

        graph.AddEdge(0, 1)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
        graph.AddEdge(0, 2)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
        graph.AddEdge(0, 3)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
        graph.AddEdge(1, 3)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
        graph.AddEdge(1, 4)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0]
            ]
        )
        graph.AddEdge(2, 3)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 0, 0],
                [0, 1, 0, 0, 0]
            ]
        )
        graph.AddEdge(3, 3)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0]
            ]
        )
        graph.AddEdge(3, 4)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 0, 1, 0]
            ]
        )

        #  0---1\
        #  |\  | \
        #  | \ |  4
        #  |  \| /
        #  2---3/
        #     /_\


    def test_RemoveEdge(self):
        vertex_0 = 0
        vertex_1 = 1
        vertex_2 = 2
        vertex_3 = 3
        vertex_4 = 4

        graph = SimpleGraph(0)
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)

        graph.RemoveEdge(0, 1)
        self.assertListEqual(graph.m_adjacency,[])
        graph.RemoveEdge(0, 0)
        self.assertListEqual(graph.m_adjacency,[])

        graph = SimpleGraph(1)
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)
        graph.AddEdge(0, 0)
        self.assertListEqual(graph.m_adjacency, [[1]])
        graph.RemoveEdge(0, 0)
        self.assertListEqual(graph.m_adjacency,[[0]])

        graph = SimpleGraph(5)
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)
        graph.AddVertex(vertex_2)
        graph.AddVertex(vertex_3)
        graph.AddVertex(vertex_4)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(0, 3)
        graph.AddEdge(1, 3)
        graph.AddEdge(1, 4)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 3)
        graph.AddEdge(3, 4)

        #  0---1\
        #  |\  | \
        #  | \ |  4
        #  |  \| /
        #  2---3/
        #     /_\

        graph.RemoveEdge(3, 3)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 0, 1],
                [0, 1, 0, 1, 0]
            ]
        )

        #  0---1\
        #  |\  | \
        #  | \ |  4
        #  |  \| /
        #  2---3/

        graph.RemoveEdge(3, 4)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 0, 0],
                [0, 1, 0, 0, 0]
            ]
        )

        #  0---1\
        #  |\  | \
        #  | \ |  4
        #  |  \|
        #  2---3

        graph.RemoveEdge(1, 2)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 0, 0],
                [0, 1, 0, 0, 0]
            ]
        )

        #  0---1\
        #  |\  | \
        #  | \ |  4
        #  |  \|
        #  2---3

        graph.RemoveEdge(3, 0)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 0, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 0, 0, 0]
            ]
        )

        #  0---1\
        #  |   | \
        #  |   |  4
        #  |   |
        #  2---3

        graph.RemoveEdge(3, 1)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 1, 1, 0, 0],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0]
            ]
        )

        #  0---1\
        #  |     \
        #  |      4
        #  |
        #  2---3

        graph.RemoveEdge(0, 1)
        self.assertListEqual(graph.m_adjacency,
            [
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1],
                [1, 0, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0]
            ]
        )

        #  0   1\
        #  |     \
        #  |      4
        #  |
        #  2---3


    def test_DepthFirstSearch(self):
        vertex_0 = 0
        vertex_1 = 1
        vertex_2 = 2
        vertex_3 = 3
        vertex_4 = 4
        vertex_5 = 5
        vertex_6 = 6
        vertex_7 = 7
        vertex_8 = 8
        vertex_9 = 9
        vertex_10 = 10

        graph = SimpleGraph(1)
        path = graph.DepthFirstSearch(vertex_0, vertex_0)
        self.assertListEqual(path, [])

        graph.AddVertex(vertex_0)

        path = graph.DepthFirstSearch(vertex_0, vertex_0)
        self.assertListEqual(path, [])

        path = graph.DepthFirstSearch(vertex_0, vertex_3)
        self.assertListEqual(path, [])

        path = graph.DepthFirstSearch(vertex_3, vertex_3)
        self.assertListEqual(path, [])

        graph.AddEdge(0, 0)
        path = graph.DepthFirstSearch(vertex_0, vertex_0)
        self.assertEqual(path[0].Value, 0)
        self.assertEqual(path[1].Value, 0)

        graph = SimpleGraph(11)
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)
        graph.AddVertex(vertex_2)
        graph.AddVertex(vertex_3)
        graph.AddVertex(vertex_4)
        graph.AddVertex(vertex_5)
        graph.AddVertex(vertex_6)
        graph.AddVertex(vertex_7)
        graph.AddVertex(vertex_8)
        graph.AddVertex(vertex_9)
        graph.AddVertex(vertex_10)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(0, 3)
        graph.AddEdge(1, 3)
        graph.AddEdge(1, 4)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 3)
        graph.AddEdge(3, 4)
        graph.AddEdge(3, 5)
        graph.AddEdge(4, 8)
        graph.AddEdge(5, 6)
        graph.AddEdge(5, 8)
        graph.AddEdge(6, 7)
        graph.AddEdge(7, 8)
        graph.AddEdge(7, 9)
        graph.AddEdge(7, 10)

        #  0---1\         10
        #  |\  | \        |
        #  | \ |  4--8----7----9
        #  |  \| /   |    |
        #  2---3/----5----6
        #     /_\

        path = graph.DepthFirstSearch(vertex_3, vertex_3)
        self.assertEqual(path[0].Value, 3)
        self.assertEqual(path[1].Value, 3)

        path = graph.DepthFirstSearch(vertex_0, vertex_3)
        self.assertEqual(path[0].Value, 0)
        self.assertEqual(path[1].Value, 3)

        path = graph.DepthFirstSearch(vertex_0, vertex_4)
        self.assertEqual(path[0].Value, 0)
        self.assertEqual(path[1].Value, 1)
        self.assertEqual(path[2].Value, 4)

        path = graph.DepthFirstSearch(vertex_4, vertex_0)
        self.assertEqual(path[0].Value, 4)
        self.assertEqual(path[1].Value, 1)
        self.assertEqual(path[2].Value, 0)

        path = graph.DepthFirstSearch(vertex_2, vertex_4)
        self.assertEqual(path[0].Value, 2)
        self.assertEqual(path[1].Value, 0)
        self.assertEqual(path[2].Value, 1)
        self.assertEqual(path[3].Value, 4)

        path = graph.DepthFirstSearch(vertex_2, vertex_0)
        self.assertEqual(path[0].Value, 2)
        self.assertEqual(path[1].Value, 0)

        path = graph.DepthFirstSearch(vertex_2, vertex_10)
        self.assertEqual(path[0].Value, 2)
        self.assertEqual(path[1].Value, 0)
        self.assertEqual(path[2].Value, 1)
        self.assertEqual(path[3].Value, 3)
        self.assertEqual(path[4].Value, 4)
        self.assertEqual(path[5].Value, 8)
        self.assertEqual(path[6].Value, 5)
        self.assertEqual(path[7].Value, 6)
        self.assertEqual(path[8].Value, 7)
        self.assertEqual(path[9].Value, 10)

        path = graph.DepthFirstSearch(vertex_10, vertex_2)
        self.assertEqual(path[0].Value, 10)
        self.assertEqual(path[1].Value, 7)
        self.assertEqual(path[2].Value, 6)
        self.assertEqual(path[3].Value, 5)
        self.assertEqual(path[4].Value, 3)
        self.assertEqual(path[5].Value, 2)


    def test_BreadthFirstSearch(self):
        vertex_0 = 0
        vertex_1 = 1
        vertex_2 = 2
        vertex_3 = 3
        vertex_4 = 4
        vertex_5 = 5
        vertex_6 = 6
        vertex_7 = 7
        vertex_8 = 8
        vertex_9 = 9
        vertex_10 = 10

        graph = SimpleGraph(1)
        path = graph.BreadthFirstSearch(vertex_0, vertex_0)
        self.assertListEqual(path, [])

        graph.AddVertex(vertex_0)

        path = graph.BreadthFirstSearch(vertex_0, vertex_0)
        self.assertListEqual(path, [])

        path = graph.BreadthFirstSearch(vertex_0, vertex_3)
        self.assertListEqual(path, [])

        path = graph.BreadthFirstSearch(vertex_3, vertex_3)
        self.assertListEqual(path, [])

        graph.AddEdge(0, 0)
        path = graph.BreadthFirstSearch(vertex_0, vertex_0)
        self.assertEqual(path[0].Value, 0)
        self.assertEqual(path[1].Value, 0)

        graph = SimpleGraph(11)
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)
        graph.AddVertex(vertex_2)
        graph.AddVertex(vertex_3)
        graph.AddVertex(vertex_4)
        graph.AddVertex(vertex_5)
        graph.AddVertex(vertex_6)
        graph.AddVertex(vertex_7)
        graph.AddVertex(vertex_8)
        graph.AddVertex(vertex_9)
        graph.AddVertex(vertex_10)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(0, 3)
        graph.AddEdge(1, 3)
        graph.AddEdge(1, 4)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 3)
        graph.AddEdge(3, 4)
        graph.AddEdge(3, 5)
        graph.AddEdge(4, 8)
        graph.AddEdge(5, 6)
        graph.AddEdge(5, 8)
        graph.AddEdge(6, 7)
        graph.AddEdge(7, 8)
        graph.AddEdge(7, 9)
        graph.AddEdge(7, 10)

        #  0---1\         10
        #  |\  | \        |
        #  | \ |  4--8----7----9
        #  |  \| /   |    |
        #  2---3/----5----6
        #     /_\

        path = graph.BreadthFirstSearch(vertex_3, vertex_3)
        self.assertEqual(path[0].Value, 3)
        self.assertEqual(path[1].Value, 3)

        path = graph.BreadthFirstSearch(vertex_0, vertex_3)
        self.assertEqual(path[0].Value, 0)
        self.assertEqual(path[1].Value, 3)

        path = graph.BreadthFirstSearch(vertex_0, vertex_4)
        self.assertEqual(path[0].Value, 0)
        self.assertEqual(path[1].Value, 1)
        self.assertEqual(path[2].Value, 4)

        path = graph.BreadthFirstSearch(vertex_4, vertex_0)
        self.assertEqual(path[0].Value, 4)
        self.assertEqual(path[1].Value, 1)
        self.assertEqual(path[2].Value, 0)

        path = graph.BreadthFirstSearch(vertex_2, vertex_4)
        self.assertEqual(path[0].Value, 2)
        self.assertEqual(path[1].Value, 3)
        self.assertEqual(path[2].Value, 4)

        path = graph.BreadthFirstSearch(vertex_2, vertex_0)
        self.assertEqual(path[0].Value, 2)
        self.assertEqual(path[1].Value, 0)

        path = graph.BreadthFirstSearch(vertex_2, vertex_10)
        self.assertEqual(path[0].Value, 2)
        self.assertEqual(path[1].Value, 3)
        self.assertEqual(path[2].Value, 4)
        self.assertEqual(path[3].Value, 8)
        self.assertEqual(path[4].Value, 7)
        self.assertEqual(path[5].Value, 10)

        path = graph.BreadthFirstSearch(vertex_10, vertex_2)
        self.assertEqual(path[0].Value, 10)
        self.assertEqual(path[1].Value, 7)
        self.assertEqual(path[2].Value, 6)
        self.assertEqual(path[3].Value, 5)
        self.assertEqual(path[4].Value, 3)
        self.assertEqual(path[5].Value, 2)

    def test_WeakVertices(self):
        vertex_0 = 0
        vertex_1 = 1
        vertex_2 = 2
        vertex_3 = 3
        vertex_4 = 4
        vertex_5 = 5
        vertex_6 = 6
        vertex_7 = 7
        vertex_8 = 8
        vertex_9 = 9
        vertex_10 = 10

        graph = SimpleGraph(1)
        self.assertListEqual(graph.WeakVertices(), [])

        graph.AddVertex(vertex_0)
        weak_vertices = graph.WeakVertices()
        self.assertEqual(weak_vertices[0].Value, 0)

        graph = SimpleGraph(2)
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)

        weak_vertices = graph.WeakVertices()
        self.assertEqual(weak_vertices[0].Value, 0)
        self.assertEqual(weak_vertices[1].Value, 1)

        graph = SimpleGraph(4)
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)
        graph.AddVertex(vertex_2)
        graph.AddVertex(vertex_3)

        weak_vertices = graph.WeakVertices()
        self.assertEqual(weak_vertices[0].Value, 0)
        self.assertEqual(weak_vertices[1].Value, 1)
        self.assertEqual(weak_vertices[2].Value, 2)

        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(0, 3)

        weak_vertices = graph.WeakVertices()
        self.assertEqual(weak_vertices[0].Value, 0)
        self.assertEqual(weak_vertices[1].Value, 1)
        self.assertEqual(weak_vertices[2].Value, 2)

        graph.AddEdge(1, 3)
        weak_vertices = graph.WeakVertices()
        self.assertEqual(weak_vertices[0].Value, 2)

        graph.AddEdge(1, 2)
        self.assertListEqual(graph.WeakVertices(), [])

        graph = SimpleGraph(11)
        graph.AddVertex(vertex_0)
        graph.AddVertex(vertex_1)
        graph.AddVertex(vertex_2)
        graph.AddVertex(vertex_3)
        graph.AddVertex(vertex_4)
        graph.AddVertex(vertex_5)
        graph.AddVertex(vertex_6)
        graph.AddVertex(vertex_7)
        graph.AddVertex(vertex_8)
        graph.AddVertex(vertex_9)
        graph.AddVertex(vertex_10)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(0, 3)
        graph.AddEdge(1, 3)
        graph.AddEdge(1, 4)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 3)
        graph.AddEdge(3, 4)
        graph.AddEdge(3, 5)
        graph.AddEdge(4, 8)
        graph.AddEdge(5, 6)
        graph.AddEdge(5, 8)
        graph.AddEdge(6, 7)
        graph.AddEdge(7, 8)
        graph.AddEdge(7, 9)
        graph.AddEdge(7, 10)

        #  0---1\         10
        #  |\  | \        |
        #  | \ |  4--8----7----9
        #  |  \| /   |    |
        #  2---3/----5----6
        #     /_\

        weak_vertices = graph.WeakVertices()
        self.assertEqual(weak_vertices[0].Value, 5)
        self.assertEqual(weak_vertices[1].Value, 6)
        self.assertEqual(weak_vertices[2].Value, 7)
        self.assertEqual(weak_vertices[3].Value, 8)
        self.assertEqual(weak_vertices[4].Value, 9)
        self.assertEqual(weak_vertices[5].Value, 10)
