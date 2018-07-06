# exercise 3.1


def right_justify(s):
    bound = 70
    while len(s) < bound:
        s = ' ' + s
    return s


print(right_justify("stuff"))


def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')


do_twice(print_spam)


# exercise 3.3


def print_grid(ncol, nrow):
    delim = 4
    col = '+----'
    col_end = '+'
    row = '|    '
    row_end = '|'

    for num in range(nrow):
        # print column header
        for x in range(ncol):
            print(end=col)
        print(col_end)

        # print row deliminators
        for y in range(delim):
            for x in range(ncol):
                print(end=row)
            print(row_end)

    # print column footer
    for num in range(ncol):
        print(end=col)
    print(col_end)


print_grid(6, 3)
