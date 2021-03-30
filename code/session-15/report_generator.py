import constants

# from reader_csv import ReaderCsv
from bitacora import Bitacora
from data_collector_factory import DataCollectorFactory

class ReportGeneretor(object):
    def __init__(self):
        self.bitacora = Bitacora()
        self.__load_data()

    @staticmethod
    def get_sicks():
        result = 0
        for p in csv.get_people():
            if p.is_sick:
                result += 1
        return result

    # @property
    # def bitacora(self):
    #     return se

    def __load_data(self):
        csv = DataCollectorFactory.get_data_collector_instance("DataCollectorCsv")
        patients = csv.get_patients()
        self.bitacora.people_helthy = patients


# TODO: REview how to handle recovered
# def get_recover(people):
#     result = 0
#     for person in people:
#         if not person.is_sick and person in bitacora.people_sick:
#             bitacora.add_recovered_person(person)
#             bitacora.remove_sick_person(person)
#             result += 1
#     return result


# def get_sicks_by_gender(people, gender):
#     result = 0
#     for person in people:
#         if person.gender == gender and person.is_sick:
#             bitacora.add_sick_person(person)
#             result += 1
#     return result


# def get_recovered_by_gender(people, gender):
#     result = 0
#     for person in people:
#         if person.gender == gender and not person.is_sick and person in bitacora.people_sick:
#             bitacora.add_recovered_person(person)
#             bitacora.remove_sick_person(person)
#             result += 1
#     return result

# # def get_man_sicks(people):
# #     result = 0
# #     for person in people:
# #         if person.gender == "Male" and person.is_sick:
# #             result += 1
# #     return result


# # def get_woman_sicks(people):
# #     result = 0
# #     for person in people:
# #         if person.gender == "Female" and person.is_sick:
# #             result += 1
# #     return result

# def get_sicks_by_age(people, age):
#     result = 0
#     vals = constants.AGES.get(age)
#     r = range(vals[0], vals[1])
#     for person in people:
#         if person.age in r and person.is_sick:
#             bitacora.add_sick_person(person)
#             result += 1
#     return result


# def get_recovered_by_gender(people, age):
#     result = 0
#     vals = constants.AGES.get(age)
#     r = range(vals[0], vals[1])
#     for person in people:
#         if person.age in r and not person.is_sick and person in bitacora.people_sick:
#             bitacora.add_recovered_person(person)
#             bitacora.remove_sick_person(person)
#             result += 1
#     return result

# def get_sicks_young(people, age):
#     result = 0
#     for person in people:
#         if person.age > 14 and person.age < 60 and person.is_sick:
#             bitacora.add_sick_person(person)
#             result += 1
#     return result

# def get_sicks_kids(people, age):
#     result = 0
#     for person in people:
#         if person.age > 0 and person.age < 15 and person.is_sick:
#             bitacora.add_sick_person(person)
#             result += 1
#     return result

# def get_sicks_adult(people, age):
#     result = 0
#     for person in people:
#         if person.age > 60 and person.age < 125 and person.is_sick:
#             bitacora.add_sick_person(person)
#             result += 1
#     return result


rg = ReportGeneretor()
print(rg.bitacora.people_helthy)