# from data_collector import DataCollector
import data_collector

from builtins import object

class DataCollectorFactory(object):
    @staticmethod
    def get_data_collector_instance(collector_type):
        instance = None
        print(data_collector.DataCollector.__subclasses__())
        for cls in data_collector.DataCollector.__subclasses__():
            print(f"This should be the class {cls}")
            if cls.__name__ == collector_type:
                instance = cls()

        return instance