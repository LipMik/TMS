class MyTime:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], MyTime):
            self.__init_with_instance(*args)
            self.normal_view(*args)
        elif len(args) == 1 and type(args[0]) is str:
            self.h, self.m, self.s = map(int, args[0].split(':'))
            self.normal_view(*args)
        elif len(args) == 1 and type(args[0]) is int:
            self.h = int(str(args[0])[:2])
            self.m = int(str(args[0])[2:4])
            self.s = int(str(args[0])[4:])
            self.normal_view(*args)
        elif len(args) == 3:
            self.h = args[0]
            self.m = args[1]
            self.s = args[2]
            self.normal_view(*args)
        else:
            self.h = 0
            self.m = 0
            self.s = 0

    def normal_view(self, *args):
        seconds = self.h * 60 * 60 + self.m * 60 + self.s
        self.h = seconds // (60 * 60)
        self.m = (seconds - self.h * 60 * 60) // 60
        self.s = (seconds - self.h * 60 * 60) % 60
        return self

    def __init_with_instance(self, *args):
        o = args[0]
        self.h = o.h
        self.m = o.m
        self.s = o.s

    def __eq__(self, other):
        return self.h == other.h and self.m == other.m and self.s == other.s

    def __ne__(self, other):
        return self.h != other.h or self.m != other.m or self.s != other.s

    def __gt__(self, other):
        return self.h > other.h or (self.h == other.h and self.m > other.m) \
               or (self.h == other.h and self.m == other.m and self.s > other.s)

    def __lt__(self, other):
        return self.h < other.h or (self.h == other.h and self.m < other.m) \
               or (self.h == other.h and self.m == other.m and self.s < other.s)

    def __ge__(self, other):
        return self.h >= other.h or (self.h == other.h and self.m >= other.m) \
               or (self.h == other.h and self.m == other.m and self.s >= other.s)

    def __le__(self, other):
        return self.h <= other.h or (self.h == other.h and self.m <= other.m) \
               or (self.h == other.h and self.m == other.m and self.s <= other.s)

    def __add__(self, other):
        return MyTime(self.h + other.h, self.m + other.m,  self.s + other.s)

    def __sub__(self, other):
        return MyTime(self.h - other.h, self.m - other.m, self.s - other.s)

    def __str__(self):
        return f'Time is {self.h}:{self.m}:{self.s}'

    def __mul__(self, other):
        return MyTime(self.h * other, self.m * other, self.s * other)


t = MyTime(10, 69, 30)
print(t)
t2 = MyTime(10, 20, 30)
print(t2)
t3 = t + t2
print(t3)
print(t - t2)
print(t * 2)
