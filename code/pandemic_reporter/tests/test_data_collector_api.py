from pandemic_reporter.pandemic_report.person import Person
from pandemic_reporter.pandemic_report.data_collector_api import DataCollectorAPI
from unittest import mock

class MockResponse(object):
    def __init__(self, mode=None):
        self.mode = mode

    @property
    def status_code(self):
        return 200

    def json(self):
        if self.mode == "empty":
            return []
        result = [{"id": 1, "name": "name1", "lname": "Last Name1", "age": "45", "gender": "Male", "covid": "Positive"}]
        return result

@mock.patch('pandemic_reporter.pandemic_report.data_collector_api.requests.get')
def test_get_empty_patients(mock_get):
    mock_get.return_value = MockResponse("empty")
    data_collector_api = DataCollectorAPI()
    result = data_collector_api.get_patients()
    assert result == []

@mock.patch('pandemic_reporter.pandemic_report.data_collector_api.requests.get')
def test_get_patients(mock_get):
    mock_get.return_value = MockResponse()
    data_collector_api = DataCollectorAPI()
    result = data_collector_api.get_patients()
    p = Person(1, "name1", "Last Name1", "45", "Male")
    p.is_sick = True
    assert result == [p]
