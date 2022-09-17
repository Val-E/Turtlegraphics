from time import sleep

import turtle


t = turtle.Turtle()
t.speed(0)


def draw_pentagram(length, limit):
    if length < limit:
        for i in range(5):
            t.forward(length)
            t.right(144)
        return None
    else:
        for c in ["black", "pink", "red"]:
            t.color(c)
            t.fillcolor(c)
            t.begin_fill()
            draw_pentagram(length/2, limit)
            t.forward(length)
            t.left(60)
            t.end_fill()


draw_pentagram(700, 20)

sleep(100)

