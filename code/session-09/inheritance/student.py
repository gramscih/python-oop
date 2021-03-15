from person import Person

class Student(Person):
    def __init__(self, name, lname, grade):
        # Person.__init__(self, name, lname)
        # super(Student, self).__init__(name, lname)
        super().__init__(name, lname)
        self.grade = grade

s = Student("Jaime", "Jaimito", "basic")
print(s.name)