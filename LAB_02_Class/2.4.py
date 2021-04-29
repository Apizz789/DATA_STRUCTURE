'''
Chapter : 2 - item : 4 - 3 SUM(2)
จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array 
ที่มีผลรวมเท่ากับ 5 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง 
***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***
'''
def ThreeSum():
    inp = list(input("Enter Your List : ").split())
    inp = [int(x) for x in inp]
    inp.sort()
    result = []
    if len(inp) <= 2:
        print("Array Input Length Must More Than 2")
        pass
    else :
        for one in range(len(inp)):
         for two in range(one+1, len(inp)):
             for three in range(two+1, len(inp)):
                    if inp[one]+inp[two]+inp[three] == 5 and [inp[one], inp[two], inp[three]] not in result :
                            result.append([inp[one], inp[two], inp[three]])
        return print(result)
ThreeSum() 