import pygame
import math
import physics
import constants

from ball import Ball

WIDTH = 1200
HEIGHT= 500

class MainWindow:
    def __init__(self):
        self.__win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__ball = Ball(300, 494, 5)
        self.__x = 0
        self.__y = 0
        self.__time = 0
        self.__velocity = 0
        self.__angle = 0
        self.__shoot = False

    def set_angle(self, mouse_pos):
        position_x = self.__ball.get_x()
        position_y = self.__ball.get_y()

        try:
            self.__angle = math.atan((position_y - mouse_pos[1]) / (position_x - mouse_pos[0]))
        except:
            self.__angle = math.pi / 2

        if mouse_pos[1] < position_y and mouse_pos[0] > position_x:
            # abs() function returns the absolute value. That mean always a positive value
            self.__angle = abs(self.__angle)
        elif mouse_pos[1] < position_y and mouse_pos[0] < position_x:
            self.__angle = math.pi - self.__angle
        elif mouse_pos[1] > position_y and mouse_pos[0] < position_x:
            self.__angle = math.pi + abs(self.__angle)
        elif mouse_pos[1] > position_y and mouse_pos[0] > position_x:
            self.__angle = (math.pi * 2) - self.__angle


    def run_win(self):
        run = True
        while run:
            if self.__shoot:
                if self.__ball.get_y() < HEIGHT - self.__ball.get_radius():
                    self.__time += 0.05
                    # pos = (x, y)
                    pos = Ball.ball_path(self.__x, self.__y, self.__velocity, self.__angle, self.__time)
                    self.__ball.set_x(pos[0])
                    self.__ball.set_y(pos[1])
                else:
                    self.__shoot = False
                    self.__ball.set_y(HEIGHT - self.__ball.get_radius())

            mouse_pos = pygame.mouse.get_pos()
            line = [(self.__ball.get_x(), self.__ball.get_y()), mouse_pos]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__shoot == False:
                        self.__shoot = True
                        self.__x = self.__ball.get_x()
                        self.__y = self.__ball.get_y()
                        self.__time = 0
                        self.__velocity = physics.calcuate_velocity(line)
                        self.set_angle(mouse_pos)

            self.__win.fill(constants.BACKGROUND)
            self.__ball.draw(self.__win)
            pygame.draw.line(self.__win, constants.COLOR_WHITE, line[0], line[1])
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    main = MainWindow()
    main.run_win()