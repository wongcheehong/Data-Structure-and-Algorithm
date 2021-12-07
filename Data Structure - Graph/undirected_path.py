"""
https://structy.net/problems/undirected-path
Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.
"""


def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, set())


def hasPath(graph, src, dst, visited):
    if(src in visited):
        return False
    if src == dst:
        return True

    visited.add(src)

    for neighbor in graph[src]:
        if(hasPath(graph, neighbor, dst, visited)):
            return True

    return False


def buildGraph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print(undirectedPath(edges, 'k', 'j'))
