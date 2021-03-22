class Person(object):
    def __init__(self, name, last_name, age, gender):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__gender = gender
        self.__is_sick = False

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def is_sick(self):
        return self.__is_sick

    @is_sick.setter
    def is_sick(self, new_value):
        self.__is_sick = new_value

    @property
    def gender(self):
        return self.__gender

    @property
    def age(self):
        return self.__age

