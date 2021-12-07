def has_path_BFS(graph, src, dst):
    queue = [src]

    while queue:
        current = queue.pop(0)
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)

    return False


def has_path_DFS(graph, src, dst):
    if src == dst:
        return True

    for neighbor in graph[src]:
        if(has_path_DFS(graph, neighbor, dst)):
            return True

    return False


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

print(has_path_DFS(graph, 'e', 'a'))
print(has_path_BFS(graph, 'a', 'e'))
