"""
https://structy.net/problems/connected-components-count
Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.
"""


def connectedComponentCount(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited) == True:
            count += 1
    return count


def explore(graph, current, visited):
    if (current in visited):
        return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True


graph = {
    0: [4, 7],
    1: [],
    2: [],
    3: [6],
    4: [0],
    6: [3],
    7: [0],
    8: []
}

print(connectedComponentCount(graph))
