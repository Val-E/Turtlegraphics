from time import sleep

import turtle


t = turtle.Turtle()
t.speed(0)


def draw_pentagram(length, limit):
    if length < limit:
        for _ in range(5):
            t.forward(length)
            t.left(144)
        return None
    else:
        for c in ["black", "pink", "violet", "red", "blue"]:
            t.color(c)
            t.fillcolor(c)
            t.begin_fill()
            draw_pentagram(length/3, limit)
            t.end_fill()
            t.forward(length)
            t.left(144)


draw_pentagram(700, 20)

sleep(100)

