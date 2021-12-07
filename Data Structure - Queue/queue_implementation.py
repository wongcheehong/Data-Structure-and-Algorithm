class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.value

    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.first = self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        removedElement = self.first
        if self.first == self.last:
            self.last = None

        self.first = self.first.next
        self.length -= 1

        return removedElement.value

    def isEmpty(self):
        return self.length == 0


myQueue = Queue()
myQueue.enqueue("First")
myQueue.enqueue("Second")
myQueue.enqueue("Third")
myQueue.enqueue("Forth")

print(myQueue.peek())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
