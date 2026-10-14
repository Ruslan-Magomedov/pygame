import pygame as pg
import sys

import random

import settings as settings
import Circle as Circle



pg.init()
pg.display.set_caption(settings.WINDOW_CAPTION)
screen = pg.display.set_mode((settings.WIDTH, settings.HEGHT))
screen.fill(settings.BG_COLOR)

clock = pg.time.Clock()
running = True

# Шары
balls = []
for i in range(1000):
    balls.append(Circle.Circle(
        x=random.randint(settings.MAX_R, settings.WIDTH-settings.MAX_R),
        y=random.randint(settings.MAX_R, settings.HEGHT-settings.MAX_R),
        speed_x=random.randint(settings.MAX_S*-1, settings.MAX_S),
        speed_y=random.randint(settings.MAX_S*-1, settings.MAX_S),
        radius=random.randint(settings.MIN_R, settings.MAX_R),
        color=random.choice(settings.CC)
    ))

# инициализация позиции мышки
mx, my = settings.WIDTH / 2, settings.HEGHT / 2



while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Отслеживание движения мыши
    mx, my = pg.mouse.get_pos()

    screen.fill(settings.BG_COLOR)

    for ball in balls:
        ball.update()
        ball.draw(screen)

        dx = abs(mx - ball.x)
        dy = abs(my - ball.y)
        
        if dx <= 50 and dy <= 50:
            if ball.radius < settings.MAX_RR:
                ball.radius += 10
        else:
            if ball.radius > ball.min_radius:
                ball.radius -= 1

    pg.display.flip()
    clock.tick(settings.FPS)



pg.quit()
sys.exit()
