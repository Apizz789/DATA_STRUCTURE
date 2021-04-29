def tb(c):
    if c == n:
        print(''.join(map(str,a)))
    else:
        a[c] = 0
        tb(c+1)
        a[c] = 1
        tb(c+1)
n = int(input('Enter Number : '))
a = [0]*n
if n < 0:
    print('Only Positive & Zero Number ! ! !')
elif n == 0:
    print(0)
else:
    tb(0)