# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом


def triangle(start_point, angle):
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=100, width=3)
    v1.draw(color=color)
    angle += 120
# function starts at zero so 240 degrees
    if angle < 241:
        triangle(start_point=v1.end_point, angle=angle)
    else:
        return


def pentagon(start_point, angle):
    v1 = sd.get_vector(start_point=start_point, angle=angle, width=3)
    v1.draw(color=color)
    angle -= 72
    if angle > -145:
        pentagon(start_point=v1.end_point, angle=angle)
    else:
        return


def cube(start_point, angle):
    v1 = sd.get_vector(start_point=start_point, angle=angle, width=3)
    v1.draw(color=color)
    angle -= 90
    if angle > -181:
        cube(start_point=v1.end_point, angle=angle)
    else:
        return


def hexagon(start_point, angle):
    v1 = sd.get_vector(start_point=start_point, angle=angle, width=3)
    v1.draw(color=color)
    angle -= 60
    if angle > -241:
        hexagon(start_point=v1.end_point, angle=angle)
    else:
        return


# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код


point_triangle = sd.get_point(90, 450)
point_pentagon = sd.get_point(130, 150)
point_cube = sd.get_point(390, 440)
point_hexagon = sd.get_point(400, 150)

input_color = int(input('1 - отранжевый\n'
                        '2 - красный\n'
                        '3 - желтый\n'))

while input_color == 5:
    if input_color == 1:
        color = sd.COLOR_ORANGE
    elif input_color == 2:
        color = sd.COLOR_RED
    elif input_color == 3:
        color = sd.COLOR_YELLOW


triangle(start_point=point_triangle, angle=0)
pentagon(start_point=point_pentagon, angle=144)
cube(start_point=point_cube, angle=90)
hexagon(start_point=point_hexagon, angle=120)


sd.pause()