import math
import turtle

bob = turtle.Turtle()


def draw_square(obj, length):
    for i in range(4):
        obj.fd(length)
        obj.lt(90)


# draw_square(bob, 350)


def polygon(obj, n, length):
    angle = 360 / n
    for i in range(n):
        obj.fd(length)
        obj.lt(angle)


# polygon(bob, 8, 100)


def circle(obj, radius):
    stride = 2 * math.pi * radius / 360.0
    for num in range(360):
        obj.fd(stride)
        obj.lt(1)


# circle(bob, 150)


def arc(obj, radius, arc):
    stride = 2 * math.pi * radius / 360.0
    angle = 0
    while angle <= arc:
        obj.fd(stride)
        obj.lt(1)
        angle += 1


# arc(bob, 150, 270)

def petal(obj, radius, angle):
    for i in range(2):
        arc(obj, radius, angle)
        obj.lt(180-angle)


def flower(obj, n, radius, angle):
    for i in range(n):
        petal(obj, radius, angle)
        obj.lt(360.0/n)


flower(bob, 7, 60.0, 60.0)

turtle.mainloop()
