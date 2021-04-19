import pandemic_report.constants as constants
import logging
import os

from pandemic_report.person import Person
from pandemic_report.data_loader import DataLoader
from pandemic_report.report_generator import ReportGeneretor

logger = None
rpt = None
# dl = DataLoader(logger)
dl = None

def generate_report(opt):
    if opt == '1':
        sicks = rpt.get_sicks()
        print("Patients that are sicks are:", sicks)
    if opt == '2':
        men = rpt.get_sicks_by_gender('male')
        women = rpt.get_sicks_by_gender('female')
        print(f"Men that are sick are: [{men}]")
        print(f"Women that are sick are: [{women}]")
    if opt == '3':
        kid = rpt.get_sicks_by_age('kid')
        young = rpt.get_sicks_by_age('young')
        adult = rpt.get_sicks_by_age('adult')
        print(f"Kid's that are sick are: [{kid}]")
        print(f"Young that are sick are: [{young}]")
        print(f"Adults that are sick are: [{adult}]")
    if opt == '4':
        pass
    if opt == '5':
        p_id = input("ID: ")
        full_name = input("Full name: ")
        age = input("Age: ")
        gender = input("Gender: ")
        covid = input('Covid: ')
        registry(p_id, full_name, age, gender, covid)

def registry(id, full_name, age, gender, covid):
    name, lname = full_name.split(' ')
    person = Person(id, name, lname, age, gender)
    person.is_sick = True if covid else False
    dl.registry_patient(person)


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(constants.LOG_FORMATTER)

    file_handler = logging.FileHandler(constants.LOG_FILE)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger

# def initializer():
#     print('INITIALIZER')
#     logger = get_logger()
#     rpt = ReportGeneretor(logger)
#     print('INITIALIZER 2')
#     dl = DataLoader(logger)

def run_app():
    run = True
    print('RUN APP')
    global logger
    logger = get_logger()
    global rpt
    rpt = ReportGeneretor(logger)
    global dl
    dl = DataLoader(logger)
    print(f'RUN APP DATA LOADER [{dl}]')
    dl.load_data()
    logger.debug("Starting Application...")
    while run:
        print("***********************************************************")
        print("1. All people sick")
        print("2. Classified by gender")
        print("3. Classified by Ege")
        print("4. Get a complete report")
        print("5. Registry patient manualy")

        print("6. Exit")
        print("***********************************************************")
        opt = input("Select an option: ")
        if opt == '6':
            run = False
        else:
            generate_report(opt)
    

if __name__ == "__main__":
    run_app()
