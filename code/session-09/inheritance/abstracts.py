from abc import ABC

class Shape(ABC):
    def calculate_area(self):
        raise NotImplementedError


class Square(Shape):
    def calculate_area(self):
        return 45


square = Square()
print(square.calculate_area())