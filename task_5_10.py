import datetime

def dif_time(d : dict):
    trav_time = list(d.values())
    dif= (trav_time[0] - trav_time[1])

    return (dif)



dict = {
    1 : {
        'Moskva' : datetime.datetime(2017, 3, 5, 19, 30, 0),
        'Minsk' :  datetime.datetime(2017, 3, 5, 8, 7, )
    },
    2 : {
        'Brest' : datetime.datetime(2017, 3, 5, 19, 30, ),
        'Minsk' : datetime.datetime(2017, 3, 5, 11, 30, )
    },
    3 : {
        'Lida' : datetime.datetime(2017, 3, 5, 11, 30, ),
        'Grodno' : datetime.datetime(2017, 3, 5, 2, 10, )
    }
}

t = datetime.timedelta(hours=7)

print(t)
for i in dict.keys():
    d_time = dif_time(dict[i])
    if d_time >t:
        print(i)

