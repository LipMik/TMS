from random import randint

lst = [i for i in range(10, 20)]

some_dict = {}
for i, j in enumerate(lst):
    some_dict[i] = lst[i]

print(some_dict)

new_lst = []
for i, j in enumerate(lst):
    new_lst.insert(i, f'{i}- {j}')

print(new_lst)
