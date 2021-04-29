'''
Chapter : 4 - item : 1 - มาใช้ Queue กันเถอะ
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา
E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue
D                 ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูล
                    ปัจจุบันของ Queue
***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty
'''

class Queue:
    def __init__(self):
        self.queue = []
    def __str__(self):
        return ", ".join(str(data) for data in self.queue) if self.size() != 0 else "Empty"
    def Enqueue(self, data):
        self.queue.append(data)
    def Dequeue(self):
        return self.queue.pop(0) if self.size() != 0 else "Empty"
    def size(self):
        return len(self.queue)

if __name__ == '__main__':
    inp = [data.split() for data in input("Enter Input : ").split(",")]
    q = Queue()
    dq = Queue()
    for data in inp:
        if len(data) == 1:                      # Dequeue
            dequeue = q.Dequeue()
            if dequeue != "Empty":
                dq.Enqueue(dequeue)
                print(dequeue, "<-", end = " ")
        else:
            q.Enqueue(int(data[1]))             # Enqueue
        print(q)
    print(dq, ":", q)
