from sympy import (
    Eq,
    latex,
    solve
)
from numpy.random import randint, choice
from sympy.abc import x, y

def integerOneStepEquation(question:dict):

    config_table = question['configuration']

    minimum = config_table['minimum_integer']
    maximum = config_table['maximum_integer']

    domain = [i for i in range(minimum, maximum + 1) if i not in [1, 0]]
    
    l, r = choice(domain, size=2, replace=False)

    equation = Eq(l * x, r)

    statement = latex(equation, mode='equation*')
    choices = [[]]
    answer = latex(solve(equation, x)[0], mode='equation*')

    return (statement, choices, answer)