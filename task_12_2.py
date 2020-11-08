class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, centre: Point, radius):
        self.center = centre
        self.r = radius
        self.pi = 3.1415

    def sqr(self):
        s = self.pi * self.r ** 2
        return s

    def len_circle(self):
        ln_c = 2 * self.pi * self.r
        return ln_c


class Triangle(Point):
    def __init__(self, a_coord: Point, b_coord: Point, c_coord: Point):
        self.a = a_coord
        self.b = b_coord
        self.c = c_coord

    def sq(self):
        s = 0.5 * abs((self.b.x - self.a.x) * (self.c.y - self.a.y) - \
                      (self.c.x - self.a.x) * (self.b.y - self.a.y))
        return s

    def len_abc(self):
        len_ab = (((self.b.x - self.a.x) ** 2) + ((self.b.y - self.a.y) ** 2)) ** 0.5
        len_bc = (((self.c.x - self.b.x) ** 2) + ((self.c.y - self.b.y) ** 2)) ** 0.5
        len_ca = (((self.c.x - self.a.x) ** 2) + ((self.c.y - self.a.y) ** 2)) ** 0.5
        per = len_ab + len_bc + len_ca

        return per


class Squere:
    def __init__(self, a_coord: Point, c_coord: Point):
        self.a = a_coord
        self.c = c_coord

    def sq(self):
        self.len_ab = ((self.a.x - self.c.x) ** 2 + (self.a.y - self.c.y) ** 2) ** 0.5
        s = self.len_ab ** 2
        return s

    def per_sq(self):
        return self.len_ab * 4


a = Point(1, 1)
b = Point(5, 5)
c = Point(1, 9)
tr = Triangle(a, b, c)
print(tr.sq())
print(tr.len_abc())
