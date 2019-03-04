from queue import *

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

    def add_directed_edge(self, item, other):
        # check if vertices exist
        # if not, do nothing
        if not item in self.vertices and not other in self.vertices:
            pass
        # if so, add edge
        else:
            self.vertices[item].add(other)

    def breadth_first_traversal(self):
        # grab keys to all vertices/nodes
        nodes = [*self.vertices]
        # if none exist, do nothing
        if not len(nodes):
            pass
        # otherwise, traverse them
        else:
            start = nodes[0]
            visited = set()
            queue = Queue()
            queue.put(start)

            while not queue.empty():
                current = queue.get()
                print(current)
                visited.add(current)
                for neighbor in self.vertices[current]:
                    if neighbor not in visited:
                        queue.put(neighbor)

    def depth_first_traversal(self):
        # grab keys to all vertices/nodes
        nodes = [*self.vertices]
        # if none exist, do nothing
        if not len(nodes):
            pass
        # otherwise, traverse them
        else:
            start = nodes[0]
            visited = set()
            stack = []
            stack.append(start)

            while len(stack):
                current = stack.pop()
                if current not in visited:
                    print(current)
                    visited.add(current)
                    for neighbor in self.vertices[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)

    def recursive_depth_first_traversal(self, current=None, visited=set()):
        if not current:
            try:
                current = [*self.vertices][0]
            except IndexError:
                pass

        print(current)
        visited.add(current)
        for neighbor in self.vertices[current]:
            if neighbor not in visited:
                self.recursive_depth_first_traversal(neighbor, visited)

    def breadth_first_search(self, start, end):
        # check that start and end exist
        # set current to start
        # add paths to queue as we traverse the graph
        # update the paths as we go and add them back to the queue
        # all paths will either fail to reach the end or reach the end
        # when they succeed, we add them to the paths array
        # we then pull out the shortest path
        if not start in self.vertices or not end in self.vertices:
            pass
        else:
            paths = []
            queue = Queue()
            queue.put([start])

            while not queue.empty():
                current_path = queue.get()
                current = current_path[-1]

                if current == end:
                    paths.append(current_path)
                else:
                    for item in self.vertices[current]:
                        if item not in current_path:
                            queue.put(list(current_path) + [item])

            paths.sort(key=len)
            print(paths)
            return paths[0]

    def depth_first_search(self):
        pass


# set up graph
graph = Graph()  # Instantiate your graph
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_directed_edge('5', '3')
graph.add_directed_edge('6', '3')
graph.add_directed_edge('7', '1')
graph.add_directed_edge('4', '7')
graph.add_directed_edge('1', '2')
graph.add_directed_edge('7', '6')
graph.add_directed_edge('2', '4')
graph.add_directed_edge('3', '5')
graph.add_directed_edge('2', '3')
graph.add_directed_edge('4', '6')

# run breadth_first_traversal
print('running breadth first traversal')
graph.breadth_first_traversal()

# run depth_first_traversal
print('running depth first traversal')
graph.depth_first_traversal()

# run recursive_depth_first_traversal
print('running recursive depth first traversal')
graph.recursive_depth_first_traversal()

# run breadth_first_search
print('running breadth first search')
print(graph.breadth_first_search('1', '7'))
print(graph.breadth_first_search('7', '4'))
print(graph.breadth_first_search('4', '6'))
