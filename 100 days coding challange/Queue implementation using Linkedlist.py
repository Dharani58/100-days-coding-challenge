class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)
        print(f"Enqueued: {val}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return -1
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return -1
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements:", self.queue)

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(q.peek())
print(q.is_empty())
print(q.size())
q.enqueue(40)
q.display()
q.dequeue()
q.display()