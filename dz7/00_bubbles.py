# -*- coding: utf-8 -*-
import random

import simple_draw as sd

point = sd.get_point(300, 300)

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1100, 100):
        point = sd.get_point(x, y)
        #bubble(point=point, step=1)

def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(5):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point=point, step=step)


sd.pause()
