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

# TODO

# Add
def arithmetic_int_add(question:dict):
    
    config_table = question['configuration']
    l, r = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    statement = Add(l, r, evaluate=False)
    choices = [[]]
    answer = statement.simplify()

    return (statement, choices, answer)
# Substract
def arithmetic_int_sub(question:dict):

    config_table = question['configuration']
    l, r = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    statement = Add(l, -r, evaluate=False)
    choices = [[]]
    answer = statement.simplify()

    return (statement, choices, answer)
# Multiply
# Divide
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