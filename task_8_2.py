def chek(strk):
    lenght = int((len(strk)) / 2)

    if len(strk) % 2 != 0:
        list_1 = list(strk[:lenght])
        list_2 = list(strk[lenght + 1:])
    else:
        list_1 = list(strk[:lenght])
        list_2 = list(strk[lenght:])

    rez = 'Palindrom'
    for i in range(len(list_1)):
        if list_1[i] != list_2[len(list_1) - (i + 1)]:
            rez = 'Not_Palindrom'

    return rez


lst = ['abba', 'abca', 'abcbca']
rez = []

for i in lst:
    rez.append(chek(i))

print(rez)
