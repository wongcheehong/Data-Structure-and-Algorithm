class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.value

    def push(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.top = newNode
            self.bottom = newNode
        else:
            belowNode = self.top
            self.top = newNode
            self.top.next = belowNode
        self.length += 1

    def pop(self):
        if self.isEmpty():
            return None

        popElement = self.top
        self.top = self.top.next
        self.length -= 1
        return popElement.value

    def isEmpty(self):
        return self.length == 0


# Top -> Node -> Bottom
myStack = Stack()
myStack.push("Discord")
myStack.push("Udemy")
myStack.push("Google")

print(myStack.peek())

print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
