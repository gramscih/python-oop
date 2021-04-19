import logging
import pandemic_report.constants as constants

from pandemic_report.bitacora import Bitacora
from pandemic_report.data_collector_factory import DataCollectorFactory
from pandemic_report.custom_exceptions import ExceptionEmptyValues, ExceptionNoInstanceFound

class DataLoader(object):
    def __init__(self, logger=None):
        self.__bitacora = Bitacora()
        self.logger = logger if logger else logging.getLogger()

    def load_data(self):
        self.logger.debug("Starting data loading...")
        status = True
        error = ""
        for collector_name in constants.DATA_COLLECTORS:
            try:
                data_collector = self.__get_instance(collector_name)
                patients = self.__get_data(data_collector)
                self.logger.debug(f"Patients recovered {patients} - for collector [{collector_name}]")
            except ExceptionNoInstanceFound as ex:
                self.logger.debug(f"load_data: Exception [{ex}] - For collector name [{collector_name}]")
                status = False
                error = "Not Conllector Instance"
                continue
            except ExceptionEmptyValues as ex:
                self.logger.debug(f"load_data: Exception [{ex}] - No values for collector name [{collector_name}]")
                error = "Empty values"
                continue
            except Exception as ex:
                self.logger.debug(f"load_data: Exception [{ex}]]")
                continue

            if not patients:
                self.logger.debug(f"load_data: No data for the following collector {collector_name}")
                continue
            
            for patient in patients:
                if patient.is_sick:
                    self.__bitacora.add_sick_person(patient)
                else:
                    self.__bitacora.add_helthy_person(patient)
        return (status, error)
        
    def registry_patient(self, person):
        print(constants.POSIBLE_VALUES_SICK.get(person.is_sick.lower()))
        if constants.POSIBLE_VALUES_SICK.get(person.is_sick.lower()):
            self.__bitacora.add_sick_person(person)
        else:
            self.__bitacora.add_helthy_person(person)
    
    def __get_data(self, collector):
        values = collector.get_patients()
        return values[-1]

    def __get_instance(self, collector_name):
        self.logger.info("Calling get instance...")
        data_collector = DataCollectorFactory.get_data_collector_instance(collector_name)
        if not data_collector:
            raise ExceptionNoInstanceFound()
        return data_collector