import csv

from person import Person

class Bitacora(object):
    def __init__(self):
        self.__people_sick = []
        self.__people_recovered = []
        self.__people_helthy = []
        self.__load_data()

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

    def __load_data(self):
        with open('src/report.csv', 'r') as file:
            reader = csv.reader(file)
            reader = list(reader)
            header = reader[0]
            for row in reader[1:]:
                p_dict = dict(zip(header, row))
                # TODO: Review KEY's to starize to work with different standards
                p = Person(p_dict["Id"], p_dict["Name"], p_dict["Last Name"], p_dict["Age"], p_dict["Gender"])
                # TODO: try to use tother than magic values -> "Positive"
                p.is_sick = p_dict["Covid"] == 'Positive'
                if p.is_sick:
                    self.add_sick_person(p)
                else:
                    self.__people_helthy.append(p)
                

b = Bitacora()
