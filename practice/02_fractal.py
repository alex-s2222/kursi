# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 500)

# нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100

point_0 = sd.get_point(300, 5)



# сделать функцию рисования ветки из заданной точки,
# заданной длины, с заданным наклоном
# def branch(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle= angle, length=length, width=3)
#     v1.draw()
#     return v1.end_point

# angle_0 =  90
# length_0 = 200
#
# next_point = branch(point=point_0, angle=angle_0, length=length_0)
# next_angle = angle_0 - 30
# next_length = length_0 * 0.75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)
# next_angle -= 30
# next_length *= 0.75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)

# написать цикл рисования ветвей с постоянным уменьшением длины на 25% и отклонением на 30 градусов

# angle_0 = 90
# length_0 = 200
#
# next_angle = angle_0
# next_length = length_0
# next_point = point_0
#
# while next_length > 1:
#     next_point = branch(point=next_point, angle=next_angle, length=next_length)
#     next_angle -= 30
#     next_length *= 0.75


# сделать функцию branch рекурсивной
def branch(point, angle, length):
    if length < 1:
       return
    v1 = sd   .get_vector(start_point=point, angle= angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - 60
    next_length = length * 0.75
    branch(point=next_point, angle=next_angle, length=next_length)


angle_0 = 90
length_0 = 200

branch(point=point_0, angle=angle_0, length=length_0)

sd.pause()

