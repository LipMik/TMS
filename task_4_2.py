a = []

n = int(input('Enter N '))
a = [int(input('')) for i in range(n)]

#1
c = 0

for i in range(n):
    if a[i]%2 == 0:
        c += 1

print(c)

#2
c = 0
i = 0
while i < n:
    if a[i] % 2 == 0:
        c += 1
    i += 1
print(c)