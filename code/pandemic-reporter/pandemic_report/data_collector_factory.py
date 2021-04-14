# from data_collector import DataCollector
import pandemic_report.data_collector as data_collector
import pandemic_report.data_collector_api as data_collector_api
import pandemic_report.data_collector_csv as data_collector_csv

class DataCollectorFactory(object):
    @staticmethod
    def get_data_collector_instance(collector_type):
        instance = None
        subclasses = data_collector.DataCollector.__subclasses__()
        for cls in subclasses:
            if cls.__name__ == collector_type:
                instance = cls()

        return instance