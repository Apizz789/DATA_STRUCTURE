"""
hapter : 2 - item : 4 - หอคอยแห่งฮานอย
 ส่งมาแล้ว 4 ครั้ง
เขียนโปรแกรมแก้ปัญหา หอคอยแห่งฮานอย โดยเราจะมีแทงไม้อยู่3แท่งคือ A B C และรับ input เป็นจำนวนแผ่นไม้ที่วางซ้อนกันให้แสดงลำดับการย้ายแผ่นไม้ทั้งหมดจากแท่ง A ไปยัง แท่งC โดยแผ่นไม้ที่มีขนาดเล็กกว่าจะอยู่ข้างบนแผ่นไม้ที่มีขนาดใหม่กว่าเสมอ(ห้ามวางแผ่นเล็กกว่าไว้ข้างล่าง)

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ทุกฟังก์ชันต้องมี parameter มากที่สุดไม่เกิน 5 ตัว

คำแนะนำ ให้สร้างฟังก์ชันสำหรับแสดงผล แยกต่างหาก และใช้ list ในการเก็บข้อมูลของแท่งไม้แต่ละแท่ง
และให้ระวังเรื่องการสลับ list ให้ดีๆ

หากมีข้อสงสัยเกี่ยวกับ หอคอยแห่งฮานอย สามารถสอบถาม TA เพิ่มเติม หรือ ลองเล่นได้ที่ https://www.mathsisfun.com/games/towerofhanoi.html

==============     Testcase     ==============

def move(n,A,B,C,maxn):
    #code here
n = int(input("Enter Input : "))

Enter Input : 3
|  |  |
1  |  |
2  |  |
3  |  |
move 1 from  A to C
|  |  |
|  |  |
2  |  |
3  |  1
move 2 from  A to B
|  |  |
|  |  |
|  |  |
3  2  1
move 1 from  C to B
|  |  |
|  |  |
|  1  |
3  2  |
move 3 from  A to C
|  |  |
|  |  |
|  1  |
|  2  3
move 1 from  B to A
|  |  |
|  |  |
|  |  |
1  2  3
move 2 from  B to C
|  |  |
|  |  |
|  |  2
1  |  3
move 1 from  A to C
|  |  |
|  |  1
|  |  2
|  |  3


Enter Input : 4
|  |  |
1  |  |
2  |  |
3  |  |
4  |  |
move 1 from  A to B
|  |  |
|  |  |
2  |  |
3  |  |
4  1  |
move 2 from  A to C
|  |  |
|  |  |
|  |  |
3  |  |
4  1  2
move 1 from  B to C
|  |  |
|  |  |
|  |  |
3  |  1
4  |  2
move 3 from  A to B
|  |  |
|  |  |
|  |  |
|  |  1
4  3  2
move 1 from  C to A
|  |  |
|  |  |
|  |  |
1  |  |
4  3  2
move 2 from  C to B
|  |  |
|  |  |
|  |  |
1  2  |
4  3  |
move 1 from  A to B
|  |  |
|  |  |
|  1  |
|  2  |
4  3  |
move 4 from  A to C
|  |  |
|  |  |
|  1  |
|  2  |
|  3  4
move 1 from  B to C
|  |  |
|  |  |
|  |  |
|  2  1
|  3  4
move 2 from  B to A
|  |  |
|  |  |
|  |  |
|  |  1
2  3  4
move 1 from  C to A
|  |  |
|  |  |
|  |  |
1  |  |
2  3  4
move 3 from  B to C
|  |  |
|  |  |
|  |  |
1  |  3
2  |  4
move 1 from  A to B
|  |  |
|  |  |
|  |  |
|  |  3
2  1  4
move 2 from  A to C
|  |  |
|  |  |
|  |  2
|  |  3
|  1  4
move 1 from  B to C
|  |  |
|  |  1
|  |  2
|  |  3
|  |  4

"""
a = []
b = []
c = []


def pop_and_append(start, dest):
    global a
    global b
    global c
    if start == 'A':
        x = a.pop(0)
    elif start == 'B':
        x = b.pop(0)
    else:
        x = c.pop(0)
    if dest == 'A':
        a.insert(0, x)
    elif dest == 'B':
        b.insert(0, x)
    else:
        c.insert(0, x)
    # print(a, b, c)


def show_tower(maxn, row):
    global a
    global b
    global c
    acp = a[::-1]
    bcp = b[::-1]
    ccp = c[::-1]
    if row == 0:
        return
    if row == maxn:
        print('|  |  |')
    if len(a) >= row:
        print(f"{acp[row-1]}  ", end="")
    else:
        print('|  ', end="")
    if len(b) >= row:
        print(f"{bcp[row-1]}  ", end="")
    else:
        print('|  ', end="")
    if len(c) >= row:
        print(f"{ccp[row-1]}", end="")
    else:
        print('|', end="")
    if row != 0:
        print()
    show_tower(maxn, row-1)




def move(n, start, filler, dest, maxn):
    if n == 1:
        print(f"move {n} from  {start} to {dest}")
        pop_and_append(start, dest)
        show_tower(maxn, maxn)
    else:
        move(n-1, start, dest, filler, maxn)
        print(f"move {n} from  {start} to {dest}")
        pop_and_append(start, dest)
        show_tower(maxn, maxn)
        move(n-1, filler, start, dest, maxn)


def rec_init_a(num, target):
    global a
    if num <= target:
        a.append(num)
        rec_init_a(num+1, target)


if __name__ == '__main__':
    n = int(input("Enter Input : "))
    rec_init_a(1, n)
    show_tower(n, n)
    move(n, 'A', 'B', 'C', n)