'''
Introduction Linked list()
Node ->  | data, next index |
data called head
next index called tail


'''
# Singly liked list
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)
class LinkedList:
    def __init__(self):
        self.head = None
        self.ssize = 0
    def __str__(self):
        if self.isEmpty():
            return "empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data)+ " "
            cur = cur.next     
        return s
    def isEmpty(self):
        return self.head == None

    def append(self, item):
        self.ssize += 1
        if self.isEmpty():
            self.head = Node(item)
            return
        node = self.head
        while (node.next != None):
            node = node.next
        node.next = Node(item)

    def addHead(self, item):
        self.ssize += 1
        if self.isEmpty():
            self.head = Node(item)
            return
        node = self.head
        self.head = Node(item)
        self.head.next = node

    def size(self):
        return self.ssize

    def search(self, item):
        node = self.head
        if self.isEmpty():
            return "Not Found"
        while node.next != None:
            if node.data == item:
                return "Found"
            node = node.next
        if node.data == item:
            return "Found"
        return "Not Found"
    def index(self, item):
        index = 0
        node = self.head
        if self.isEmpty():
            return -1
        if self.size() == 1:
            if node.data == item:
                return index
        while node.next != None:
            if node.data == item:
                return index
            node = node.next
            index += 1

        if node.data == item:
            return index
        return -1


if __name__ == '__main__':
    L = LinkedList()
    inp = input("Enter XXXX : ").split(",")
    for i in inp:
        if i[:2] == "AP":
            L.append(i[3:])
        elif i[:2] == "AH":
            L.addHead(i[3:])
        elif i[:2] == "SE":
            print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
        elif i[:2] == "ID":
            print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
        elif i[:2] == "SI":
            print("Linked List size = {0} : {1}".format(L.size(), L))
    print("Linked List :", L)