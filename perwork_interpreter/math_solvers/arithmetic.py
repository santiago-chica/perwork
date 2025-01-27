from sympy import (
    latex,
    solve,
    diff,
    Eq,
    Add,
    Mul,
    Expr,
    fraction,
    Rational
)
from numpy.random import randint, choice
from sympy.abc import x, y
from json import load as json_load
from random import choice
from utils import (
    get_numbers_in_range
)

# -- Arithmetic --

# - Integers -

# TODO

# Add
def int_add(question:dict):
    config_table = question['configuration']
    l, r = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    statement = Add(l, r, evaluate=False)
    choices = []
    answer = statement.simplify()

    return (statement, choices, answer)
# Substract
def int_sub(question:dict):
    config_table = question['configuration']
    l, r = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    statement = Add(l, -r, evaluate=False)
    choices = []
    answer = statement.simplify()

    return (statement, choices, answer)
# Multiply
def int_mul(question:dict):
    config_table = question['configuration']
    l, r = get_numbers_in_range(
        config_table['minimum_factor'],
        config_table['maximum_factor'],
        [0, 1],
        2
    )

    statement = Mul(l, r, evaluate=False)
    choices = []
    answer = statement.simplify()

    return (statement, choices, answer)
# Divide
def int_div(question:dict):
    config_table = question['configuration']

    divisor = get_numbers_in_range(
        config_table['minimum_factor'],
        config_table['maximum_factor'],
        [0, 1],
    )

    answer = get_numbers_in_range(
        config_table['minimum_factor'],
        config_table['maximum_factor'],
        [1],
    )

    dividend = divisor * answer

    statement = Rational(dividend, divisor, gcd=1)
    choices = []

    return (statement, choices, answer)
# Add and substract
def int_add_sub(question:dict):
    operator_array = [
        int_add,
        int_sub
    ]
    operation = choice(operator_array)
    return operation(question)
# Multiply and divide
def int_mul_div(question:dict):
    operator_array = [
        int_mul,
        int_div
    ]
    operation = choice(operator_array)
    return operation(question)
# Summary
def int_summary(question:dict):
    on_add_sub = choice([True, False])

    if on_add_sub:
        return int_add_sub(question)
    
    return int_mul_div(question)

# - Order of operations -

# TODO
# Basic operations
# Include exponents
# Include parentheses
# Include exponents and parentheses

# - Fractions -

# TODO
# Add with common denominators
# Subtract with common denominators
# Add with uncommon denominators
# Subtract with uncommon denominators
# Multiply
# Divide
# Simplify
# Add and subtract
# Multiply and divide
# Summary

# - Summary -

# TODO
# Arithmetic summary