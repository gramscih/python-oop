from person import Person

class Employee(Person):
    def __init__(self, ci, name, lastname, id):
        super().__init__(ci, name, lastname)
        self.__id = id

    def introduce_your_self(self):
        print(f"Hello, I am an employee with id {self.__id}")