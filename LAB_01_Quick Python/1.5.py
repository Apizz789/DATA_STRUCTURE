'''
Chapter : 1 - item : 5 - vickrey auction
จงสร้าง vickrey auction แบบจำลอง
Vickrey auction คือการประมวลที่ผู้ที่จะชนะการประมูล คือ ผู้ที่ยื่นซองเสนอราคาสูงที่สุด แต่จะจ่ายจริงในราคาที่สูงเป็นอันดับสองรองลงมา

word
"Enter All Bid : "
"not enough bidder"
"error : have more than one highest bid"
"winner bid is $ need to pay $"

'''
if __name__ == "__main__":
    num_bid = [int(n) for n in input("Enter All Bid : ").split()]
    Second_price = 0 
    MAX = 0
    for i in num_bid:
        if i >= MAX:   
            Second_price = MAX
            MAX = i
        elif i < MAX and i > Second_price:
            Second_price = i
    if len(num_bid) == 1:
        print("not enough bidder")
    elif MAX == Second_price:
        print("error : have more than one highest bid")
    else :
        print(f"winner bid is {MAX} need to pay {Second_price}") 