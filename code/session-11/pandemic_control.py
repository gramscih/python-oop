import report_generator

from person import Person

class PandemicControl(object):
    def __init__(self, city):
        self.__city = city
        self.__people = []

    @property
    def city(self):
        return self.__city

    @property
    def people(self):
        return self.__people

    @people.setter
    def people(self, new_value):
        self.__people = new_value

    def print_report(self):
        print(f"----------------------For the City: [{self.__city}]----------------------")
        sick_number = report_generator.get_sicks(people)
        recovered = report_generator.get_recover(people)
        print(f"The number of persons that are sick is [{sick_number}]")
        print(f"The number of persons that are recovered from the sickness is [{recovered}]")

        print(self.__people)


person1 = Person("name1", "last_name1", 45, "Male")
person2 = Person("name2", "last_name2", 30, "Female")
person3 = Person("name3", "last_name3", 30, "Male")

person3.is_sick = True

people = [person1, person2, person3]

p = PandemicControl("Cbba")
p.people = people
p.print_report()

