import requests
import session_19.constants as constants

from session_19.data_collector import DataCollector
from session_19.person import Person

class DataCollectorAPI(DataCollector):
    def __init__(self):
        self.base_url = "http://127.0.0.1:5000"
    
    def get_patients(self):
        request_result = requests.get(f'{self.base_url}/patients')
        result = []
        if request_result.status_code == 200:
            person_list = request_result.json()
            for person_dict in person_list:
                person = Person(person_dict['id'], person_dict['name'], person_dict['lname'], person_dict['age'], person_dict['gender'])
                person.is_sick = constants.POSIBLE_VALUES_SICK.get(person_dict['covid'].lower())
                result.append(person)
        return result

