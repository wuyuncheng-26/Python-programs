from time import *
from turtle import *
speed(8)
color("blue")
pensize(5)
a = int(input("请输入边数："))
b = int(input("请输入边长："))
for _ in range(a):
    forward(b)
    left(360 / a)
sleep(3)