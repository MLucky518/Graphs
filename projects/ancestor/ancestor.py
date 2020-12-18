from util2 import Queue, Graph
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


children = []

for tup in test_ancestors:
    children.append(tup[1])


def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    graph = Graph()

    if starting_node not in children:
        return -1 

    for tup in ancestors:
        parent = tup[0]
        child = tup[1]
        graph.add_vertex(child)
        graph.add_vertex(parent)  # add both vertices into the graph

        graph.add_edge(child, parent)  # creates the relationship
    print(graph.vertices)

    # starts a new path beginning with the starting node
    q.enqueue([starting_node])
    earliest_ancestor = 0
    longest_path = 0
    while q.size() > 0:
        current_path = q.dequeue()
        current_node = current_path[-1]
        path_length = len(current_path)
    #  set earliest ancestor to the smaller value if theres a tie
        if path_length > longest_path or path_length >= longest_path and current_node < earliest_ancestor:
            earliest_ancestor = current_node
            longest_path = path_length

        # the vertice values are the parents and the children are keys
        parents = graph.get_neighbors(current_node)
        for parent in parents:
            path_clone = list(current_path)
            path_clone.append(parent)
            q.enqueue(path_clone)

    return earliest_ancestor


print(earliest_ancestor(test_ancestors, 5))
