class Queue:

    def __init__(self):
        self.item = []

    def enqueue(self, data):
        self.item.append(data)

    def dequeue(self):
        return self.item.pop(0)

def encodemsg(q1, q2):

    q = Queue()

    i = 0
    j = 0

    while i < len(q1):
        if (ord(q1[i]) >= 97 and ord(q1[i]) <= 122 and ord(q1[i]) + q2[j] > 122) or (ord(q1[i]) >= 65 and ord(q1[i]) <= 90 and ord(q1[i]) + q2[j] > 90):
            k = ord(q1[i]) + q2[j] - 26
            q.enqueue(chr(k))


        elif (ord(q1[i]) >= 97 and ord(q1[i]) <= 122 and ord(q1[i]) + q2[j] <= 122) or ord(q1[i]) >= 65 and ord(q1[i]) <= 90 and ord(q1[i]) + q2[j] <= 90:
            k = ord(q1[i]) + q2[j]
            q.enqueue(chr(k))

        i += 1
        j += 1

        if j == len(q2):
            j = 0

    return q.item


if __name__ == '__main__':

    q1 = Queue()
    q2 = Queue()

    inp = input('Enter String and Code : ').split(',')

    for e in inp[0]:
        if e != ' ':
            q1.enqueue(e)

    for e in inp[1]:
        q2.enqueue(int(e))

    print('Encode message is : ', encodemsg(q1.item, q2.item))
    print('Decode message is : ', q1.item)