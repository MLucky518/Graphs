from util2 import Queue, Graph
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


values = []

for tup in test_ancestors:
    values.append(tup[1])


def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    graph = Graph()
    if starting_node not in values:
        return -1
    for tup in ancestors:
        parent = tup[0]
        child = tup[1]
        graph.add_vertex(child)
        graph.add_vertex(parent)  # add both vertices into the graph
        
        graph.add_edge(child, parent)  # creates the one way relationship
    print(graph.vertices)

    # starts a new path beginning with the starting node
    q.enqueue([starting_node])
    earliest_ancestor = -1
    longest_path = 1
    while q.size() > 0:
        current_path = q.dequeue()
        current_node = current_path[-1]

        if len(current_path) >= longest_path and current_node < earliest_ancestor:
            earliest_ancestor = current_node
            longest_path = len(current_path)

        if len(current_path) > longest_path:
            longest_path = len(current_path)
            earliest_ancestor = current_node

        # the vertice values are the parents and the children are keys
        parents = graph.get_neighbors(current_node)
        for parent in parents:
            path_clone = list(current_path)
            path_clone.append(parent)
            q.enqueue(path_clone)

    return earliest_ancestor


print(earliest_ancestor(test_ancestors, 5))
