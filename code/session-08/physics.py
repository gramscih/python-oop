import math

# class Physics:
#     """This class would help us to calculate the physics problems
#     in this case would be used for parabolic movement
#     """
    
    # def __init__(self):
    #     """Physics contructor
    #     """
        # self.__g = 9.8

GRAVITY = 9.8

def calculate_distance(initial_velocity, angle):
    """This function should calcuate the distance 
    that take the object

    Args:
        initial_velocity (float): This paramether is the initial velocity of the object
        angle (float): This paramether is the angle of that the object take off
    """
    validate_value(initial_velocity)
    validate_value(angle)

    dis = (initial_velocity * math.sin(2*angle)) / GRAVITY
    return dis


def calculate_time(initial_velocity, angle):
    """This function should calculate the time that the object
    would be in the air

    Args:
        initial_velocity (float): This paramether is the initial velocity of the object
        angle (float): This paramether is the angle of that the object take off
    """
    validate_value(initial_velocity)
    validate_value(angle)

    time = 2 * initial_velocity * math.sin(angle)
    return time
    

def calculate_x_velocity(initial_velocity, angle):
    """[summary]

    Args:
        initial_velocity (float): This paramether is the initial velocity of the object
        angle (float): This paramether is the angle of that the object take off
    """
    validate_value(initial_velocity)
    validate_value(angle)

    v_x = initial_velocity * math.cos(angle)
    return v_x

def calculate_y_velocity(self, initial_velocity, angle):
    """[summary]

    Args:
        initial_velocity (float): This paramether is the initial velocity of the object
        angle (float): This paramether is the angle of that the object take off
    """
    validate_value(initial_velocity)
    validate_value(angle)

    v_y = initial_velocity * math.sin(angle)
    return v_y


def calcuate_height(initial_velocity, angle):
    """[summary]

    Args:
        initial_velocity (float): This paramether is the initial velocity of the object
        angle (float): This paramether is the angle of that the object take off
    """
    validate_value(initial_velocity)
    validate_value(angle)
    
    # ((Vo * sin <angle>)^2)/ 2*g
    height = ((initial_velocity * math.sin(angle))**2)/(2 * 9.8)
    return height


def validate_value(value):
    """This function validate if values is an integer if is str trow exception

    Args:
        value (object): Values to validate

    Raises:
        ValueError: [description]
    """
    if type(value) == str:
        raise ValueError("You entered an string and float or int is expected")


# p = Physics()
# p.calculate_distance("30", 45)
# print(p.calculate_distance(30, 45))
# print(p.calculate_time(30, 45))
# print(p.calculate_x_velocity(30, 45))
# print(p.calculate_y_velocity(30, 45))
# print(p.calcuate_height(30, 45))

# print(Physics.calcuate_height(35, 40))