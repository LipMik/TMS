from exceptions import *
from classes import Math


def choice():
    log = bool
    while True:
        print('\t\tWelcome to calculate \n')
        choose = input('Enter \'go\' to continuation or \'break\' to exit \n')
        if choose == 'go'.lower():
            log = True
            break
        elif choose == 'break'.lower():
            print('Bye!')
            log = False
            break
    return log


def ui_func():
    answer = True
    while answer:
        answer = choice()
        if answer == False:
            break

        a = enter_exc()
        b = enter_exc()
        Math(a, b)
