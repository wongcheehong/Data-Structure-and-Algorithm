class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value):
        self.head = Node(value, None)
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        llist = []
        currentNode = self.head
        while currentNode is not None:
            llist.append(currentNode.value)
            currentNode = currentNode.next
        return "From Head to tail (Left to Rights): " + str(llist)

    def append(self, value):
        newNode = Node(value, None)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = Node(value, self.head)
        self.head = newNode
        self.length += 1

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)

        if index == 0:
            return self.prepend(value)

        i = 0
        currentNode = self.head
        # after while loop, currentNode will be the node before the insert node
        while i != index-1:
            currentNode = currentNode.next
            i += 1

        nextNode = currentNode.next
        currentNode.next = Node(value, nextNode)
        self.length += 1

    def remove(self, index):
        if index > self.length:
            return print("Out of bounds")
        if index == 0:
            self.head = self.head.next
            return
        i = 0
        currentNode = self.head
        # after while loop, currentNode will be the node before the remove node
        while i != index-1:
            currentNode = currentNode.next
            i += 1

        removedNode = currentNode.next
        currentNode.next = removedNode.next
        if index == self.length-1:
            self.tail = currentNode
        self.length -= 1

    def currentHeadAndTail(self):
        print(f"{self.head.value}, {self.tail.value}")

    def reverse(self):
        previousNode = None
        currentNode = self.head
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

        # Switch between the head and tail pointer
        tempNode = self.head 
        self.head = self.tail
        self.tail = tempNode


myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(15)
myLinkedList.prepend(1)
myLinkedList.insert(4, 100)  # [1, 10, 100, 5, 15]
myLinkedList.remove(4)  # [1, 10, 100, 5, 15]
print(myLinkedList)
print(myLinkedList.length)
myLinkedList.reverse()
print(f"reversed: {myLinkedList}")
