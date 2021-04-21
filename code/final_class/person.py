class Person(object):
    def __init__(self, ci, name, lastname):
        self.__ci = ci
        self.__name = name
        self.__lastname = lastname

    def introduce_your_self(self):
        print(f"Hello, My name is {self.__name} {self.__lastname}")