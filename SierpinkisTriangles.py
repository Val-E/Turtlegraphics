from time import sleep

import turtle


t = turtle.Turtle()
t.speed(0)


def draw_triangles(length: int, limit: int) -> None:
    if length < limit:
        # picture 1
        for _ in range(4):
           t.forward(length)
           t.left(60)

        # picture 2
        # for _ in range(4):
        #     t.forward(length)
        #     t.right(60)

        # picture 3
        # for _ in range(2):
        #    t.forward(length)
        #    t.right(300)

        # picture 4
        # for _ in range(2):
        #    t.forward(length)
        #    t.left(300)

        # picture 5
        # for _ in range(4):
        #     t.forward(2 * length)
        #     t.left(60)

        # picture 6
        # for _ in range(4):
        #     t.forward(2 * length)
        #     t.right(60)

        return None
    else:
        for c in ["red", "black", "violet"]:
            t.color(c)
            t.fillcolor(c)
            t.begin_fill()
            draw_triangles(length/2, limit)
            t.forward(length)
            t.left(120)
            t.end_fill()


if __name__ == "__main__":
    draw_triangles(700, 5)
    sleep(100)

