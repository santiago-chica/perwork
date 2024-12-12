from sympy import (symbols,
                   Add,
                   latex,
                   solve,
                   Symbol,
                   StrPrinter,
                   diff)
from sympy.abc import x
from numpy.random import choice


if __name__ == '__main__':



    f = 3 * x ** 4
    dev = diff(f, x)

    statement = latex(dev, mode='equation*', order='none')

    print(statement)