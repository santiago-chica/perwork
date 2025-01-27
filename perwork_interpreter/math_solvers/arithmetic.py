from sympy import (
    latex,
    solve,
    diff,
    Eq,
    Add,
    Mul,
    Expr
)
from numpy.random import randint, choice
from sympy.abc import x, y
from json import load as json_load
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
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [],
        2
    )

    statement = Mul(l, r, evaluate=False)
    choices = []
    answer = statement.simplify()

    return (statement, choices, answer)
# Divide
def int_div(question:dict):
    config_table = question['configuration']
    l, r = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [],
        2
    )

    statement = Expr(l / r, evaluate=False)
    choices = []
    answer = statement.simplify()

    return (statement, choices, answer)
# Add and substract
# Multiply and divide
# Summary

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