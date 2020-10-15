sign = None
x = int(input('Enter X : '))
y = int(input('Enter Y : '))

while sign != '0':

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