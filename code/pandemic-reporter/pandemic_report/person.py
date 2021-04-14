class Person(object):
    def __init__(self, id, name, last_name, age, gender):
        self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__gender = gender
        self.__is_sick = False

    @property
    def id(self):
        return self.__id

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

    @is_sick.setter
    def is_sick(self, new_value):
        self.__is_sick = new_value

    @property
    def gender(self):
        return self.__gender

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f"{self.__id} - {self.__name} - {self.__last_name} - {self.__age} - {self.__gender} - {self.__is_sick}"
    
    def __eq__(self, p_to_compare):
        return self.__id == p_to_compare.id and self.__name == p_to_compare.name and self.__last_name == p_to_compare.last_name and self.__gender == p_to_compare.gender and self.__is_sick == p_to_compare.is_sick

