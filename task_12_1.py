class Time:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], Time):
            self.__init_with_instance(*args)
        elif len(args) == 1 and type(args[0]) is str:
            self.h, self.m, self.s = map(int, args[0].split(':'))
        elif len(args) == 1 and type(args[0]) is int:
            self.h = int(str(args[0])[:2])
            self.m = int(str(args[0])[2:4])
            self.s = int(str(args[0])[4:])
        elif len(args) == 3:
            self.h = args[0]
            self.m = args[1]
            self.s = args[2]
        else:
            self.h = 0
            self.m = 0
            self.s = 0

    def __init_with_instance(self, *args):
        o = args[0]
        self.h = o.h
        self.m = o.m
        self.s = o.s

    def __eq__(self, other):
        return self.h == other.h and self.m == other.m and self.s == other.s

    def __add__(self, other):
        seconds = self.h * 60 * 60 + self.m * 60 + self.s
        new_hours = seconds % (60 * 60)
        new_minutes = (seconds - new_hours * 60 * 60) // 60
        new_seconds = (seconds - new_hours * 60 * 60) % 60
        return Time(
            new_hours,
            new_minutes,
            new_seconds,
        )

    def __str__(self):
        return f'Time is {self.h}:{self.m}:{self.s}'

    # def __eq__(self, other):
    #     return 0



t = Time(25, 20, 40)
print(t)
# t = Time('10:20:40')
# print(t)
# t1 = Time('10:20:40')
#
# print(t1)
# t2 = Time(t1)
# print(t2)
# t3 = Time(t2)
# print(t3)
#
# t4 = Time(t2)
# t = Time(Time(Time(Time(Time('10:20:40')))))
# t = Time(t4)
# t = Time()
# t = Time(1, 142, 53, 54)


