import turtle

bob = turtle.Turtle()


def fractal(obj, length, n):
    """
    Draws a fractal tree with given length and given number of branches
    :param obj: the turtle used to draw
    :param length: the length of trunk
    :param n: the number of branches
    :return:
    """
    if n == 0:
        return
    angle = 50
    obj.fd(length*n)
    obj.lt(angle)
    draw(obj, length, n-1)
    obj.rt(2*angle)
    draw(obj, length, n-1)
    obj.lt(angle)
    obj.bk(length*n)


def koch(obj, length):
    """
    Draws a Koch-curve with given turtle object and given length.
    :param obj: the turtle used to draw
    :param length: the length of the Koch curve
    :return: void
    """
    if length < 3:
        obj.fd(length)
    else:
        koch(obj, length/3)
    obj.lt(60)

    if length < 3:
        obj.fd(length)
    else:
        koch(obj, length/3)
    obj.rt(120)

    if length < 3:
        obj.fd(length)
    else:
        koch(obj, length/3)
    obj.lt(60)

    if length < 3:
        obj.fd(length)
    else:
        koch(obj, length/3)


def snowflake(obj, length):
    """
    Draws a snowflake by drawing three Koch curves in a pattern of a equilateral triangle,
    resulting in a hexagonal snowflake.
    :param obj: the turtle used to draw
    :param length: the length of each Koch curve
    :return:
    """
    for i in range(3):
        koch(obj, length)
        obj.rt(120)


snowflake(bob, 100)

turtle.mainloop()
