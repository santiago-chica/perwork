from collections import Counter
from sympy import (
    latex,
    solve,
    diff,
    sqrt,
    Add,
    Mul,
    expand,
    I,
    Function,
    solve,
    Eq,
    Rational,
    Abs,
    Symbol,
    log,
    Sum,
    DotProduct,
    Mul
)
from numpy import (
    clip,
    median,
    log,
    exp,
    var,
    std,
    quantile
)

from numpy import median as med

from numpy.random import (
    randint,
    choice,
    normal,
    random
)
from sympy.abc import x, y, z
from utils import (
    get_numbers_in_range,
    latexify,
    prime_number_list,
    string_to_tex,
    format_number
)

from sympy.vector import CoordSys3D

N = CoordSys3D('N')

# - Vectors -

def get_2d_vector(config_table:dict):
    a, b = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    return a * N.i + b * N.j

def get_3d_vector(config_table:dict):
    a, b, c = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        3
    )

    return a * N.i + b * N.j + c * N.k
# - 2D vectors -

def generic_vec_add(config_table:dict, three_dimensions:bool):
    if three_dimensions:
        vector_function = get_3d_vector
    else:
        vector_function = get_2d_vector

    v1 = vector_function(config_table)
    v2 = vector_function(config_table)

    statement = string_to_tex(f'\\left({latex(v1)}\\right) + \\left({latex(v2)}\\right)')
    choices = []
    answer = string_to_tex(latex(v1 + v2))

    return (statement, choices, answer)
def generic_vec_sub(config_table:dict, three_dimensions:bool):
    if three_dimensions:
        vector_function = get_3d_vector
    else:
        vector_function = get_2d_vector

    v1 = vector_function(config_table)
    v2 = vector_function(config_table)

    statement = string_to_tex(f'\\left({latex(v1)}\\right) - \\left({latex(v2)}\\right)')
    choices = []
    answer = string_to_tex(latex(v1 - v2))

    return (statement, choices, answer)
def generic_vec_scalar(config_table:dict, three_dimensions:bool):
    if three_dimensions:
        vector_function = get_3d_vector
    else:
        vector_function = get_2d_vector

    v = vector_function(config_table)
    scalar = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1]
    )

    statement = Mul(v, scalar, evaluate=False)
    choices = []
    answer = statement.expand()

    return latexify((statement, choices, answer))
def generic_vec_dot(config_table:dict, three_dimensions:bool):
    if three_dimensions:
        vector_function = get_3d_vector
    else:
        vector_function = get_2d_vector

    v1 = vector_function(config_table)
    v2 = vector_function(config_table)

    statement = string_to_tex(f'\\left({latex(v1)}\\right) \\cdot \\left({latex(v2)}\\right)')
    choices = []
    answer = string_to_tex(latex(v1 & v2))

    return (statement, choices, answer)
def generic_vec_cross(config_table:dict, three_dimensions:bool):
    if three_dimensions:
        vector_function = get_3d_vector
    else:
        vector_function = get_2d_vector

    v1 = vector_function(config_table)
    v2 = vector_function(config_table)

    statement = string_to_tex(f'\\left({latex(v1)}\\right) \\times \\left({latex(v2)}\\right)')
    choices = []
    answer = string_to_tex(latex(v1 ^ v2))

    return (statement, choices, answer)

# Add
def vec_2d_add(config_table):
    return generic_vec_add(config_table, False)
# Subtract
def vec_2d_sub(config_table):
    return generic_vec_sub(config_table, False)
# Multiply scalar and vector
def vec_2d_scalar(config_table):
    return generic_vec_scalar(config_table, False)
# Dot product
def vec_2d_dot(config_table):
    return generic_vec_dot(config_table, False)
# Summary
def vec_2d_summary(config_table:dict):
    operator_array = [
        vec_2d_add,
        vec_2d_sub,
        vec_2d_scalar,
        vec_2d_dot
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - 3D vectors -

# Add
def vec_3d_add(config_table):
    return generic_vec_add(config_table, True)
# Subtract
def vec_3d_sub(config_table):
    return generic_vec_sub(config_table, True)
# Multiply scalar and vector
def vec_3d_scalar(config_table):
    return generic_vec_scalar(config_table, True)
# Dot product
def vec_3d_dot(config_table):
    return generic_vec_dot(config_table, True)
# Cross product
def vec_3d_cross(config_table):
    return generic_vec_cross(config_table, True)
# Summary
def vec_3d_summary(config_table:dict):
    operator_array = [
        vec_3d_add,
        vec_3d_sub,
        vec_3d_scalar,
        vec_3d_dot,
        vec_3d_cross
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - Matrices -

# - 2 x 2 matrices -
# TODO
# Add
# Subtract
# Trace
# Determinant
# Inverse
# Characteristic polynomial
# Eigenvalues
# Eigenvectors
# Vector times matrix
# Multiply
# Summary

# - 3 x 3 matrices -
# TODO
# Add
# Subtract
# Trace
# Determinant
# Inverse
# Characteristic polynomial
# Eigenvalues
# Eigenvectors
# Vector times matrix
# Multiply
# Summary

# - Other matrices -
# TODO
# Matrix null space
# Matrix nullity
# Matrix rank
# Row reduce
# Multiply
# Summary