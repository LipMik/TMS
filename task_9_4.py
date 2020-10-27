def my_decorator(change_order):
    def wrapper(*args):
        test_lst = []
        for i in args:
            test_lst.extend(i)

        new_order = []
        for i in reversed(test_lst):
            new_order.append(i)
        return change_order(new_order)

    return wrapper


@my_decorator
def some_function(ls):
    print(ls)


old_order = [i for i in range(10)]
print(old_order)

some_function(old_order)