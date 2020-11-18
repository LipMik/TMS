import argparse
from _datetime import datetime
import time

parser = argparse.ArgumentParser()
parser.add_argument('user_name', help='Имя пользователя', type=str, default='Микалай')
parser.add_argument('last_name', help='Фамилия пользователя', type=str, default='Липский')
parser.add_argument('pomodoro_m', help='Время работы', type=int, default=25)
parser.add_argument('pause', help=' Пауза (мин.)', type=int, default=5)
parser.add_argument('count_of_cycle', help='Количество циклов', type=int, default=4)
parser.add_argument('count_of_cycle', help='Название задачи', type=str)
args = parser.parse_args()

with open('log2.txt', 'a+') as log:
    log.writelines(f'{args.user_name} : {args.last_name} : {datetime.now()}\n')

cycle = 0
work_time = int(args.pomodoro_m * 60)
pause_time = int(args.pause * 60)

while cycle < args.count_of_cycle:
    print('Pomodoro started! Work!')
    print(f'Time : {args.pomodoro_m} min')
    time.sleep(work_time)
    print(f'Stop work!Pause {pause_time}')
    time.sleep(pause_time)
    cycle += 1
