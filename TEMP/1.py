class Stack:
    def __init__ (self):
        self.stack = []
    def __str__ (self):
        if self.isEmpty() :
            return "Empty"
        s = ""
        for i in self.stack:
            s += str(i) + " "
        return s
    def push(self, item):
        return self.stack.append(item)
    def pop(self):
        return self.stack.pop() if not self.isEmpty() else "Empty"
    def peek(self):
        return self.stack[-1] if not self.isEmpty() else "Empty"
    def isEmpty(self):
        return self.size == 0
    def size (self):
        return len(self.stack)
    def clear (self):
        return self.stack.clear()
class Queue:
    def __init__(self):
        self.queues = []
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        s = ""
        for i in self.queues:
            s += str(i) + " " 
        return s
    def Enqueue(self, item):
        return self.queues.append(item)
    def Dequeue(self):
        return self.queues.pop[0] if not self.isEmpty() else "Empty"
    def isEmpty (self):
        return self.size() == 0
    def size (self):
        return len(self.queues)
    