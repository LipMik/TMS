class Car:

    def __new__(cls, *args, **kwargs):
        print('It\'s a new car')
        return super().__new__(cls)

    def __init__(self, manufacture, model, year, speed = 0):
        self.__manufacture = manufacture
        self.__model = model
        self.__year = year
        self.__speed = speed

    def speed_up(self):
        self.__speed += 5

    def speed_down(self):
        self.__speed -= 5

    def speed_stop(self):
        self.__speed = 0

    def get_speed(self):
        return self.__speed

    def set_speed(self, s):
        self.__speed = s

    def speed_return(self):
        self.__speed *= (-1)


ford = Car('Ford', 'Fiesta', 2005, 90)

print(ford.get_speed())
ford.speed_up()
print(ford.get_speed())
ford.speed_up()
print(ford.get_speed())
ford.speed_down()
print(ford.get_speed())
ford.speed_return()
print(ford.get_speed())
ford.speed_return()
print(ford.get_speed())
