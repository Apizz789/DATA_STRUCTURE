'''
Chapter : 2 - item : 2 - weirdSubtract
จงสร้างฟังชั่นการลบที่จะคิดทีละครั้งละ 1 โดยมีเงื่อนไขคือ
หากตัวตั้งลงท้ายด้วย 0 ตัด 0 ทิ้ง
หากไม่ใช่ลบปกติ

def weirdSubtract(n,k):
	### Enter Your Code Here ###

n,s = input("Enter num and sub : ").split()
print(weirdSubtract(int(n),int(s)))
'''
def weirdSubtract(n, k):
    for i in range(k):
        if n % 10 == 0:
            n = n // 10
        else:
            n -= 1 
    return n           
n, k = input("Enter num and sub : ").split()
print(weirdSubtract(int(n),int(k)))
