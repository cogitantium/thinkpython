def check_fermat(a, b, c, n):
    """
    Fermat's Last Theorem states that there are now positive integers a,b, and c such that
    a**n + b**n = c**n for any values of n greater than 2.
    :param a: must be positive
    :param b: must be positive
    :param c: must be positive
    :param n: must be greater than 2
    """
    if n < 3:
        print("n is smaller than 3, cannot check Fermat's Last Theorem")
    elif a <= 0 or b <= 0 or c <= 0:
        print("a, b, and c must be positive integers, cannot check Fermat's Last Theorem")
    elif c**n == a**n + b**n:
        print('Dang, he was wrong!')
    else:
        print("No, that doesn't work")


def get_input():
    """
    Takes four inputs and casts them to ints, lastly calling check_fermat
    """
    a = int(input('Input a:\n'))
    b = int(input('Input b:\n'))
    c = int(input('Input c:\n'))
    n = int(input('Input n:\n'))
    check_fermat(a, b, c, n)


get_input()
