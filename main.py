from task_12_2 import *


if __name__ == '__main__':
    a = Point(1, 1)
    b = Point(5, 5)
    c = Point(1, 9)
    tr = Triangle(a, b, c)
    print(tr.sq())
    print(tr.len_abc())

