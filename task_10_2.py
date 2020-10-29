import csv
from datetime import datetime

fields = ['date', 'place', 'degree', 'speed_wind']
rows = [
    ['22.10.2020', 'Minsk', '14', '7'],
    ['23.10.2020', 'Minsk', '11', '7'],
    ['24.10.2020', 'Minsk', '10', '5'],
    ['25.10.2020', 'Minsk', '17', '2'],
    ['26.10.2020', 'Minsk', '14', '8'],
    ['27.10.2020', 'Minsk', '8', '9'],
    ['28.10.2020', 'Minsk', '4', '5'],
    ['29.10.2020', 'Minsk', '9', '3'],
    ['22.10.2020', 'Grodno', '14', '7'],
    ['22.10.2020', 'Brest', '14', '7'],
    ['21.10.2020', 'Minsk', '14', '7'],
]
filename = "weather_file.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

today = datetime.today()

days = 0
temp = 0
speed = 0
week = 7

with open('weather_file.csv', encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")

    for row in file_reader:
        # date = datetime.strptime(row[0], "%d.%m.%Y")

        if row[1] == 'Minsk':
            days += 1
            temp += float(row[2])
            speed += float(row[3])

meedle_temp = float(temp / days)
meedle_speed = float(speed / days)

print(meedle_temp)
print(meedle_speed)
