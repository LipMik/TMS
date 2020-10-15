n = int(input('Enter N: '))

sum = 0
pr = 1
if n == 0:
    pr = 0

while n > 0:
    sum += (n % 10)
    pr *= (n % 10)
    n = int(n / 10)

print(sum)
print(pr)