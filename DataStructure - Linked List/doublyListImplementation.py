class Node:
    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        llist = []
        currentNode = self.head
        while currentNode is not None:
            llist.append(currentNode.value)
            currentNode = currentNode.next
        return "From Head to tail (Left to Rights): " + str(llist)

    def backwardTraversal(self):
        array = []
        currentNode = self.tail
        while currentNode is not None:
            array.append(currentNode.value)
            currentNode = currentNode.previous
        return array

    def append(self, value):
        newNode = Node(value, self.tail, None)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = Node(value, None, self.head)
        self.head.previous = newNode
        self.head = newNode
        self.length += 1

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)

        if index == 0:
            return self.prepend(value)

        i = 0
        currentNode = self.head
        while i != index:
            currentNode = currentNode.next
            i += 1
        previousNode = currentNode.previous
        previousNode.next = Node(value, previousNode, currentNode)
        self.length += 1

    def remove(self, index):
        if index > self.length:
            return print("Out of bounds")
        if index == 0:
            self.head = self.head.next
            self.head.previous = None
            return

        i = 0
        unwantedNode = self.head
        while i != index:
            unwantedNode = unwantedNode.next
            i += 1

        previousNode = unwantedNode.previous
        previousNode.next = unwantedNode.next
        if index == self.length-1:
            self.tail = previousNode
        self.length -= 1

    def currentHeadAndTail(self):
        print(f"{self.head.value}, {self.tail.value}")


myLinkedList = DoublyLinkedList(10)
myLinkedList.append(5)
myLinkedList.append(15)
myLinkedList.prepend(1)
myLinkedList.insert(4, 100)  # [1, 10, 100, 5, 15]
myLinkedList.remove(4)  # [1, 10, 100, 5, 15]
myLinkedList.currentHeadAndTail()
print(myLinkedList)
print(myLinkedList.backwardTraversal())
print(myLinkedList.length)
