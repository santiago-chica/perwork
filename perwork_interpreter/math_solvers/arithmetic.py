from numpy.random import randint, choice
from sympy.abc import x, y
from json import load as json_load
from random import choice
from utils import (
    get_numbers_in_range,
    latexify,
    string_to_tex
)

# - Integers -

# Add
def int_add(config_table:dict):
    l, r = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    statement = string_to_tex(f'{l} + {r}')
    choices = []
    answer = string_to_tex(str(l + r))

    return (statement, choices, answer)
# Substract
def int_sub(config_table:dict):
    l, r = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    statement = string_to_tex(f'{l} - {r}')
    choices = []
    answer = string_to_tex(str(l - r))

    return (statement, choices, answer)
# Multiply
def int_mul(config_table:dict):
    l, r = get_numbers_in_range(
        config_table['minimum_factor'],
        config_table['maximum_factor'],
        [0, 1],
        2
    )

    statement = string_to_tex(f'{l} \\times {r}')
    choices = []
    answer = string_to_tex(str(l * r))

    return (statement, choices, answer)
# Divide
def int_div(config_table:dict):
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

    statement = string_to_tex(f'{dividend} \\div {divisor}')
    answer = string_to_tex(str(answer))
    choices = []

    return (statement, choices, answer)
# Add and substract
def int_add_sub(config_table:dict):
    operator_array = [
        int_add,
        int_sub
    ]
    operation = choice(operator_array)
    return operation(config_table)
# Multiply and divide
def int_mul_div(config_table:dict):
    operator_array = [
        int_mul,
        int_div
    ]
    operation = choice(operator_array)
    return operation(config_table)
# Summary
def int_summary(config_table:dict):
    on_add_sub = choice([True, False])

    if on_add_sub:
        return int_add_sub(config_table)
    
    return int_mul_div(config_table)

# - Order of operations -

# Basic operations
def order_basic(config_table:dict):
    n1, n2, n3, n4 = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        4
    )
    statement = 2
    choices = []
    answer = statement.simplify()

    return latexify((statement, choices, answer))
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