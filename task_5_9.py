m =  int(input('Enter M: '))
n =  int(input('Enter n: '))

def splitter(a: int):
    splitters = []
    for i in range(2,int(a / 2 + 1)):
        if a % i == 0:
            splitters.append(i)
    print(splitters)

while m < n + 1:
    splitter(m)
    m += 1

