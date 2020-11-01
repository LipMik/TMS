import csv
from datetime import datetime


rows = [
    ['22.10.2020', '25.10.2020', '25.10.1994', '25.10.2024', '25.10.2020'],
    ['23.10.2020', '25.10.2020', '25.10.2020', '25.10.2020'],
    ['25.10.2020', '25.10.2010', '14.02.2015', '29.01.2007'],
]
filename = "weather_file.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)

today = datetime.today()

days = 0
temp = 0
speed = 0
week = 7

with open('weather_file.csv', encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    lst = []

    for i in file_reader:

        for j in i:
            lst.append(datetime.strptime(j, "%d.%m.%Y"))

        m = min(lst)

print(m)


