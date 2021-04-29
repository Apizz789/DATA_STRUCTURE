class node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    ptr = None
    root = None
    for i in l:
        newNode = node(data = int(i))
        if(ptr == None):
            root= newNode
            ptr = newNode
        else:
            ptr.next = newNode
            ptr = newNode
    return root


def printList(H):
    ptr = H
    while(ptr != None):
        print(ptr.data,end=" ")
        ptr = ptr.next
    print()

def mergeOrderesList(p,q):

    root = None
    tail = None
    ptr_L = p
    ptr_R = q

    while(ptr_L != None or ptr_R != None):

        if(ptr_L == None):
            tail.next  = ptr_R
            break

        if(ptr_R == None):
            tail.next  = ptr_L
            break

        if(ptr_L != None and ptr_L.data <= ptr_R.data):
            if(root == None):
                root = ptr_L
                tail = root
            else:
                tail.next = ptr_L
                tail = ptr_L
            ptr_L = ptr_L.next
        elif(ptr_R != None):
            if(root == None):
                root = ptr_R
                tail = root
            else:
                tail.next = ptr_R
                tail = ptr_R
            ptr_R = ptr_R.next

    return root


#################### FIX comand ####################
# input only a number save in L1,L2
L1,L2 = input("Enter 2 Lists : ").split()
L1 = L1.split(',')
L2 = L2.split(',')
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)