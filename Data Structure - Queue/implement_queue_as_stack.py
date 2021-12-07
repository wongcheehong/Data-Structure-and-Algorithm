class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x: int) -> None:
        self.dump_to_stack1()
        self.stack1.append(x)
        self.size += 1

    def pop(self) -> int:
        self.dump_to_stack2()
        self.size -= 1
        return self.stack2.pop()

    def peek(self) -> int:
        self.dump_to_stack2()
        return self.stack2[-1]

    def dump_to_stack1(self):
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dump_to_stack2(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)

print(obj.peek())
print(obj.pop())
print(obj.pop())
print(obj.empty())
print(obj.pop())
print(obj.empty())
