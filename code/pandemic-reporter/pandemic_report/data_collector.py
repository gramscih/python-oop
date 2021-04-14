from abc import ABC, abstractmethod

class DataCollector(ABC):

    @abstractmethod
    def get_patients(self):
        pass
