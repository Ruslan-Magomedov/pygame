import pygame as pg

import settings as settings



class Circle:
    def __init__(self, x: int, y: int, speed_x: float, speed_y: float, color: str, radius: int):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
        self.radius = radius
        self.min_radius = self.radius



    def update(self):
        # движение
        self.x += self.speed_x
        self.y += self.speed_y

        # границы окна
        if self.x-self.radius <= 0 or self.x+self.radius >= settings.WIDTH:
            self.speed_x *= -1
        if self.y-self.radius <= 0 or self.y+self.radius >= settings.HEGHT:
            self.speed_y *= -1



    def draw(self, window):
        # отрисовка объекта
        pg.draw.circle(window, self.color, (self.x, self.y), self.radius)
