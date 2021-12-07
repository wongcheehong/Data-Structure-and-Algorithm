def depthFirstPrint(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
            stack.append(neighbour)


def depthFirstPrintRecursive(graph, source):
    print(source)
    for neighbour in graph[source]:
        depthFirstPrintRecursive(graph, neighbour)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depthFirstPrint(graph, 'a')
# depthFirstPrintRecursive(graph, 'a')
