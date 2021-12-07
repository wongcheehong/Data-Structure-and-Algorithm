class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        if node in self.adjacentList:
            print(f"Node {node} already exists")
            return
        self.adjacentList[node] = []
        self.numberOfNodes += 1

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnection(self):
        for key, array in self.adjacentList.items():
            print(f"{key}-> ", end="")
            for node in array:
                print(f"{node} ", end="")
            print()


myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')

myGraph.showConnection()
# 0-> 1 2
# 1-> 3 2 0
# 2-> 4 1 0
# 3-> 1 4
# 4-> 3 2 5
# 5-> 4 6
# 6-> 5
