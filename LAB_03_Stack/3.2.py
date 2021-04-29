'''
Chapter : 3 - item : 2 - Number in Stack
จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้
A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack
P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )
D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  
LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม
*** Hint ***
ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ
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
        return self.stack.pop() 
    def peek(self):
        return self.stack[-1] 
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return len(self.stack)
    def clear(self):
        return self.stack.clear() 
    def delete(self, item):
        self.stack.remove(item) 

if __name__ == "__main__":
    # ManageStack()
    inp = list(input("Enter Input : ").split(","))
    s = Stack()
    
    # s.stack.sort()
    for i in inp:
        if i.startswith("A"):
            i = i.split()
            s.push(int(i[1]))
            print(f"Add = {i[1]}")

        elif i.startswith("P"):
            i = i.split()
            if s.is_empty():
                print("-1")
            else: 
                print(f"Pop = {s.pop()}")

        elif i.startswith("D"):
            i = i.split()
            if not s.is_empty():
                for j in range(s.size()):
                    if int(i[1]) in s.stack:
                        print(f"Delete = {i[1]}")
                        s.delete(int(i[1]))
            else: 
                    print("-1")
                
        elif i.startswith("LD"):
            i = i.split()
            if not s.is_empty():
                ss = Stack()
                for num in s.stack:        
                    if int(num) < int(i[1]) :       
                        ss.push(num)
                for temp in reversed(ss.stack):
                    print(f"Delete = {temp} Because {temp} is less than {i[1]}")
                    s.delete(temp)                         
            else:
                print("-1")

        elif i.startswith("MD"):
            i = i.split()
            if not s.is_empty():
                ss = Stack()
                for num in s.stack:        
                    if int(num) > int(i[1]) :       
                        ss.push(num)
                for temp in reversed(ss.stack):
                    print(f"Delete = {temp} Because {temp} is more than {i[1]}")  
                    s.delete(temp)                         
            else:
                print("-1")   

    print("Value in Stack =",("[{0}]".format(', '.join(map(str, s.stack)))))
#                   อย่าแก้แล้ว                    #
#                   อย่าแก้แล้ว                    #
#                   อย่าแก้แล้ว                    #
