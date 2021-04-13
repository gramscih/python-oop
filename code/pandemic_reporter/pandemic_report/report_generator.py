import pandemic_report.constants as constants

from pandemic_report.bitacora import Bitacora


class ReportGeneretor(object):

    def __init__(self, logger=None):
        self.bitacora = Bitacora()
        self.logger = logger

    # @staticmethod
    def get_sicks(self):
        self.logger.info("Generating report of sicks")
        result = len(self.bitacora.people_sick)
        return result

    def get_recover(self):
        self.logger.info("Generating report of recovered")
        result = len(self.bitacora.people_recovered)
        return result

    def get_sicks_by_gender(self, gender):
        result = 0
        for patient in self.bitacora.people_sick:
            if patient.gender.lower() == gender.lower() and patient.is_sick:
                result += 1
        return result

    def get_sicks_by_age(self, age):
        result = 0
        vals = constants.AGES.get(age)
        r = range(vals[0], vals[1])
        self.logger.debug(f"Range of age reviewed: {r}")
        for patients in self.bitacora.people_sick:
            self.logger.debug(f"Patient Age: {patients.age} is in range [{patients.age in r}] if is sick [{patients.is_sick}]")
            if patients.age in r and patients.is_sick:
                result += 1
        return result
