# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 800)


def figure(start, angle, length, ):
    side = sd.get_vector(start_point=start, angle=angle, length=length, width=1)
    side.draw()

    return side.end_point


def triangle_2(_point, _angle, _len, ):
    next_point = _point
    for i in range(3):
        next_point = figure(start=next_point, angle=_angle + 360 / 3 * i, length=_len)


def square_2(_point, _angle, _len, ):
    next_point = _point
    for i in range(4):
        next_point = figure(start=next_point, angle=_angle + 360 / 4 * i, length=_len, )


def pentagon_2(_point, _angle, _len, ):
    next_point = _point
    for i in range(5):
        next_point = figure(start=next_point, angle=_angle + 360 / 5 * i, length=_len, )


def octagon_2(_point, _angle, _len, _color):
    next_point = _point
    for i in range(6):
        next_point = figure(start=next_point, angle=_angle + 360 / 6 * i, length=_len,)


namber = {
    1: 'треугольник',
    2: "четырех угольник",
    3: "пятиугольник",
    4: "шестиугольник"}

print("Выбери цвет!")
for i, item in namber.items():
    print(f"{i}. {item}")

color_vibor = int(input())
print(color_vibor)
if not (1 <= color_vibor <= 4):
    print("Fuck you! Нужно выбрать 1-4")
else:
    print(f"Ты выбрал {namber[color_vibor]}")
    if color_vibor == 1:
        point_0 = sd.get_point(400, 400)
        triangle_2(point_0, 0, 80,)
    if color_vibor == 2:
        point_0 = sd.get_point(400, 400)
        square_2(point_0, 0, 80,)
    if color_vibor == 3:
        point_0 = sd.get_point(400, 400)
        pentagon_2(point_0, 0, 80,)
    if color_vibor == 4:
        point_0 = sd.get_point(400, 400)
        octagon_2(point_0, 0, 80,)
sd.pause()
