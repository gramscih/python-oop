from person import Person
from client import Client
from employee import Employee


def could_you_introduce(obj):
    # With out polymorphism
    # if type(obj) == employee:
    #     obj.introduce_employee()
    # if type(obj) == client:
    #     obj.introuce_client()
    obj.introduce_your_self()

person = Person(123, "Gramsci", "Hermozo")
client = Client(321, "Juanito", "Perez", "JP321")
employee = Employee(543, "Jose", "Santos", "JS543")

could_you_introduce(person)
could_you_introduce(client)
could_you_introduce(employee)