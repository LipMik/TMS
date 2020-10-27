def fact(x):
    rezult = 1

    if x % 2 == 0:
        start = 2
    else:
        start = 1

    for i in range(start, x + 2, 2):
        rezult *= i

    return rezult


n = int(input('Enter n: '))

rez = fact(n)

print(rez)
