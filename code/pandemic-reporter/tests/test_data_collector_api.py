import requests
import pytest

from pandemic_report.person import Person
from pandemic_report.data_collector_api import DataCollectorAPI
from unittest import mock

class MockResponse(object):
    def __init__(self, status_mode=200, json_mode=None):
        self.status_mode = status_mode
        self.json_mode = json_mode

    @property
    def status_code(self):
        return self.status_mode

    def json(self):
        if self.json_mode == "empty":
            return []
        result = [{"id": 1, "name": "name1", "lname": "Last Name1", "age": "45", "gender": "Male", "covid": "Positive"}]
        return result

@mock.patch('pandemic_report.data_collector_api.requests.get')
def test_get_empty_patients(mock_get):
    mock_get.return_value = MockResponse(json_mode="empty")
    data_collector_api = DataCollectorAPI()
    result = data_collector_api.get_patients()
    assert result == (200, "OK", [])

@mock.patch('pandemic_report.data_collector_api.requests.get')
def test_get_patients(mock_get):
    mock_get.return_value = MockResponse()
    data_collector_api = DataCollectorAPI()
    result = data_collector_api.get_patients()
    p = Person(1, "name1", "Last Name1", "45", "Male")
    p.is_sick = True
    assert result == (200, "OK", [p])

@mock.patch('pandemic_report.data_collector_api', **{'return_value.requests.get': requests.exceptions.ConnectionError()})
def test_get_patients_connection_error(mock_get):
    with pytest.raises(requests.exceptions.ConnectionError):
        data_collector_api = DataCollectorAPI()
        result = data_collector_api.get_patients()

@mock.patch('pandemic_report.data_collector_api.requests.get')
def test_get_patients_bad_request(mock_get):
    mock_get.return_value = MockResponse(404)
    data_collector_api = DataCollectorAPI()
    result = data_collector_api.get_patients()
    assert result == (404, "Not Found", [])

@mock.patch('pandemic_report.data_collector_api.requests.get')
def test_get_patients_request_timeout(mock_get):
    mock_get.return_value = MockResponse(408)
    data_collector_api = DataCollectorAPI()
    result = data_collector_api.get_patients()
    assert result == (408, "Request timeout", [])