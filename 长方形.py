from time import *
from turtle import *
hideturtle()
tracer(0)
color("blue")


def draw_rectangle(x, y, a, b):
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    for _ in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)
    end_fill()
    penup()
    update()


draw_rectangle(0, 0, 100, 70)
draw_rectangle(70, 80, 60, 40)
draw_rectangle(150, 60, 140, 130)
draw_rectangle(-100, 100, 100, 90)
draw_rectangle(-100, -180, 70, 50)
draw_rectangle(-200, -180, 70, 50)
sleep(3)
