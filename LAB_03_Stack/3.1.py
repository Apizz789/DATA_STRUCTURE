'''
Chapter : 3 - item : 1 - สร้าง stack
ให้นักศึกษา สร้าง class Stack ด้วย list ของ python โดย มี method ดังต่อไปนี้
def __init__()    // ใช้สำหรับสร้าง list ว่าง
def push(i)        // เก็บข้อมูลลง stack
def pop()          // นำข้อมูลออกจาก stack
def isEmpty()   // ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
def size()         // ตรวจสอบจำนวนข้อมูลใจ stack
แล้วให้โปรแกรมรับข้อมูล เพื่อเก็บใน stack และให้ทำงานตาม code คำสั่งต่อไปนี้
print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter data to stack : ").split()]
s = Stack()
for e in ls:
    s.push(e)
print(s.size(),"Data in stack : ",s.items)
while not s.isEmpty():
    s.pop()
print(s.size(),"Data in stack : ",s.items)
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

if __name__ == "__main__":
    print(" *** Stack implement by Python list***")
    ls = [e for e in input("Enter data to stack : ").split()]
    s = Stack()
    for e in ls:
        s.push(e)
    print(s.size(), "Data in stack : ", s.stack)
    while not s.is_empty():
        s.pop()
    print(s.size(), "Data in stack : ", s.stack)