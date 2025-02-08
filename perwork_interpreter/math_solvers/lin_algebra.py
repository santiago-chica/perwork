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
    Mul,
    Matrix,
    trace,
    det
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

def get_matrix(config_table:dict, dimensions:int, is_identity=False):
    # Each row
    matrix_information = []
    for i in range(dimensions):
        row = []
        # Each dimension
        for j in range(dimensions):
            if is_identity:
                n = 1 if i == j else 0
            else:
                n = get_numbers_in_range(
                    config_table['minimum_integer'],
                    config_table['maximum_integer']
                )
            row.append(n)
        matrix_information.append(row)

    matrix = Matrix(matrix_information)

    if det(matrix) == 0:
        matrix = get_matrix(config_table, dimensions, is_identity)

    return matrix
def get_vector(config_table:dict, dimensions:int):
    vector_information = []
    for _ in range(dimensions):
        n = get_numbers_in_range(
            config_table['minimum_integer'],
            config_table['maximum_integer']
        )
        vector_information.append([n])
    return Matrix(vector_information)

def generic_add(config_table:dict, dimensions:int):
    m1 = get_matrix(config_table, dimensions)
    m2 = get_matrix(config_table, dimensions)

    statement = string_to_tex(f'{latex(m1)} + {latex(m2)}')
    choices = []
    answer = string_to_tex(latex(m1 + m2))

    return (statement, choices, answer)
def generic_sub(config_table:dict, dimensions:int):
    m1 = get_matrix(config_table, dimensions)
    m2 = get_matrix(config_table, dimensions)

    statement = string_to_tex(f'{latex(m1)} - {latex(m2)}')
    choices = []
    answer = string_to_tex(latex(m1 - m2))

    return (statement, choices, answer)
def generic_trace(config_table:dict, dimensions:int):
    statement = get_matrix(config_table, dimensions)
    choices = []
    answer = trace(statement)

    return latexify((statement, choices, answer))
def generic_det(config_table:dict, dimensions:int):
    statement = get_matrix(config_table, dimensions)
    choices = []
    answer = det(statement)

    return latexify((statement, choices, answer))
def generic_inv(config_table:dict, dimensions:int):
    statement = get_matrix(config_table, dimensions)
    choices = []
    answer = statement.inv()

    return latexify((statement, choices, answer))
def generic_char_poly(config_table:dict, dimensions:int):
    identity = get_matrix(config_table, dimensions, True)

    statement = get_matrix(config_table, dimensions)
    choices = []

    second_matrix = statement - x * identity
    polynomial = det(second_matrix)

    answer = polynomial.expand()

    return latexify((statement, choices, answer))
def generic_eigenvals(config_table:dict, dimensions:int):
    statement = get_matrix(config_table, dimensions)
    choices = []
    answer = statement.eigenvals(False)

    return latexify((statement, choices, answer))
def generic_eigenvects(config_table:dict, dimensions:int):
    statement = get_matrix(config_table, dimensions)
    choices = []
    answer = statement.eigenvects(False)

    return latexify((statement, choices, answer))
def generic_vec_times_matrix(config_table:dict, dimensions:int):
    m = get_matrix(config_table, dimensions)
    v = get_vector(config_table, dimensions)

    statement = string_to_tex(f'{latex(m)} \\cdot {latex(v)}')
    choices = []
    answer = string_to_tex(latex(m * v))

    return (statement, choices, answer)
def generic_multiply(config_table:dict, dimensions:int):
    m1 = get_matrix(config_table, dimensions)
    m2 = get_matrix(config_table, dimensions)

    statement = string_to_tex(f'{latex(m1)} \\cdot {latex(m2)}')
    choices = []
    answer = string_to_tex(latex(m1 * m2))

    return (statement, choices, answer)
# - 2 x 2 matrices -

# Add
def m2x2_add(config_table:dict):
    return generic_add(config_table, 2)
# Subtract
def m2x2_sub(config_table:dict):
    return generic_sub(config_table, 2)
# Trace
def m2x2_trace(config_table:dict):
    return generic_trace(config_table, 2)
# Determinant
def m2x2_det(config_table:dict):
    return generic_det(config_table, 2)
# Inverse
def m2x2_inv(config_table:dict):
    return generic_inv(config_table, 2)
# Characteristic polynomial
def m2x2_char_poly(config_table:dict):
    return generic_char_poly(config_table, 2)
# Eigenvalues
def m2x2_eigenvals(config_table:dict):
    return generic_eigenvals(config_table, 2)
# Eigenvectors
def m2x2_eigenvects(config_table:dict):
    return generic_eigenvects(config_table, 2)
# Vector times matrix
def m2x2_vec_times_matrix(config_table:dict):
    return generic_vec_times_matrix(config_table, 2)
# Multiply
def m2x2_multiply(config_table:dict):
    return generic_multiply(config_table, 2)
# Summary
def m2x2_summary(config_table:dict):
    operator_array = [
        m2x2_add,
        m2x2_sub,
        m2x2_trace,
        m2x2_det,
        m2x2_inv,
        m2x2_char_poly,
        m2x2_eigenvals,
        m2x2_eigenvects,
        m2x2_vec_times_matrix,
        m2x2_multiply
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - 3 x 3 matrices -

# Add
def m3x3_add(config_table:dict):
    return generic_add(config_table, 3)
# Subtract
def m3x3_sub(config_table:dict):
    return generic_sub(config_table, 3)
# Trace
def m3x3_trace(config_table:dict):
    return generic_trace(config_table, 3)
# Determinant
def m3x3_det(config_table:dict):
    return generic_det(config_table, 3)
# Inverse
def m3x3_inv(config_table:dict):
    return generic_inv(config_table, 3)
# Characteristic polynomial
def m3x3_char_poly(config_table:dict):
    return generic_char_poly(config_table, 3)
# Eigenvalues
def m3x3_eigenvals(config_table:dict):
    return generic_eigenvals(config_table, 3)
# Eigenvectors
def m3x3_eigenvects(config_table:dict):
    return generic_eigenvects(config_table, 3)
# Vector times matrix
def m3x3_vec_times_matrix(config_table:dict):
    return generic_vec_times_matrix(config_table, 3)
# Multiply
def m3x3_multiply(config_table:dict):
    return generic_multiply(config_table, 3)
# Summary
def m3x3_summary(config_table:dict):
    operator_array = [
        m3x3_add,
        m3x3_sub,
        m3x3_trace,
        m3x3_det,
        m3x3_inv,
        m3x3_char_poly,
        m3x3_eigenvals,
        m3x3_eigenvects,
        m3x3_vec_times_matrix,
        m3x3_multiply
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - Other matrices -
# TODO
# Matrix null space
# Matrix nullity
# Matrix rank
# Row reduce
# Multiply
# Summary