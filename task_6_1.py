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


def summ_matrix_a_b(a: list, b: list):
    rezult_matr = [[0 for i in range(len(a))] for j in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            rezult_matr[i][j] = (int(a[i][j]) + int(b[i][j]))
    return rezult_matr


def difference_a_b(a: list, b: list):
    rezult_matr = [[0 for i in range(len(a))] for j in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            rezult_matr[i][j] = (int(a[i][j]) - int(b[i][j]))
    return rezult_matr


def multiplication(matr_a, g):
    for i in range(len(matr_a)):
        for j in range(len(matr_a[0])):
            matr_a[i][j] *= g
    return matr_a


n = int(input('Enter N: '))
m = int(input('Enter M: '))

matrix = create_matrix(n, m)
print(matrix)

summ_matr = summ_matrix(matrix)
print('Summa of elements', summ_matr)

max_matrix = max_of_matrix(matrix)
print('Max element', max_matrix)

min_matrix = min_of_matrix(matrix)
print('Min element', min_matrix)

max_line = ind_max_line(matrix)
print('Index of row with max element', max_line)

min_line = ind_min_line(matrix)
print('Index of line with min element',min_line)

s_column = summ_column(matrix)

min_column, max_column = ind_column(s_column)
print('Index of column with max element', max_column)
print('Index of column with min element', min_column)

matrix = nul_down(matrix, n, m)
print('replacing elements below the main diagonal', matrix)

matrix = nul_up(matrix, n, m)
print('replacing elements above the main diagonal', matrix)

matrix_a = create_matrix(n, m)
print('New matrix A', matrix_a)

matrix_b = create_matrix(n, m)
print('New matrix B', matrix_b)

matrix_c = summ_matrix_a_b(matrix_a, matrix_b)
print('Summ matrixs A and B', matrix_c)

matrix_c = difference_a_b(matrix_a, matrix_b)
print('Difference between A and B', matrix_c)

g = int(input('Enter g: '))
matrix_a = multiplication(matrix_a, g)
print('matrix_a * g', matrix_a)
