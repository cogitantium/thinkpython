def is_triangle(a, b, c):
    """
    Each parameter is the length of one side of the proposed triangle.
    If any sum of two sides are less than the last side, a triangle cannot be formed.
    """
    if a + b < c or a + c < b or b + c < a:
        print('No')
    else:
        print('Yes')


def get_input():
    """
    Takes three inputs and casts them to ints, lastly calling is_triangle
    """
    a = int(input('Input a:\n'))
    b = int(input('Input b:\n'))
    c = int(input('Input c:\n'))

    is_triangle(a, b, c)


get_input()
