def rec_row(number, sharp):
    print('_'*(number-sharp), end='')
    print('#'*(sharp), end='')
    print()


def rec_pattern(number, row=0):
    if number > 0:
        if row < number:
            row += 1
            rec_row(number, row)
            rec_pattern(number, row)
    elif number < 0:
        if row < abs(number):
            rec_row(abs(number), abs(number)-row)
            row += 1
            rec_pattern(number, row)
    else:
        print('Not Draw!')


if __name__ == '__main__':
    number = int(input("Enter Input : "))
    rec_pattern(number)