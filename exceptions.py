def null_exc(n, m):
    try:
        rez_d = n / m
    except ZeroDivisionError:
        return 'Деление на ноль невозможно!'

    else:
        return rez_d


def enter_exc():
    while True:
        try:
            n = float(input('Введите число: '))
        except ValueError:
            print('Вы ввели не число. Попробуйте снова!')

        else:
            return float(n)
