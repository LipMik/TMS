from task_12_2 import *


if __name__ == '__main__':
    a = Point(1, 1)
    b = Point(5, 5)
    c = Point(1, 9)

    triangle = Triangle(a, b, c)
    triangle.perimetr()
    triangle.squere()

    squere = Squere(a, b)
    squere.perimetr()
    squere.perimetr()

    circle = Circle(a, 10)
    circle.squere()
    circle.perimetr()
