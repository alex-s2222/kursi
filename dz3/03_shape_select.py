# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана


def triangle(start_point, angle):
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=100, width=3)
    v1.draw()
    angle += 120
# function starts at zero so 240 degrees
    if angle < 241:
        triangle(start_point=v1.end_point, angle=angle)
    else:
        return


def pentagon(start_point, angle):
    v1 = sd.get_vector(start_point=start_point, angle=angle, width=3)
    v1.draw()
    angle -= 72
    if angle > -145:
        pentagon(start_point=v1.end_point, angle=angle)
    else:
        return


def cube(start_point, angle):
    v1 = sd.get_vector(start_point=start_point, angle=angle, width=3)
    v1.draw()
    angle -= 90
    if angle > -181:
        cube(start_point=v1.end_point, angle=angle)
    else:
        return


def hexagon(start_point, angle):
    v1 = sd.get_vector(start_point=start_point, angle=angle, width=3)
    v1.draw()
    angle -= 60
    if angle > -241:
        hexagon(start_point=v1.end_point, angle=angle)
    else:
        return


# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

global_point = sd.get_point(300,300)

# TODO здесь ваш код
user_input_bool = -10000

while user_input_bool != 5:
    print('Введите с клавитатуры цыфру для вывода фиигурв \n'
          '1 - трегольник \n'
          '2 - пятиугольник \n'
          '3 - шестиугольник \n'
          '4 - четырехугольник \n'
          '5 - выход\n')

    user_input = int(input())

    sd.clear_screen()

    if user_input == 1:
        triangle(start_point=global_point, angle=0)
    elif user_input == 2:
        pentagon(start_point=global_point, angle=144)
    elif user_input == 3:
        hexagon(start_point=global_point, angle=120)
    elif user_input == 4:
        cube(start_point=global_point, angle=90)
    elif user_input == 5:
        user_input_bool = 5

sd.pause()
