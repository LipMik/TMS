lst = str( input('Enter st : '))

lst = lst.split(' ')
new_lst =[]

for i in reversed(lst):
    new_lst.append(i)

print(new_lst)
