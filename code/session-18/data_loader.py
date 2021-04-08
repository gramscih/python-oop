import constants

from bitacora import Bitacora
from data_collector_factory import DataCollectorFactory

class DataLoader(object):
    def __init__(self, logger=None):
        self.__bitacora = Bitacora()
        self.logger = logger

    def load_data(self):
        self.logger.debug("Starting data loading...")
        for collector_name in constants.DATA_COLLECTORS:
            patients = self.__get_instance(collector_name)
            for patient in patients:
                if patient.is_sick:
                    self.__bitacora.add_sick_person(patient)
                else:
                    self.__bitacora.add_helthy_person(patient)

    def __get_instance(self, collector_name):
        self.logger.info("Calling get instance...")
        data_collector = DataCollectorFactory.get_data_collector_instance(collector_name)
        # self.logger.debug(f"The instance that was created: [{data_collector}]")
        patients = data_collector.get_patients()
        self.logger.debug(f"From instance [{data_collector}] is returning [{patients}]: ")
        return patients