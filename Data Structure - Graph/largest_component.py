"""
https://structy.net/problems/largest-component
Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.
"""


def largest_component(graph):
    visited = set()
    highest = 0
    for node in graph:
        no_of_connected_nodes = explore(graph, node, visited)
        if highest < no_of_connected_nodes:
            highest = no_of_connected_nodes

    return highest


def explore(graph, current, visited):
    if (current in visited):
        return 0

    visited.add(current)

    count = 1
    for neighbor in graph[current]:
        count += explore(graph, neighbor, visited)

    return count


print(largest_component({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}))  # -> 4
