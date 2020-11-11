from abc import ABC, abstractmethod


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure(ABC):

    @abstractmethod
    def perimetr(self) -> None:
        pass

    @abstractmethod
    def area(self) -> None:
        pass


class Circle(Figure):

    def __init__(self, centre: Point, radius):
        self.center = centre
        self.r = radius
        self.pi = 3.1415

    def area(self):
        area = self.pi * self.r ** 2
        return area

    def perimetr(self):
        per = 2 * self.pi * self.r
        return per


class Triangle(Figure):

    def __init__(self, a_coord: Point, b_coord: Point, c_coord: Point):
        self.a = a_coord
        self.b = b_coord
        self.c = c_coord

    def area(self):
        area = 0.5 * abs((self.b.x - self.a.x) * (self.c.y - self.a.y) - \
                      (self.c.x - self.a.x) * (self.b.y - self.a.y))
        return area

    def perimetr(self):

        len_ab = (((self.b.x - self.a.x) ** 2) + ((self.b.y - self.a.y) ** 2)) ** 0.5
        len_bc = (((self.c.x - self.b.x) ** 2) + ((self.c.y - self.b.y) ** 2)) ** 0.5
        len_ca = (((self.c.x - self.a.x) ** 2) + ((self.c.y - self.a.y) ** 2)) ** 0.5
        per = len_ab + len_bc + len_ca

        return per


class Squere(Figure):

    def __init__(self, a_coord: Point, c_coord: Point):
        self.a = a_coord
        self.c = c_coord

    def perimetr(self):
        self.len_ab = ((self.a.x - self.c.x) ** 2 + (self.a.y - self.c.y) ** 2) ** 0.5
        per = self.len_ab * 4
        return per

    def area(self):
        area = self.len_ab ** 2
        return area
