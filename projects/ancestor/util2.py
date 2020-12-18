class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)



class Graph():
    
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
