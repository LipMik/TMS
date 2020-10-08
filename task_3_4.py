string = input('Enter string: ')

centr = int (len(string) / 2)

print(string[(centr-1):centr])

if string[centr] == string[0]:
    print(string[1:len(string)-1])
