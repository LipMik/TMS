class Math:
    def __init__(self, n, m):
        self.n = n
        self.m = m

        self.r_sum = self.n + self.m
        self.r_raz = self.n - self.m
        self.r_pr = self.n * self.m

        try:
            self.rez_d = self.n / self.m
        except ZeroDivisionError:
            self.rez_d = 'Деление на ноль невозможно!'

        else:
            self.rez_d = self.n / self.m

        print(self.r_sum)
        print(self.r_raz)
        print(self.r_pr)
        print(self.rez_d)
