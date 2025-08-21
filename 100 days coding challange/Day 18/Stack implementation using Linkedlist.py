class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        print(f"Pushed: {val}")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return -1
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return -1
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements:", self.stack)

s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print(s.peek())
print(s.is_empty())
print(s.size())