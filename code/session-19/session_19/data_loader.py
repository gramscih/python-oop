import logging
import session_19.constants as constants

from session_19.bitacora import Bitacora
from session_19.data_collector_factory import DataCollectorFactory

class DataLoader(object):
    def __init__(self, logger=None):
        self.__bitacora = Bitacora()
        self.logger = logger if logger else logging.getLogger()

    def load_data(self):
        self.logger.debug("Starting data loading...")
        status = "Success"
        for collector_name in constants.DATA_COLLECTORS:
            data_collector = self.__get_instance(collector_name)
            if not data_collector:
                status = "Failed"
                self.logger.debug(f"load_data: Status [{status}] - collector name [{collector_name}]")
                continue
            patients = data_collector.get_patients()
            if len(patients) == 0:
                status = "Failed"
                self.logger.debug(f"load_data: Status [{status}] - collector name [{collector_name}] - No Data for that collecot")
                continue
            for patient in patients:
                if patient.is_sick:
                    self.__bitacora.add_sick_person(patient)
                else:
                    self.__bitacora.add_helthy_person(patient)
        return status
        

    def __get_instance(self, collector_name):
        self.logger.info("Calling get instance...")
        data_collector = DataCollectorFactory.get_data_collector_instance(collector_name)
        return data_collector
        # self.logger.debug(f"The instance that was created: [{data_collector}]")
        # patients = data_collector.get_patients()
        # self.logger.debug(f"From instance [{data_collector}] is returning [{patients}]: ")
        # return patients