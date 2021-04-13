import csv

from pandemic_reporter.pandemic_report.person import Person
from pandemic_reporter.pandemic_report.data_collector import DataCollector

class DataCollectorCsv(DataCollector):
    def __init__(self):
        self.__people = []
        self.__load_data()

    def get_patients(self):
        return self.__people

    def __load_data(self):
        with open('src/report.csv', 'r') as file:
            reader = csv.reader(file)
            print(reader)
            reader = list(reader)
            header = reader[0]
            for row in reader[1:]:
                p_dict = dict(zip(header, row))
                # TODO: Review KEY's to starize to work with different standards
                p = Person(p_dict["Id"], p_dict["Name"], p_dict["Last Name"], p_dict["Age"], p_dict["Gender"])
                # TODO: try to use tother than magic values -> "Positive"
                p.is_sick = p_dict["Covid"] == 'Positive'
                self.__people.append(p)