import pygame
import constants
import physics

class Ball:
    def __init__(self, x, y , radius, color = constants.COLOR_WHITE):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__color = color

    def draw(self, win):
        pygame.draw.circle(win, (0,0,0), (self.__x, self.__y), self.__radius)
        pygame.draw.circle(win, self.__color, (self.__x, self.__y), self.__radius -1)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    
    def set_x(self, new_x):
        self.__x = new_x
    
    def set_y(self, new_y):
        self.__y = new_y

    def get_radius(self):
        return self.__radius

    @staticmethod
    def ball_path(start_x, start_y, velocity, angle, time):
        velocity_x = physics.calculate_x_velocity(velocity, angle)
        velocity_y = physics.calculate_y_velocity(velocity, angle)

        dist_x = physics.calcuate_height(velocity_x, time)
        dist_y = physics.calculate_distance(velocity_y, time)

        new_x = round(dist_x + start_x)
        new_y = round(start_y - dist_y)

        return (new_x, new_y)

