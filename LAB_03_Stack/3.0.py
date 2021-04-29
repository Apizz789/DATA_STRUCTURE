'''
Introduction Stack()
Stack concept is used " LIFO " >> Last In Frist Out
    The main function of Stack is
        * def __init__(self):       >> create Stack
        * def __str__(self):        >> change list to string and return string
        * def push(self, items):    >> append items to stack
        * def pop(self):            >> remove items on the top of Stack from stack
        * def peek(self):           >> return item on the top of Stack from stack
        * def is_empty(self):       >> check if Stack is empty
        * def size(self):           >> return size of stack
        * def clear(self):          >> remove all items from stack
Let's see how it works !!
'''
class Stack():
    def __init__(self):
        self.stack = []
    def __str__(self):
        if self.is_empty():
            return "Empty"
        s = ""
        for i in self.stack:
            s += str(i) + " "
        return s
    def push(self, item):
        return self.stack.append(item)
    def pop(self):
        return self.stack.pop() if not self.is_empty() else "Empty"
    def peek(self):
        return self.stack[-1] if not self.is_empty() else "Empty"
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return len(self.stack)
    def clear(self):
        return self.stack.clear()