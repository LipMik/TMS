def my_decorator(change_order):
    def wrapper(*args):
        test_lst = args

        new_order = []
        for i in reversed(test_lst):
            new_order.append(i)
        return change_order(new_order)

    return wrapper


@my_decorator
def some_function(*args):
    print(*args)


a = 1
b = 2
c = 3
some_function(a, b, c)