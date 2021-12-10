# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (700, 700)
colors = {
    1: sd.COLOR_RED,
    2: sd.COLOR_ORANGE,
    3: sd.COLOR_YELLOW,
    4: sd.COLOR_GREEN,
    5: sd.COLOR_BLACK,
    6: sd.COLOR_BLUE,
    7: sd.COLOR_WHITE
}
colors_name = {
    1: 'Индеец',
    2: 'Трамп',
    3: 'КИТАЕЦ',
    4: 'НЛО',
    5: 'Афро-американец',
    6: 'Толерантный',
    7: 'Белый'
}


def figure(start, angle, length, color):
    side = sd.get_vector(start_point=start, angle=angle, length=length, width=1)
    side.draw(color=color)

    return side.end_point


def triangle_2(_point, _angle, _len, _color):
    next_point = _point
    for i in range(3):
        next_point = figure(start=next_point, angle=_angle + 360 / 3 * i, length=_len, color=_color)


def square_2(_point, _angle, _len, _color):
    next_point = _point
    for i in range(4):
        next_point = figure(start=next_point, angle=_angle + 360 / 4 * i, length=_len, color=_color)


def pentagon_2(_point, _angle, _len, _color):
    next_point = _point
    for i in range(5):
        next_point = figure(start=next_point, angle=_angle + 360 / 5 * i, length=_len, color=_color)


# point_0 = sd.get_point(400, 300)
# pentagon_2(point_0, 0, 80)


def octagon_2(_point, _angle, _len, _color):
    next_point = _point
    for i in range(6):
        next_point = figure(start=next_point, angle=_angle + 360 / 6 * i, length=_len, color=_color)


# point_0 = sd.get_point(400, 500)
# octagon_2(point_0, 0, 80)

print("Выбери цвет!")
for i, item in colors_name.items():
    print(f"{i}. {item}")

color_vibor = int(input())
print(color_vibor)

if (1 <= color_vibor <= 7):
    _color = colors[color_vibor]
    print(f"Ты выбрал {colors_name[color_vibor]} - {colors[color_vibor]}")
    if (color_vibor == 7):
        print("маленький расист")

    else:
        print("попросил оценить от 1 до 7 чел пишет 12")

point_0 = sd.get_point(400, 100)
triangle_2(point_0, 0, 80, _color)
point_0 = sd.get_point(400, 500)
octagon_2(point_0, 0, 80, _color)
point_0 = sd.get_point(400, 200)
square_2(point_0, 0, 80, _color)
point_0 = sd.get_point(400, 300)
pentagon_2(point_0, 0, 80, _color)
sd.pause()
