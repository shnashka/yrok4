# -*- coding: utf-8 -*-

import simple_draw as sd
import random as r

x = 1000
y = 1000
sd.resolution = (x, y)
N = 20
snowflakes = []

for _ in range(N):
    snowflakes.append([r.randint(0, x), r.randint(y - 100, y + 250), r.randint(10, 100), True])


def padenie(snowflak2):
    while True:
        sd.clear_screen()
        for snowflake in snowflak2:
            point = sd.get_point(snowflake[0], snowflake[1])
            sd.snowflake(center=point, length=snowflake[2], color=sd.COLOR_WHITE)
            if snowflake[3]:
                if snowflake[1] <= 0:
                    snowflake[1] = 0
                    snowflake[3] = False
                    snowflakes.append([r.randint(0, x), r.randint(y - 100, y + 250), r.randint(10, 100), True])
                else:
                    snowflake[1] -= 15
                    snowflake[0] += r.randint(-15, 15)
        sd.sleep(0.05)
        if sd.user_want_exit():
            break


padenie(snowflakes)
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
