'''
Chapter : 2 - item : 3 - Mod Position
ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการแสดงตำแหน่งของ List ในตำแหน่งที่หารเลขใดๆลงตัว จาก String
def mod_position(arr, s):
    //Code Here
Input ตำแหน่งที่แรกเป็นค่าใน String ที่นำเข้ามา
Input ตำแหน่งที่สองเป็นตัวเลขที่ทำการบอกว่าจะแสดงที่ตำแหน่งที่หารตัวเลขนั้นๆลงตัว 
เช่นถ้าใส่เลข 3 และ String มีค่าเป็น ABCDEFG ก็จะแสดงตำแหน่งที่ 3 คือ C กับตำแหน่งที่ 6 คือ F 
'''

def mod_position():
    print("*** Mod Position ***")
    inp = list(input("Enter Input : ").split(","))
    temp, num = inp[0], int(inp[1])
    result = []
    for index in range(len(temp)):
        if (index+1) % num == 0:
            result.append(temp[index])
    return print(result)      
mod_position()