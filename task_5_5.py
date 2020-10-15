from random import randint

def dif(mas: list, m: int):
    for i,j in enumerate(mas):
        if j % 2 == 0:
            mas[i] = m
    return (mas)

n = 19
s = []

for i in range(n):
    s.append(randint(1,100))
print(s)

m = int(max(s))
print (m)
s = dif(s,m)

print(s)
