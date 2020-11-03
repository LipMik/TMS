class Room:
    __rooms_counter = 0

    def __new__(cls, *args, **kwargs):
        print('It\'s a room')
        return super().__new__(cls)

    def __init__(self, number, length, width, master):
        self.__master = master
        self.__number = number
        self.lenght = length
        self.width = width
        Room.__rooms_counter += 1

    def booking(self):
        print('Room reserved')

    def status(self):
        print('Close')

    def __area_counter(self):
        self.__area = self.lenght * self.width

    def get_number(self):
        return self.__number

    def set_number(self, new_number):
        self.__number = new_number

    def get_master(self):
        return self.__master

    def set_master(self, new_master):
        self.__master = new_master


# room_1 = Room(1, 5, 6, 'Ivan')
# room_1.set_master('Vasay')
# room_1.status()
# room_1.booking()
# print(room_1.get_master())


class Car:

    def __init__(self, brand, year, color, master):
        self.__brand = brand
        self.__year = year
        self.__color = color
        self.__master = master

    def drive(self):
        print('Car is driving')

    def broke(self):
        print('Car is broken')

    def get_brand(self):
        return self.__brand

    def set_brand(self, new_brand):
        self.__brand = new_brand

    def get_year(self):
        return self.__year

    def set_year(self, new_year):
        self.__year = new_year

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__color = new_color

    def get_master(self):
        return self.__master

    def set_master(self, new_master):
        self.__master = new_master


# car_1 = Car('Toyota', 1995, 'red', 'Vasya')
# print(car_1.broke())
# car_1.drive()
# car_1.get_master()


class Cat:

    def __init__(self, breed, owner, weight):
        self.__breed = breed
        self.__owner = owner
        self.__weight = weight

    def voice(self):
        print('Myu')

    def play(self):
        print('the cat is plaing')

    def get_breed(self):
        return self.__breed

    def set_breed(self, new_breed):
        self.__breed = new_breed

    def get_owner(self):
        return self.__owner

    def set_owner(self, new_owner):
        self.__owner = new_owner

    def get_weght(self):
        return self.__weght

    def set_weight(self, new_weight):
        self.__weght = new_weight


# cat_1 = Cat('British', 'Sveta', 3)
# cat_1.play()
# cat_1.voice()


class Book:
    salary = 0

    def __init__(self, writer, page, price):
        self.__writer = writer
        self.__page = page
        self.__price = price

    def status(self):
        print('Book sold')

    def profit(self):
        self.salary += self.__price
        print(self.salary)

    def get_writer(self):
        return self.__writer

    def set_writer(self, new_writer):
        self.__writer = new_writer

    def get_page(self):
        return self.__page

    def set_page(self,new_page):
        self.__page = new_page

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price


# harry_potter = Book('Rowling', 500, 100)
# harry_potter.status()
# harry_potter.profit()


class Dog:

    def __init__(self, name, owner, age):
        self.__name = name
        self.__owner = owner
        self.__age = age

    def voice(self):
        print('Gav')

    def play(self):
        print('Jump!')

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_owner(self):
        return self.__owner

    def set_owner(self, new_owner):
        self.__owner = new_owner

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age


# dog_1 = Dog('Tuzik', 'Pasha', 5)
# dog_1.play()
# dog_1.voice()
# print(dog_1.get_owner())
# dog_1.set_owner('Sveta')
# print(dog_1.get_owner())
