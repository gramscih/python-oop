from unittest import mock
from pandemic_reporter.pandemic_report.data_loader import DataLoader
from pandemic_reporter.pandemic_report.person import Person
from pandemic_reporter.pandemic_report.bitacora import Bitacora

class MockCollector(object):
    def __init__(self, mode=None):
        self.patients = []
        self.fill_patients(mode)

    def get_patients(self):
        return self.patients

    def fill_patients(self, mode):
        if not mode:
            p1 = Person(1, "name1", "last_name1", 23, "Female")
            p2 = Person(2, "name2", "last_name2", 24, "Female")
            p3 = Person(3, "name3", "last_name3", 25, "Male")
            p4 = Person(4, "name4", "last_name4", 26, "Female")
            p5 = Person(5, "name5", "last_name5", 27, "Male")
            self.patients.append(p1)
            self.patients.append(p2)
            self.patients.append(p3)
            self.patients.append(p4)
            self.patients.append(p5)

# Other posible solutions to Mock empty values
# class MockCollectorEmpty(object):
#     def __init__(self):
#         self.patients = []
#         # self.fill_patients()

#     def get_patients(self):
#         return self.patients

@mock.patch("pandemic_reporter.pandemic_report.data_loader.DataCollectorFactory.get_data_collector_instance")
def test_load_data_correct_loading(mock_get_collector_instance):
    mock_get_collector_instance.return_value = MockCollector()
    dt = DataLoader()
    (status, error) = dt.load_data()
    assert status == True

@mock.patch("pandemic_reporter.pandemic_report.data_loader.DataCollectorFactory.get_data_collector_instance")
def test_load_data_none_collector(mock_get_collector_instance):
    mock_get_collector_instance.return_value = None
    dt = DataLoader()
    (status, error) = dt.load_data()
    assert status == False
    assert error == "Not Conllector Instance"

@mock.patch("pandemic_reporter.pandemic_report.data_loader.DataCollectorFactory.get_data_collector_instance")
def test_load_data_empty_result(mock_get_collector_instance):
    mock_get_collector_instance.return_value = MockCollector("Empty")
    dt = DataLoader()
    (status, error) = dt.load_data()
    assert status == True
