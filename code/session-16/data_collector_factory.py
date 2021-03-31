# from data_collector import DataCollector
import data_collector
import data_collector_api
import data_collector_csv

from builtins import object                 

class DataCollectorFactory(object):
    @staticmethod
    def get_data_collector_instance(collector_type):
        instance = None
        subclasses = data_collector.DataCollector.__subclasses__()
        for cls in subclasses:
            if cls.__name__ == collector_type:
                instance = cls()

        return instance