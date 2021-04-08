import constants
import logging
import os

from data_loader import DataLoader
from report_generator import ReportGeneretor

run = True

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

def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(constants.LOG_FORMATTER)

    file_handler = logging.FileHandler(constants.LOG_FILE)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger

logger = get_logger()
rpt = ReportGeneretor(logger)
dl = DataLoader(logger)
dl.load_data()
logger.debug("Starting Application...")
while run:
    print("***********************************************************")
    print("1. All people sick")
    print("2. Classified by gender")
    print("3. Classified by Ege")
    print("4. Get a complete report")
    print("4. Get a complete report")

    print("5. Exit")
    print("***********************************************************")
    opt = input("Select an option: ")
    if opt == '5':
        run = False
    else:
        generate_report(opt)
    
# if __name__ == "__main__":
#     logger = get_logger()