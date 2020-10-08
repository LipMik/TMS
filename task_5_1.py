sign = None


while sign != '0':
    x = int(input('Enter X : '))
    y = int(input('Enter Y : '))
    sign = input('Enter SIGN : ')
    if sign == '0':
        print ('Process was stopped by the user! ')
    elif sign == '+':
        print(x + y)
    elif sign == '-':
        print(x - y)
    elif sign == '*':
        print(x * y)
    elif sign == '/' and y != 0:
        print(x / y)
    elif sign == '/' and y == 0:
        print ('invalid value Y!')

    else: print ('Enter correct SIGN!')