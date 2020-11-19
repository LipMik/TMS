import argparse
from _datetime import timedelta, datetime
import time

parser = argparse.ArgumentParser()
parser.add_argument('user_name', help='Имя пользователя', type=str, default='LMikalai')
parser.add_argument('start_h', help='Количество часов', type=int, default=0)
parser.add_argument('start_m', help='Количество минут', type=int, default=0)
parser.add_argument('start_s', help='Количество секунд', type=int, default=1)
args = parser.parse_args()

step = timedelta(seconds=1)
start_time = timedelta(hours=args.start_h, minutes=args.start_m, seconds=args.start_s)
finish = timedelta(hours=0, minutes=0, seconds=0)

with open('log.txt', 'a+') as log:
    log.writelines(f'{args.user_name} : {datetime.now()}')


def my_generator(start_time):
    while start_time > finish:

        time.sleep(1)
        start_time -= step
        yield start_time
        if start_time == finish:
            print('Alarm')


gen = my_generator(start_time)

for i in gen:
    print(f'Time : {i}')
