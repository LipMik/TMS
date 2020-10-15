n = 200
m = 300

def s_dell (a: int):
    summ = 0

    i = 1
    while i <= (a / 2):
        if a % i == 0:
            summ += i
        i += 1
    return (summ)

i = n
j = m

while i < n+((m-n)/2):
    s_n = s_dell(i)
    j = m
    while j > n:
        s_m = s_dell(j)
        if (s_n == j) and (s_m == i):
            print(i,j)
        j -= 1
    i +=1
