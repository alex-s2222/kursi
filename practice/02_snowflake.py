# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# познакомится с параметрами библиотечной функции рисования снежинки sd.snowflake()
point_0 = sd.get_point(100, 500)

# sd.snowflake(center=point_0, length=200)

# sd.snowflake(center=point_0, length=200, factor_a=0.5)
y = 500
x = 100

y2 = 450
x2 = 150
while True:
    sd.clear_screen()
    point_0 = sd.get_point(x, y)
    sd.snowflake(center=point_0, length=50)
    y -= 30

    if y < 0:
        break
    x += 50

    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=50)
    y2 -= 10

    if y < 50:
        break
    x2 += 50

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# реализовать падение одной снежинки

# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()
