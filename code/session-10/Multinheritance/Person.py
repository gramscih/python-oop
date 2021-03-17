class Person(object):
    def __init__(self, age):
        self.name = "Gramsci"
        self.age = age

    def get_name(self):
        return self.name

class Student(object):
    def __init__(self, student_id):
        self.name = "Jaime"
        self.student_id = student_id

    def get_name(self):
        return self.name

class Resident(Person, Student):
    def __init__(self, name, age, student_id):
        Person.__init__(self, age)
        Student.__init__(self, student_id)


r = Resident("name", 123, 4321)
print(r.get_name())