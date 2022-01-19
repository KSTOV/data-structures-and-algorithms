class Graph:
    def __init__(self):
        self.adjancency_list = {}

    def size(self):
        return len(self.adjancency_list)

    def get_nodes(self):
        return list(self.adjancency_list.keys())

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjancency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if end_vertex not in self.adjancency_list:
            raise KeyError

        edge = Edge(end_vertex, weight)
        self.adjancency_list[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        return self.adjancency_list[vertex]


class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Vertex:
    def __init__(self, value):
        self.value = value
