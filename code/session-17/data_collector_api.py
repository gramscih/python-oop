# import requests

import data_collector

class DataCollectorAPI(data_collector.DataCollector):
    def __init__(self):
        self.base_url = "data_collector"
    
    def get_patients(self):
        pass
        # result = requests.get(f'{self.base_url}/patients')
        # return result

