# последовательность из 2 чисел считал за подходящий участок

from random import randint

def rez(m: list):
    j = 0
    while len(m) >1 and m[j]< m [j+1]:
        m = m[j+1:]

    m = m[1:]
    return(m)


def ini():
    n = randint(10,20)
    mas = []
    for i in range(n):
        mas.append(randint(0,100))
    return(mas)

mas = ini()
print (mas)

count = 0
e = len(mas)
c = 0

while len(mas) > 1:
    mas = rez(mas)

    if (e - len(mas)) > 1:
        c += 1
        e = len(mas)
    else : e = len(mas)

print(c)



