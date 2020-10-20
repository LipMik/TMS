def rez_function(i: float):
    some_dict = {
        1: ((lambda a, dm=2.54: dm * a)(i)),
        2: ((lambda a, cm=0.39: cm * a)(i)),
        3: ((lambda a, ml=1.61: ml * a)(i)),
        4: ((lambda a, km=0.62: km * a)(i)),
        5: ((lambda a, nt=0.45: nt * a)(i)),
        6: ((lambda a, kg=2.2: kg * a)(i)),
        7: ((lambda a, unc=28.35: unc * a)(i)),
        8: ((lambda a, gr=0.0353: gr * a)(i)),
        9: ((lambda a, gl=4.55: gl * a)(i)),
        10: ((lambda a, l_gl=0.22: l_gl * a)(i)),
        11: ((lambda a, pt=0.57: pt * a)(i)),
        12: ((lambda a, l_p=1.76: l_p * a)(i))
    }
    return some_dict.values()


number = 1
while number != 0:
    print('1: Дюймы в сантиметры \n' 
          '2: Сантиметры в дюймы\n'
          '3: Мили в километры\n'
          '4: Километры в мили\n'
          '5: Фунты в килограммы\n'
          '6: Килограммы в фунты\n'
          '7: Унции в граммы\n'
          '8: Граммы в унции\n'
          '9: Галлон в литры\n'
          '10: Литры в галлоны\n'
          '11: Пинты в литры\n'
          '12: Литры в пинты')
    number = int(input('Enter number of operation: '))
    val = float(input('Enter value: '))
    rezult = list(rez_function(val))
    print(rezult[number-1])
