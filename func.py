from exceptions import null_exc


def calculater(n, m):
    n = float(n)
    m = float(m)
    rez_s = n + m
    rez_r = n - m
    rez_p = n * m
    rez_d = null_exc(n, m)

    print(rez_s)
    print(rez_r)
    print(rez_p)
    print(rez_d)
