'''
Introduction Queue()
Queue concept is used " FIFO " >> Frist In Frist Out
    The main function of Queue is
        * def __init__(self):       >> create Queue
        * def __str__(self):        >> change list to string and return string
        * def EnQueue(self, items): >> append items to queue
        * def DeQueue(self):        >> remove items on the index[0] of Queue from queue
        * def is_empty(self):       >> check if Queue is empty
        * def size(self):           >> return size of queue
        * def clear(self):          >> remove all items from queue
Let's see how it works !!
'''
class Queue():
    def __init__(self):
        self.queue = []
    def __str__(self):
        if self.is_empty():
            return "Empty"
        s = ""
        for i in self.queue:
            s += str(i) + " "
        return s
    def EnQueue(self, item):
        return self.queue.append(item)
    def DeQueue(self):
        return self.queue.pop(0) if not self.is_empty() else "Empty"
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return len(self.queue)
    def clear(self):
        return self.queue.clear()
