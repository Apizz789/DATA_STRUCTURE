'''
Chapter : 2 - item : 5 - funString
 ส่งมาแล้ว 0 ครั้ง
จงสร้าง Class funString ที่จะรับพารามิเตอร์เป็น String และเลขคำสั่งโดยมีฟังก์ชันดังต่อไปนี้

1. หาความยาวของ String

2. สลับพิมพ์เล็กพิมพ์ใหญ่ใน String (ห้ามใช้คำสั่ง upper และ lower)

3. Reverse String (ห้ามใช้คำสั่ง reversed)

4. ลบตัวอักษรที่ปรากฏมาก่อนใน String

class funString():

    def __init__(self,string = ""):

        ### Enter Your Code Here ###

    def __str__(self):

        ### Enter Your Code Here ###

    def size(self) :

        ### Enter Your Code Here ###

    def changeSize(self):

        ### Enter Your Code Here ###

    def reverse(self):

        ### Enter Your Code Here ###

    def deleteSame(self):

       ### Enter Your Code Here ###

str1,str2 = input("Enter String and Number of Function : ").split()
res = funString(str1)
if str2 == "1" :    print(res.size())
elif str2 == "2":  print(res.changeSize())
elif str2 == "3" : print(res.reverse())
elif str2 == "4" : print(res.deleteSame())
'''

class funString():
    def __init__(self, items):
        self.items = items
    def size(self):
        return len(self.items)
    def changeSize(self):
        temp = ""
        for i in range(len(self.items)):
            if self.items[i].islower(): temp += chr(ord(self.items[i]) - 32)
            else :                      temp += chr(ord(self.items[i]) + 32)
        return temp
    def reverse(self):
        temp = ""
        for i in range(len(self.items) -1, -1, -1):
            temp += self.items[i]
        return temp
    def deleteSame(self):
        temp = ""
        for i in range(len(self.items)):
            if self.items[i] not in temp:
                temp += self.items[i]
        return temp
        
inp_text, inp_choice = input("Enter String and Number of Function : ").split()
res = funString(inp_text)
if   inp_choice == "1" : print(res.size())
elif inp_choice == "2" : print(res.changeSize())
elif inp_choice == "3" : print(res.reverse())
elif inp_choice == "4" : print(res.deleteSame()) 