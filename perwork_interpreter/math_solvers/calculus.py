from sympy import (
    latex,
    solve,
    diff,
    Eq,
    Add,
)
from numpy.random import randint, choice
from sympy.abc import x, y
from utils import (
    get_numbers_in_range
)

# - Derivatives -
def calculus_deriv_power(question:dict):

    config_table = question['configuration']
    exponent = get_numbers_in_range(
        config_table['minimum_exponent'],
        config_table['maximum_exponent'],
        [0],
        1
    )[0]

    coefficient = get_numbers_in_range(
        config_table['minimum_coefficient'],
        config_table['maximum_coefficient'],
        [0],
        1
    )[0]

    statement = coefficient * x ** exponent
    choices = [[]]
    answer = diff(statement, x)

    return (statement, choices, answer)