"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):

        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise Exception("vertex does not exist")

    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            current = q.dequeue()
            if current not in visited:
                print(current)
                visited.add(current)
                for neighbor in self.get_neighbors(current):

                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            current = s.pop()
            if current not in visited:
                print(current)
                visited.add(current)
                for neighbor in self.get_neighbors(current):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)

        edges = self.get_neighbors(starting_vertex)
        if len(edges) == 0:
            return
        else:
            for edge in edges:

                if edge not in visited:
                    self.dft_recursive(edge, visited)
                else:
                    return

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            current_path = q.dequeue()
            current_vertex = current_path[-1]
            if current_vertex is destination_vertex:
                return current_path
            else:
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    edges = self.get_neighbors(current_vertex)
                    for edge in edges:
                        path_clone = list(current_path)
                        path_clone.append(edge)
                        q.enqueue(path_clone)



    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            current_path = s.pop()
            current_vertex = current_path[-1]
            if current_vertex is destination_vertex:
                return current_path
            else:
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    edges = self.get_neighbors(current_vertex)
                    for edge in edges:
                        path_clone = list(current_path)
                        path_clone.append(edge)
                        s.push(path_clone)


    def dfs_recursive(self, starting_vertex, destination_vertex,path=None,visited=None):
        print(starting_vertex,"start")
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        print(path,"path1")
        path = path + [starting_vertex]
        print(path,"path2")

        if starting_vertex == destination_vertex:
            return path

        for edge in self.get_neighbors(starting_vertex):
            if edge not in visited:
                new_path = self.dfs_recursive(edge,destination_vertex,path, visited)
                if new_path:
                    return new_path
            else:
                return None




if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
