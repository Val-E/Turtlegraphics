from time import sleep

import turtle


t = turtle.Turtle()
t.speed(0)


def draw_fractal(length, limit):
    if length < limit:
        for _ in range(3):
            t.forward(length)
            t.left(60)
        return None
    else:
        for c in ["red", "black", "violet"]:
            t.color(c)
            t.fillcolor(c)
            t.begin_fill()
            draw_fractal(length/2, limit)
            t.forward(length)
            t.left(120)
            t.end_fill()


draw_fractal(1000, 1)
sleep(100)

