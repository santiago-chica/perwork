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
    get_numbers_in_range,
    latexify
)

# - Integrals -

# TODO
# Basic integrals
# Integration by parts
# U-substitution
# Trigonometric substitution
# Summary

# - Discontinuities -

# TODO
# Rational functions

# - Derivatives -

# TODO
# Power rule
def deriv_power(config_table:dict):
    exponent = get_numbers_in_range(
        config_table['minimum_exponent'],
        config_table['maximum_exponent'],
        [0]
    )

    coefficient = get_numbers_in_range(
        config_table['minimum_coefficient'],
        config_table['maximum_coefficient'],
        [0]
    )

    statement = coefficient * x ** exponent
    choices = []
    answer = diff(statement, x)

    return latexify((statement, choices, answer))
# Product rule
# Quotient rule
# Chain rule
# Summary

# - Summary -
# Calculus summary