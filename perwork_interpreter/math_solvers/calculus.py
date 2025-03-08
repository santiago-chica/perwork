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
    Rational,
    real_roots
)
from numpy.random import randint, choice
from sympy.abc import x, y
from utils import (
    get_numbers_in_range,
    latexify
)

# - Integrals -

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
def get_polynomial(config_table):
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
    return expression
def get_two_different_functions(config_table):
    possible_cases = ['sin', 'cos', 'e', 'exp']

    f_case, g_case = choice(possible_cases, 2, False)

    f = random_function(config_table, x, 1, f_case)
    g = random_function(config_table, x, 1, g_case)
    return f, g

# Basic integrals
def int_basic(config_table:dict):
    expression = get_polynomial(config_table)
    
    statement = Integral(expression, x)
    choices = []
    answer = integrate(expression, x)

    return latexify((statement, choices, answer))
# Integration by parts
def int_parts(config_table:dict):
    n = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0]
    )

    v, du = get_two_different_functions(config_table)

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
# TODO

# Summary
def int_summary(config_table:dict):
    operator_array = [
        int_basic,
        int_parts,
        int_u_sub
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - Discontinuities -

# Rational functions
def dis_rational(config_table:dict):
    a, b, c, d, e = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        5
    )

    numerator = ((x - a) * (x - b)).expand()
    denominator = (x - c) * ((x - d) * (x - e)).expand()

    statement = numerator / denominator
    choices = []
    answer = real_roots(denominator)

    return latexify((statement, choices, answer))

# - Derivatives -

# Power rule
def deriv_power(config_table:dict):
    expression = get_polynomial(config_table)
    
    statement = diff(expression, x, evaluate=False)
    choices = []
    answer = diff(expression, x)

    return latexify((statement, choices, answer))
# Product rule
def deriv_product(config_table:dict):
    f, g = get_two_different_functions(config_table)

    statement = diff(f * g, x, evaluate=False)
    choices = []
    answer = diff(f * g, x)

    return latexify((statement, choices, answer))
# Quotient rule
def deriv_quotient(config_table:dict):
    f, g = get_two_different_functions(config_table)

    statement = diff(f / g, x, evaluate=False)
    choices = []
    answer = diff(f / g, x)

    return latexify((statement, choices, answer))
# Chain rule
def deriv_chain(config_table:dict):
    g = random_function(config_table, x, 1)
    f = random_function(config_table, g, 1)

    statement = diff(f, x, evaluate=False)
    choices = []
    answer = diff(f, x)

    return latexify((statement, choices, answer))
# Summary
def deriv_summary(config_table:dict):
    operator_array = [
        deriv_power,
        deriv_product,
        deriv_quotient,
        deriv_chain
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - Summary -

# Calculus summary
def summary(config_table:dict):
    operator_array = [
        int_basic,
        int_parts,
        int_u_sub,
        dis_rational,
        deriv_power,
        deriv_product,
        deriv_quotient,
        deriv_chain
    ]
    operation = choice(operator_array)
    return operation(config_table)