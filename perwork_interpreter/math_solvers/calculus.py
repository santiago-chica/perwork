from sympy import (
    latex,
    solve,
    diff,
    Eq,
    Add,
    Integral,
    integrate,
    Expr,
    sin,
    cos,
    E,
    Rational
)
from numpy.random import randint, choice
from sympy.abc import x, y
from utils import (
    get_numbers_in_range,
    latexify
)

# - Integrals -

# Basic integrals
def int_basic(config_table:dict):
    term_amount = get_numbers_in_range(
        config_table['minimum_term_count'],
        config_table['maximum_term_count'],
        [0]
    )
    coefficients = get_numbers_in_range(
        config_table['minimum_coefficient'],
        config_table['maximum_coefficient'],
        [0],
        term_amount
    )
    exponents = get_numbers_in_range(
        config_table['minimum_exponent'],
        config_table['maximum_exponent'],
        [],
        term_amount
    )

    if term_amount == 1:
        coefficients = [coefficients]
        exponents = [exponents]

    expression = 0
    for n in range(term_amount):
        coefficient = coefficients[n]
        exponent = exponents[n]

        expression += coefficient * x ** exponent
    
    statement = Integral(expression, x)
    choices = []
    answer = integrate(expression, x)

    return latexify((statement, choices, answer))

# Random function picker
def random_function(config_table:dict, f, n, case=None):
    if not case:
        possible_cases = ['sin', 'cos', 'e', 'exp']
        case = choice(possible_cases)

    match case:
        case 'sin':
            return n * sin(f)
        case 'cos':
            return n * cos(f)
        case 'e':
            return n * E ** f
        case 'exp':
            exponent = get_numbers_in_range(
                config_table['minimum_exponent'],
                config_table['maximum_exponent'],
                [0]
            )
            return n * f ** exponent

# Integration by parts
def int_parts(config_table:dict):
    n = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0]
    )

    possible_cases = ['sin', 'cos', 'e', 'exp']

    v_case, du_case = choice(possible_cases, 2, False)

    v = random_function(config_table, x, 1, v_case)
    du = random_function(config_table, x, 1, du_case)

    u = integrate(du, x)
    dv = diff(v, x)

    statement = Integral(n * u * dv, x)
    choices = []
    answer = integrate(n * u * dv, x)

    return latexify((statement, choices, answer))
# U-substitution
def int_u_sub(config_table:dict):
    num, den, a, b = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        4
    )
    n = Rational(num, den)

    u = a * x + b

    f = random_function(config_table, u, n)

    statement = Integral(f, x)
    choices = []
    answer = integrate(f, x)

    return latexify((statement, choices, answer))
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