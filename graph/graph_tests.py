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
