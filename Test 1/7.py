# def print_square(n) : 
      
#     for i in range(1, n+1) : 
#         for j in range(1, n+1) : 
#             if (i == 1 or i == n or 
#                 j == 1 or j == n) :             
#                 print(i, end = "")             
#             else : 
#                 print(" ", end = "")             
          
#         print() 
          
          
   
# # Driver code for above function 
# rows = 8
# print_square(rows)
if __name__ == '__main__':
    num = int(input("Enter a positive number : "))
    numbers = '123456789ABCDEF'
    lst = []
    lst_rev = []
    if 0 < num < 16:
        for i in range(1, num+1):
            if i < 10:
                lst.append(str(i))
            else:
                lst.append(numbers[i-1])
        for i in reversed(lst):
            lst_rev.append(i)

        print(*lst, sep=" ")
        for i in range(num-2):
            s = str(lst[i+1])
            for _ in range(num*2-3):
                s += ' '
            s += str(lst[i])
            print(s)
        if num != 1:
            print(*lst_rev, sep=" ")
    elif num <= 0:
        print(num, 'is too low.')
    elif num >= 16:
        print(num, 'is too high.')