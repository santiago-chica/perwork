

import math_solvers.arithmetic as arithmetic
import math_solvers.number_theory as number_theory
import math_solvers.algebra as algebra
import math_solvers.calculus as calculus
# -- Calculus --


def parse_math(question:dict):
    return {
        'arithmetic_int_add': arithmetic.arithmetic_int_add,
        'arithmetic_int_sub': arithmetic.arithmetic_int_sub,
        'calculus_deriv_power': calculus.calculus_deriv_power
    }.get(question['operation'])(question)