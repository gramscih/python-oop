from abc import ABC, abstractmethod

class Reader(ABC):
    @abstractmethod
    def get_people(self):
        pass