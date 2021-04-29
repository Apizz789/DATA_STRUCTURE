inp = list(map(int, input("Enter number : ").split()))
if inp.count(-1) <= 0:
    print("Error")
else:
    # print("DDDDDDDDDD JAAA")
    maxx = 0
    second = 0
    result = 0
    for i in inp:
        if inp.count(i) > maxx and i > 0:
            maxx = inp.count(i)
            result = i
        elif inp.count(i) == maxx :
            second = inp.count(i)
    if result == 0 or maxx == second:
        print("Erorr")
    else:
         print(result)