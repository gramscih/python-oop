import pygame

class Ball:
    def __init__(self, x, y , radius, color):
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