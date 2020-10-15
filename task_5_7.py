from operator import index
from random import randint

def create():
    n = randint(2,6)
    m = n
    matr = []

    matr = [[randint(1,50) for j in range(n)] for i in range(n)]

    return(matr)


matr = create()
print(matr)

for i,j in enumerate(matr):
    m = max(j)
    ind_m = j.index(max(j))

    gl = j[i]
    j[i] = m
    j[ind_m] = gl
    print(j)


