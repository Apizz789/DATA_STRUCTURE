'''
Chapter : 3 - item : 3 - Postfix Calculator
จงเขียนโปรแกรมโดยใช้ Stack เพื่อคำนวณหา ค่าของนิพจน์แบบ postfix 
โดยให้แสดงผลลัพธ์ตามตัวอย่าง

class Stack():
    def __init__(self, ls = None):
    def push(self,i):
    def pop(self):
    def isEmpty(self):
    def size(self):

def postFixeval(st):
    s = Stack()
    ### Enter Your Code Here ###
    return s.pop()          
print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))
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
    def pop(self):
        return self.stack.pop() if not self.is_empty() else "Empty"
    def push(self, items):
        return self.stack.append(items)
    def peek(self):
        return self.stack[-1] if not self.is_empty() else "Empty"
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return len(self.stack)
    def clear(self):
        return self.stack.clear()


def postfixeval(inp):
    s = Stack()
    for i in inp:
        if i not in "+-*/" :
            s.push(i)
            # print(i, end = " ")
            continue
        op1, op2 = s.pop(), s.pop()
        op1, op2 = float(op1), float(op2)
    
        if i == '+':
            s.push(op2 + op1)
        elif i == '-':
            s.push(op2 - op1)
        elif i == '*':
            s.push(op2 * op1)
        elif i == '/':
            s.push(op2 / op1)

    return s.pop()

if __name__ == '__main__':
    print(" ***Postfix expression calcuation***")
    token = list(input("Enter Postfix expression : ").split())
    print("Answer : ",'{:.2f}'.format(postfixeval(token)))