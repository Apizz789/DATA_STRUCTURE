class Node:
    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.ssize = 0

    def __str__(self):
        if self.isempty():
            return ''
        cur, s = self.head, str(self.head.data)
        while cur.next != None:
            s += "->" + str(self.next.data)
            cur = cur.next
        return s

    def str_reverse(self):
        if self.isempty():
            return ''
        cur, s = self.tail, str(self.tail.data)
        while cur.previous != None:
            s += "->" + str(self.previous.value)
            cur = cur.previous
        return s
    
    def isempty(self):
        return self.head == None
    
    def append(self,data):
        if self.isempty():
            self.head = self.tail = Node(data)
            self.ssize += 1
            return
        self.ssize += 1
        cur = self.head
        while cur.next != None:
            cur = cur.next
        node = Node(data)
        node.previous, cur.next, self.tail = cur, node, node
        
    def addBef(self, data):
        if self.isempty():
            self.head = self.tail = Node(data)
            self.ssize += 1
            return
        node = Node(data)
        if self.size() == 1:
            node.next, self.tail.previous, self.head = self.tail, node, node
        else :
            node.next, self.head.previous, self.head = self.head, node, node
        self.ssize += 1
    def insert(self, pos, item):
        if pos > self.size() or pos < 0 :
            return print("Data cannot be added")
        
        if self.isempty():
            self.head = self.tail = Node(item)
            self.ssize += 1
            return print(f"index = {pos} and data = {item}")

        node = Node(item)
        if pos == 0:
            self.ssize += 1
            node.next, self.head.previous, self.head = self.head, node, node
            return print(f"index = {pos} and data = {item}")
        if pos == self.size():
            self.ssize += 1
            node.previous, self.tail.next, self.tail = self.tail, node, node
            return print(f'index = {pos} and data = {item}')

        cur, index = self.head, 0
        while index != pos-1:
            index += 1
            cur = cur.next
        
        cur.next.previous = node
        node.next = cur.next
        node.previous = cur
        cur.next = node
        self.ssize += 1
        return print(f'index = {pos} and data = {item}')

        def size(self):
            return self.ssize

        def remove(self, item):
            if self.isEmpty():
                return print("Not Found!")

            cur = self.head
            if self.size() == 1 and cur.value == item:
                self.head = self.tail = None
                self.ssize -= 1
                return print(f'removed : {item} from index : 0')

            self.ssize -= 1
            if item == self.head.value:
                self.head = self.head.next
                self.head.previous = None
                return print(f'removed : {item} from index : 0')

            index = 0
            while cur.next != None:
                if cur.value == item:
                    cur.previous.next, cur.next.previous = cur.next, cur.previous
                    return print(f'removed : {item} from index : {index}')
                index += 1
                cur = cur.next
            if cur.value == item:
                self.tail = self.tail.previous
                self.tail.next = None
                return print(f'removed : {item} from index : {index}')
            self.ssize += 1
            return print("Not Found!")
if __name__ == '__main__':
    inp = input('Enter Input : ').split(',')

    L = LinkedList()
    for data in inp:
        data = data.split()
        if data[0] == 'A':
            L.append(data[1])
        elif data[0] == 'Ab':
            L.add_before(data[1])
        elif data[0] == 'I':
            L.insert(int(data[1].split(':')[0]), data[1].split(':')[1])
        else:
            L.remove(data[1])
        print('linked list :', L)
        print('reverse :', L.str_reverse())