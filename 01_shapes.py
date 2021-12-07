# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (700, 700)


def triangle(point, angle, side_len):
    vector_1 = sd.get_vector(start_point=point, angle=angle, length=side_len, width=1)
    vector_1.draw()
    vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=angle + 120, length=side_len, width=1)
    vector_2.draw()
    vector_3 = sd.get_vector(start_point=vector_2.end_point, angle=angle + 240, length=side_len, width=1)
    vector_3.draw()


point_0 = sd.get_point(101, 101)
triangle(point_0, 0, 40)


def square(point, angle, side_len):
    vector_1 = sd.get_vector(start_point=point, angle=angle, length=side_len, width=1)
    vector_1.draw()
    vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=angle + 90, length=side_len, width=1)
    vector_2.draw()
    vector_3 = sd.get_vector(start_point=vector_2.end_point, angle=angle + 180, length=side_len, width=1)
    vector_3.draw()
    vector_4 = sd.get_vector(start_point=vector_3.end_point, angle=angle + 270, length=side_len, width=1)
    vector_4.draw()


point_0 = sd.get_point(100, 200)
square(point_0, 0, 50)


def pentagon(point, angle, side_len):
    vector_1 = sd.get_vector(start_point=point, angle=angle, length=side_len, width=1)
    vector_1.draw()
    vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=angle + 72 * 1, length=side_len, width=1)
    vector_2.draw()
    vector_3 = sd.get_vector(start_point=vector_2.end_point, angle=angle + 72 * 2, length=side_len, width=1)
    vector_3.draw()
    vector_4 = sd.get_vector(start_point=vector_3.end_point, angle=angle + 72 * 3, length=side_len, width=1)
    vector_4.draw()
    vector_5 = sd.get_vector(start_point=vector_4.end_point, angle=angle + 72 * 4, length=side_len, width=1)
    vector_5.draw()


point_0 = sd.get_point(100, 300)
pentagon(point_0, 0, 60)


def octagon(point, angle, side_len):
    vector_1 = sd.get_vector(start_point=point, angle=angle, length=side_len, width=1)
    vector_1.draw()
    vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=angle + 60 * 1, length=side_len, width=1)
    vector_2.draw()
    vector_3 = sd.get_vector(start_point=vector_2.end_point, angle=angle + 60 * 2, length=side_len, width=1)
    vector_3.draw()
    vector_4 = sd.get_vector(start_point=vector_3.end_point, angle=angle + 60 * 3, length=side_len, width=1)
    vector_4.draw()
    vector_5 = sd.get_vector(start_point=vector_4.end_point, angle=angle + 60 * 4, length=side_len, width=1)
    vector_5.draw()
    vector_6 = sd.get_vector(start_point=vector_5.end_point, angle=angle + 60 * 5, length=side_len, width=1)
    vector_6.draw()


point_0 = sd.get_point(100, 400)
octagon(point_0, 0, 70)


def figure(start, angle, length):
    side = sd.get_vector(start_point=start, angle=angle, length=length, width=1)
    side.draw()
    return side.end_point


def triangle_2(_point, _angle, _len):
    next_point = _point
    for i in range(3):
        next_point = figure(start=next_point, angle=_angle + 360 / 3 * i, length=_len)


point_0 = sd.get_point(400, 100)
triangle_2(point_0, 0, 80)


def square_2(_point, _angle, _len):
    next_point = _point
    for i in range(4):
        next_point = figure(start=next_point, angle=_angle + 360 / 4 * i, length=_len)


point_0 = sd.get_point(400, 200)
square_2(point_0, 0, 80)


def pentagon_2(_point, _angle, _len):
    next_point = _point
    for i in range(5):
        next_point = figure(start=next_point, angle=_angle + 360 / 5 * i, length=_len)


point_0 = sd.get_point(400, 300)
pentagon_2(point_0, 0, 80)


def octagon_2(_point, _angle, _len):
    next_point = _point
    for i in range(6):
        next_point = figure(start=next_point, angle=_angle + 360 / 6 * i, length=_len)


point_0 = sd.get_point(400, 500)
octagon_2(point_0, 0, 80)

sd.pause()
