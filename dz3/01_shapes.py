# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

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

# TODO здесь ваш код

point_triangle = sd.get_point(90, 450)
point_pentagon = sd.get_point(130, 150)
point_cube = sd.get_point(390, 440)
point_hexagon = sd.get_point(400, 150)


triangle(start_point=point_triangle, angle=0)
pentagon(start_point=point_pentagon, angle=144)
cube(start_point=point_cube, angle=90)
hexagon(start_point=point_hexagon, angle=120)

# v1 = sd.get_vector(start_point=point_hexagon, angle=120, width=3)
# v1.draw()
# v1 = sd. get_vector(start_point=v1.end_point, angle=60, width=3)
# v1.draw()
# v1 = sd.get_vector(start_point=v1.end_point, angle=0, width=3)
# v1.draw()
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
