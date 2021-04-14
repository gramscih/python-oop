import csv

from pandemic_report.person import Person
from pandemic_report.data_collector import DataCollector

# Need A refactor
class DataCollectorCsv(DataCollector):
    def __init__(self):
        self.__people = []
        self.__load_data()

    # This function need to return a tuple
    # (status, message, result) -> (200, "ok", [...])
    def get_patients(self):
        return self.__people

    def __load_data(self):
        with open('src/report.csv', 'r') as file:
            reader = csv.reader(file)
            # Reade result
            # "name, lastname, age, gender"
            # "name1, lastname1, 23, female"
            reader = list(reader)
            header = reader[0]
            for row in reader[1:]:
                p_dict = dict(zip(header, row))
                # TODO: Review KEY's to starize to work with different standards
                p = Person(p_dict["Id"], p_dict["Name"], p_dict["Last Name"], p_dict["Age"], p_dict["Gender"])
                # TODO: try to use tother than magic values -> "Positive"
                p.is_sick = p_dict["Covid"] == 'Positive'
                self.__people.append(p)