class Student:
    university = "Jala"
    
    def __init__(self, name: str, lastname: str, year: int):
        self.__name = name
        self.__lastname = lastname
        self.__year = year

    def presentation(self):
        print("My name is {}".format(self.__name))
        print("My lastname is {}".format(self.__lastname))
        print("I have {} years old".format(self.__year))
        

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        print("Setting... Name")
        self.__name = new_name
    
    # name = property(get_name, set_name)

    
    
# Student.university = "UMSS"
# student_1 = Student("Gramsci", "Hermozo", 31)
# print("Hello from get function - {} is my name".format(student_1.name))
# student_1.name = "GHC"
# print("Hello after set function - {} is my name".format(student_1.name))

# student_1.presentation()
# student_2 = Student("Andres", "Santos", "23")
# student_2.presentation()
# print(student_2.university)
# student_3 = Student("Jhon", "Wheek", 54)
# student_3.presentation()
# print(student_3.university)

# print("[+] Enter your name")
name = input("[+] Enter your name: ")
print("Entered: {} Name".format(name))
lastname = input("[+] Enter your latname: ")
print("Entered: {} lastname".format(lastname))
year = input("[+] How years old?: ")
print("Entered {} years old".format(year))
# print("years {} type".format(type(year)))
student = Student(name, lastname, year)
student.presentation()