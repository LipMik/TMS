import csv

fields = ['firstname', 'lastname', 'age']
rows = [
    ['Ivan', 'Ivanov', '3'],
    ['Petr', 'Ivanov', '28'],
    ['Petr', 'Ivanov', '10'],
    ['Vasili', 'Sidorov', '15'],
    ['Mikalai', 'Sidorov', '16'],
    ['Vasili', 'Sidorov', '46']
]
filename = "first_file.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

count_1_12 = 0
count_13_18 = 0
count_19_25 = 0
count_26_40 = 0
count_40 = 0

with open('first_file.csv', encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")

    for row in file_reader:
        if row[2] == 'age':
            continue
        elif 12 >= int(row[2]) >= 1:
            count_1_12 += 1
        elif 18 >= int(row[2]) >= 13:
            count_13_18 += 1
        elif 25 >= int(row[2]) >= 19:
            count_19_25 += 1
        elif 40 >= int(row[2]) >= 26:
            count_26_40 += 1
        elif int(row[2]) >= 40:
            count_40 += 1

print('1 -12:', count_1_12)
print('13 - 18:', count_13_18)
print('19 - 25:', count_19_25)
print('26 - 40:', count_26_40)
print('> 40:', count_40)
