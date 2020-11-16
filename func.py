from exceptions import null_exc


def calculater_dif(n, m):
    n = float(n)
    m = float(m)

    rez_dif = n - m
    print(rez_dif)


def calculater_sum(n, m):
    rez_s = n + m
    print(rez_s)


def calculater_pr(n, m):
    rez_p = n * m
    print(rez_p)


def calculater_del(n, m):
    rez_d = null_exc(n, m)
    print(rez_d)
