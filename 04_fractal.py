# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 1000)


# def draw_branches(point, angle, length):
#     vetka1 = sd.get_vector(start_point=point, angle=angle + 30, length=length, width=3)
#     vetka2 = sd.get_vector(start_point=point, angle=angle - 30, length=length, width=3)
#     vetka1.draw(sd.COLOR_RED)
#     vetka2.draw(sd.COLOR_DARK_YELLOW)
#     return vetka1.end_point


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви
def draw_branches(point, angle, length):
    if length < 11:
        return
    else:
        # angle_delta = 30
        length_delta = .75
        angle_l = angle - 30
        angle_r = angle + 30
        vetka11 = sd.get_vector(start_point=point, angle=angle_l, length=length, width=1)
        vetka22 = sd.get_vector(start_point=point, angle=angle_r, length=length, width=1)
        vetka11.draw()
        vetka22.draw()

        next_point = vetka11.end_point
        next_length = length * length_delta
        next_angle = angle_l - 30
        draw_branches(point=next_point, angle=next_angle, length=next_length)
        next_angle = angle_l + 30
        draw_branches(point=next_point, angle=next_angle, length=next_length)

        next_point = vetka22.end_point
        next_length = length * length_delta
        next_angle = angle_r - 30
        draw_branches(point=next_point, angle=next_angle, length=next_length)
        next_angle = angle_r + 30
        draw_branches(point=next_point, angle=next_angle, length=next_length)


root_point = sd.get_point(600, 303)
draw_branches(point=root_point, angle=180
              , length=100)

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
