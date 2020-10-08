n = int(input('Enter START '))

i = 15

#1
a = []
a.append(n)
a.append(n)
j = 2

while j < i:
    a.insert(j, a[j-1] + a[j -2])
    j += 1

print(a)

#2
b = []
b.append(n)
b.append(n)
j = 0
for j in range(i-2):
    b.insert(j + 2, b[j] + b[j + 1])

print(b)
