from random import randint


def create_matrix(n: int, m: int):
    matr = [[randint(10, 50) for i in range(n)] for j in range(m)]
    return matr


def summ_matrix(matr: list):
    summ = 0
    for row in matr:
        for elem in row:
            summ += elem
    return summ


def max_of_matrix(matr: list):
    return max(max(matr))


def min_of_matrix(matr: list):
    return min(min(matr))


def ind_max_line(matr: list):
    max = 0
    ind_max = 0
    for i, j in enumerate(matr):
        if sum(j) > max:
            ind_max = i
            max = sum(j)
    return ind_max


def ind_min_line(matr: list):
    minn = 0
    ind_min = 0
    for i, j in enumerate(matr):
        if sum(j) < minn:
            ind_min = i
            minn = sum(j)
    return ind_min


def summ_column(matr):
    rez = [sum(i) for i in zip(*matr)]
    return rez


def ind_column(matr):
    ind_min = matr.index(min(matr))
    ind_max = matr.index(max(matr))
    return ind_min, ind_max


def nul_down(matr, x, y):
    for i in range(y):
        for j in range(i + 1, x):
            matr[j][i] = 0
    return matr


def nul_up(matr, x, y):
    for i in range(y):
        for j in range(i + 1, x):
            matr[i][j] = 0
    return matr


n = int(input('Enter N: '))
m = int(input('Enter M: '))

matrix = create_matrix(n, m)
print(matrix)

summ_matr = summ_matrix(matrix)
print(summ_matr)

max_matrix = max_of_matrix(matrix)
print(max_matrix)

min_matrix = min_of_matrix(matrix)
print(min_matrix)

max_line = ind_max_line(matrix)
print(max_line)

min_line = ind_min_line(matrix)
print(min_line)

s_column = summ_column(matrix)
print(s_column)

min_column, max_column = ind_column(s_column)
print(max_column)
print(min_column)

matrix = nul_down(matrix, n, m)
print(matrix)

matrix = nul_up(matrix, n, m)
print(matrix)

matrix_a = create_matrix(n, m)
matrix_b = create_matrix(n, m)
print(matrix_a)
print(matrix_b)
