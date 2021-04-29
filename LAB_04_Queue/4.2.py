'''
Chapter : 4 - item : 2 - PSD48 a.k.a เขาเรียกผมว่าเอเรน
PSD48 (P-Saderd 48 Group) เป็นวงไอดอลวงหนึ่งที่กระแสกำลังมาแรง 
ณ ตอนนี้โดยเพลงที่ได้รับความนิยมอย่างมากคือเพลงจี่หอย โดยวง PSD48 กำลังจะจัดงานจับมือขึ้น 
โดยมีกฎอยู่ว่าถ้าหากคนที่กำลังต่อแถวอยู่เป็นคนจาก กองกำลังสำรวจ จะได้สิทธิพิเศษในการแทรกแถวไปข้างหน้าสุดทันที 
(แต่ถ้าหากคนหน้าสุดก็เป็นคนของกองกำลังสำรวจก็ต้องต่อหลังเขาอยู่ดี)  
PSD48 อยากให้คุณช่วยเขียนโปรแกรมสำหรับหาว่าจะมีโอตะ id ใดบ้างที่ได้จับมือ
เพลงประกอบ : https://youtu.be/Jd4Hd-HFgls

Input :
EN <value>  เป็นโอตะธรรมดา  id = value
ES <value>  เป็นโอตะของกองกำลังสำรวจ  id = value
D                 เป็นคำสั่งแสดงผล value ของหัวแถว ถ้าหากในแถวไม่มีคนจะแสดงคำว่า Empty
'''
class Queue:
    def __init__(self):
        self.queue = []
    def Enqueue(self, value):
        return self.queue.append(value)
    def Dequeue(self):
        return self.queue.pop(0) if not self.is_empty() else "Empty"
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return len(self.queue)

if __name__ == "__main__":
    inp = input("Enter Input : ").split(",")
    Q1, Q2 = Queue(), Queue()
    for item in inp:
        if item.split()[0].startswith("EN"):
            Q1.Enqueue(item.split()[1])
        elif item.split()[0].startswith("ES"):
            Q2.Enqueue(item.split()[1])
        elif item.split()[0].startswith("D"):
            if Q2.size() > 0:
                print(Q2.queue[0])
                Q2.Dequeue()
            elif Q1.size() > 0:
                print(Q1.queue[0])
                Q1.Dequeue()
            elif Q1.is_empty() or Q2.is_empty():
                print("Empty")


        