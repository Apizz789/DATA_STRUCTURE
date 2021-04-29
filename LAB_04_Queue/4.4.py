class Queue:

    def __init__(self):
        self.item = []

    def enqueue(self, data):
        self.item.append(data)

    def dequeue(self):
        self.item.pop(0)

    def print_program1(self):

        print('My   Activity:Location = ', end='')
        i = 0

        while i < len(self.item)-1:
            print(self.item[i], end=', ')
            i += 1
        print(self.item[len(self.item)-1])

    def print_program2(self):

        print('Your Activity:Location = ', end='')
        i = 0

        while i < len(self.item)-1:
            print(self.item[i], end=', ')
            i += 1
        print(self.item[len(self.item)-1])


def my_program(lst):
    act = {0: 'Eat', 1: 'Game', 2: 'Learn', 3: 'Movie'}
    loc = {0: 'Res.', 1: 'ClassR.', 2: 'SuperM.', 3: 'Home'}

    program1 = Queue()

    for ew in lst:
        s = ''
        for i in range(len(act)):
            if int(ew.split(':')[0]) == i:
                s += str(act[i])
        s += ':'
        for j in range(len(loc)):
            if int(ew.split(':')[1]) == j:
                s += str(loc[j])
        program1.enqueue(s)

    program1.print_program1()


def ur_program(lst):
    act = {0: 'Eat', 1: 'Game', 2: 'Learn', 3: 'Movie'}
    loc = {0: 'Res.', 1: 'ClassR.', 2: 'SuperM.', 3: 'Home'}

    program2 = Queue()

    for ew in lst:
        s = ''
        for i in range(len(act)):
            if int(ew.split(':')[0]) == i:
                s += str(act[i])
        s += ':'
        for j in range(len(loc)):
            if int(ew.split(':')[1]) == j:
                s += str(loc[j])
        program2.enqueue(s)

    program2.print_program2()


def compare_score(pro1, pro2):

    score = 0
    i = 0
    while i < len(pro1):
        if pro1[i].split(':')[0] == pro2[i].split(':')[0] and pro1[i].split(':')[1] == pro2[i].split(':')[1]:
            score += 4
        elif pro1[i].split(':')[0] != pro2[i].split(':')[0] and pro1[i].split(':')[1] == pro2[i].split(':')[1]:
            score += 2
        elif pro1[i].split(':')[0] == pro2[i].split(':')[0] and pro1[i].split(':')[1] != pro2[i].split(':')[1]:
            score += 1
        elif pro1[i].split(':')[0] != pro2[i].split(':')[0] and pro1[i].split(':')[1] != pro2[i].split(':')[1]:
            score -= 5
        i += 1

    if score >= 7:
        print('Yes! You\'re my love! : Score is %d.' % score)
    elif 0 < score < 7:
        print('Umm.. It\'s complicated relationship! : Score is %d.' % score)
    elif score <= 0:
        print('No! We\'re just friends. : Score is %d.' % score)


if __name__ == '__main__':

    inp = input('Enter Input : ').split(',')

    me = []
    u = []

    for e in inp:
        me.append(e.split(' ')[0])
        u.append(e.split(' ')[1])

    i = 0

    print('My   Queue = ', end='')
    while i < len(me) - 1:
        print(me[i], end=', ')
        i += 1
    print(me[len(me) - 1])

    i = 0

    print('Your Queue = ', end='')
    while i < len(u) - 1:
        print(u[i], end=', ')
        i += 1
    print(u[len(u) - 1])

    my_program(me)
    ur_program(u)
    compare_score(me, u)
