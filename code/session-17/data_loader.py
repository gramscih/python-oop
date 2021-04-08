from bitacora import Bitacora
from data_collector_factory import DataCollectorFactory

class DataLoader(object):
    def __init__(self, logger=None):
        self.__bitacora = Bitacora()
        self.logger = logger

    def load_data(self):
        self.logger.debug("Starting data loading...")
        data_collector = DataCollectorFactory.get_data_collector_instance("DataCollectorCsv")
        patients = data_collector.get_patients()
        for patient in patients:
            if patient.is_sick:
                self.__bitacora.add_sick_person(patient)
            else:
                self.__bitacora.add_helthy_person(patient)

