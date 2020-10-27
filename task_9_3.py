from random import randint


def my_decorator(method_to_decorate):
    def wrapper(l):
        new_lst = []
        for i, j in enumerate(l):
            if i % 2 == 0:
                new_lst.append(j)
        return method_to_decorate(new_lst)

    return wrapper


@my_decorator
def some_function(ls):
    print(ls)


lst = [randint(0, 10) for i in range(10)]
print(lst)

some_function(lst)
