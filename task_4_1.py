a = []

n = int(input('Enter the number of elements '))
a = [int(input('')) for i in range(n)]
print(a)

#1
b = []
for i in a:
    b.append(i*(-2))

print(b)

#2
b = []
i = 0
while i < len(a):
    i += 1
    b.append(i* -2)

print(b)