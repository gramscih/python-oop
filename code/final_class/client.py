from person import Person

class Client(Person):
    def __init__(self, ci, name, lastname, count_number):
        super().__init__(ci, name, lastname)
        self.__count = count_number

    def introduce_your_self(self):
        print(f"Hello, I am an client with id {self.__count}")