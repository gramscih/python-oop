from bitacora import Bitacora

bitacora = Bitacora()

def get_sicks(people):
    result = 0
    for person in people:
        if person.is_sick:
            bitacora.add_sick_person(person)
            result += 1
    return result


def get_recover(people):
    result = 0
    for person in people:
        if not person.is_sick and person in bitacora.people_sick:
            bitacora.add_recovered_person(person)
            # bitacora.remove_sick_person(person)
            result += 1
    return result