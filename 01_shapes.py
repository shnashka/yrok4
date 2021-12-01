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
triangle(point_0, 0, 100)


def square(point, angle, side_len):
    vector_1 = sd.get_vector(start_point=point, angle=angle, length=side_len, width=1)
    vector_1.draw()
    vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=angle + 90, length=side_len, width=1)
    vector_2.draw()
    vector_3 = sd.get_vector(start_point=vector_2.end_point, angle=angle + 180, length=side_len, width=1)
    vector_3.draw()
    vector_4 = sd.get_vector(start_point=vector_3.end_point, angle=angle + 270, length=side_len, width=1)
    vector_4.draw()


point_0 = sd.get_point(200, 200)
square(point_0, 0, 50)

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
