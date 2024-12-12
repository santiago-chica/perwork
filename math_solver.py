from sympy import (
    latex,
    solve,
    diff,
    Eq,
    Add,
)
from numpy.random import randint, choice
from sympy.abc import x, y
from json import load as json_load
from utils import (
    get_numbers_in_range
)

# -- Arithmetic --

# - Integers -

def arithmetic_int_add(question:dict):
    
    config_table = question['configuration']
    l, r = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    equation = Add(l, r, evaluate=False)

    statement = latex(equation, mode='equation*', order='none')
    choices = [[]]
    answer = latex(equation.simplify(), mode='equation*')

    return (statement, choices, answer)

def arithmetic_int_sub(question:dict):

    config_table = question['configuration']
    l, r = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    equation = Add(l, -r, evaluate=False)

    statement = latex(equation, mode='equation*', order='none')
    choices = [[]]
    answer = latex(equation.simplify(), mode='equation*')

    return (statement, choices, answer)

# -- Calculus --

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
    f = coefficient * x ** exponent
    f_prime = diff(f, x)

    statement = latex(f, mode='equation*')
    choices = [[]]
    answer = latex(f_prime, mode='equation*')

    

    return (statement, choices, answer)



def algebra_eq_int_one_step(question:dict):

    config_table = question['configuration']
    l, r = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1],
        2,
        can_repeat=False
    )

    equation = Eq(l * x, r)

    statement = latex(equation, mode='equation*')
    choices = [[]]
    answer = latex(solve(equation, x)[0], mode='equation*')

    return (statement, choices, answer)

def parse_math(question:dict):
    return {
        'arithmetic_int_add': arithmetic_int_add,
        'arithmetic_int_sub': arithmetic_int_sub,
        'calculus_deriv_power': calculus_deriv_power,
        'algebra_eq_int_one_step': algebra_eq_int_one_step,
    }.get(question['operation'])(question)