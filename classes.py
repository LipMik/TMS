class Math:
    @staticmethod
    def calculater_sum(n, m):
        n = n
        m = m
        r_sum = n + m
        print(r_sum)

    @staticmethod
    def calculater_dif(n, m):
        n = n
        m = m
        r_raz = n - m
        print(r_raz)

    @staticmethod
    def calculater_pr(n, m):
        n = n
        m = m
        r_pr = n * m
        print(r_pr)

    @staticmethod
    def calculater_del(n, m):
        n = n
        m = m
        try:
            rez_d = n / m
        except ZeroDivisionError:
            rez_d = 'Деление на ноль невозможно!'
            print(rez_d)
        else:
            rez_d = n / m
            print(rez_d)
