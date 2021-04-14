import requests
import pandemic_report.constants as constants

from pandemic_report.data_collector import DataCollector
from pandemic_report.person import Person

class DataCollectorAPI(DataCollector):
    def __init__(self):
        self.base_url = "http://127.0.0.1:5000"
    
    def get_patients(self):
        try:
            request_result = requests.get(f'{self.base_url}/patients')
        except requests.exceptions.ConnectionError as ex:
            raise ex
        result = []
        status = constants.POSIBLE_STATUS_CODES.get(request_result.status_code)
        if status.get("is_good"):
            person_list = request_result.json()
            for person_dict in person_list:
                person = Person(person_dict['id'], person_dict['name'], person_dict['lname'], person_dict['age'], person_dict['gender'])
                person.is_sick = constants.POSIBLE_VALUES_SICK.get(person_dict['covid'].lower())
                result.append(person)

        return (request_result.status_code, status.get("message"), result)

