a = []

n = int(input('Enter N '))
a = [(input('')) for i in range(n)]

#1
b = a[1:]
b.append(a[0])

print(b)

#2
b = []
for i in range(n):
    b.insert(i-1, a[i])

print(b)

#3
c = []
i = 0
while i < n :
   c.insert(i-1, a[i] )
   i +=1

print(c)