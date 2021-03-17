# class Shape(object):
#     def calculate_area(self):
#         pass

# class Square(Shape):
#     def __init__(self):
#         self.side_lenght = 2

#     def calculate_area(self):
#         return self.side_lenght ** 2

# class Triangle(Shape):
#     def __init__(self):
#         self.base_lenght = 4
#         self.height = 3
    
#     def calculate_area(self):
#         return 0.5 * self.base_lenght * self.height

# def get_are(input_obj):
#     print(input_obj.calculate_area())

# s = Shape()
# sq = Square()
# t = Triangle()

# get_are(s)
# get_are(sq)
# get_are(t)


class Square(object):
    def __init__(self):
        self.side_lenght = 2

    def calculate_square_area(self):
        return self.side_lenght ** 2

class Triangle(object):
    def __init__(self):
        self.base_lenght = 4
        self.height = 3
    
    def calculate_triangle_area(self):
        return 0.5 * self.base_lenght * self.height

def get_are(input_obj):
    area = None
    if type(input_obj) == Square:
        area = input_obj.calculate_square_area()
    if type(input_obj) == Triangle:
        area = input_obj.calculate_triangle_area()
    print(area)

sq = Square()
t = Triangle()

get_are(sq)
get_are(t)

print(len("123"))
print(len([1,2,3]))
print(len({'a':"a"}))
len(123)