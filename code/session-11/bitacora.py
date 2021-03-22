class Bitacora(object):
    def __init__(self):
        print("Some thing")
        self.__people_sick = []
        self.__people_recovered = []
        self.__people_helthy = []

    def add_sick_person(self, person):
        self.__people_sick.append(person)

    def add_recovered_person(self, person):
        self.__people_recovered.append(person)

    def add_helthy_person(self, person):
        self.__people_helthy.append(person)

    def remove_sick_person(self, person):
        self.__people_sick.remove(person)

    @property
    def people_sick(self):
        return self.__people_sick

    @property
    def people_recovered(self):
        return self.__people_recovered

    @property
    def people_helthy(self):
        return self.__people_helthy
