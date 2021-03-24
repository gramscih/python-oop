import unittest

from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        print("setUP")
        self.emp_1 = Employee("Gramsci", "Hermozo", 2500)
        self.emp_2 = Employee("Pepito", "Perez", 4000)

    def tearDown(self):
        print("tearDown")

    def test_email(self):
        # self.emp_1 = Employee("Gramsci", "Hermozo", 2500)
        # self.emp_2 = Employee("Pepito", "Perez", 4000)
        print("test_email")

        self.assertEqual(self.emp_1.email, "Gramsci.Hermozo@email.com")
        self.assertEqual(self.emp_2.email, "Pepito.Perez@email.com")

        self.emp_1.first = "John"        
        self.emp_2.first = "Pedro"        

        self.assertEqual(self.emp_1.email, "John.Hermozo@email.com")
        self.assertEqual(self.emp_2.email, "Pedro.Perez@email.com")


    def test_fullname(self):
        # self.emp_1 = Employee("Gramsci", "Hermozo", 2500)
        # self.emp_2 = Employee("Pepito", "Perez", 4000)

        print("test_fullname")

        self.assertEqual(self.emp_1.fullname, "Gramsci Hermozo")
        self.assertEqual(self.emp_2.fullname, "Pepito Perez")

        self.emp_1.first = "John"        
        self.emp_2.first = "Pedro"        

        self.assertEqual(self.emp_1.fullname, "John Hermozo")
        self.assertEqual(self.emp_2.fullname, "Pedro Perez")

    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            sch = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with("http://company.com/Hermozo/May")
            self.assertEqual(sch, 'Success')

if __name__ == "__main__":
    unittest.main()





    complex_1 = ComplexNumber(2, 4)
    complex_2 = ComplexNumber(1, 2)

    result = complex_1 + complex_2

    assertEqual(result, "3 + 6i")
    print(result) # => 3 + 6i => 6i + 3