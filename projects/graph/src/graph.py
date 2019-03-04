"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, item):
        # check if vertex exists
        # if so, do nothing
        if item in self.vertices:
            pass
        # else, add vertex
        else:
            self.vertices[item] = set()

    def add_edge(self, item, other):
        # check if vertices exist
        # if not, do nothing
        if not item in self.vertices and not other in self.vertices:
            pass
        # if so, add edge
        else:
            self.vertices[item].add(other)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
