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

# -- Algebra --

# - Radicals -

# TODO
# Add
# Substract
# Multiply
# Distribute
# Rationalize
# Simplify
# Summary

# - Complex Numbers -

# TODO
# Add
# Subtract
# Multiply
# Divide
# Find the norm
# Summary

# - Polynomials -

# TODO
# Evaluate at a point
# Add
# Subtract
# Expand
# Factor
# Multiply monomial and polynomial
# Multiply two polynomials
# Binomial expansion
# Horizontal axis intercepts
# Summary

# - Quadratic polynomials -

# TODO
# Expand
# Factor
# Complete the square
# Summary

# - Equation Solving -

# - Integers -

# One step equations
def eq_int_one_step(question:dict):
    config_table = question['configuration']
    l, r = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1],
        2,
        can_repeat=False
    )
    statement = Eq(l * x, r)
    choices = []
    answer = solve(statement, x)[0]
    return (statement, choices, answer)
# Two step equations
# Multi-step equations
# Summary

# - Rationals -

# TODO
# One step equations
# Two step equations
# Multi-step equations
# Summary

# - Radicals -

# TODO
# One step equations
# Two step equations
# Multi-step equations
# Summary

# - Absolute Values -

# TODO
# Integer equations
# Rational equations
# Radical equations

# - Quadratic Equations -

# TODO
# Completed squares
# Integer solutions
# Difference of squares
# Complex number solutions
# Radical solutions
# Summary

# - General -

# TODO
# Completed squares
# Integer solutions
# Difference of squares
# Complex number solutions
# Radical solutions
# Summary

# - Exponents and logarithms -

# Exponential equations
# Logarithmic equations

# - Systems of Equations -

# TODO
# Systems of two equations
# Systems of three equations
# Systems of four equations

# - Summary -

# TODO
# Algebra summary