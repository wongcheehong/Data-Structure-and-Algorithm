class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[-1]

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if not self.array:
            return None
        return self.array.pop()


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
