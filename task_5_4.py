n = int(input('Enter N: '))

def summ (a:int):
    s = 1
    for i in range(2,a,1):
        s += 1 / i
    return (s)

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    print (summ(n))
