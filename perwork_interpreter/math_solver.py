import math_solvers.arithmetic as arithmetic
import math_solvers.number_theory as number_theory
import math_solvers.algebra as algebra
import math_solvers.calculus as calculus

def parse_math(question:dict):
    config_table = question['configuration']
    return {
        'arithmetic_int_add': arithmetic.int_add, # Arithmetic
        'arithmetic_int_sub': arithmetic.int_sub,
        'arithmetic_int_mul': arithmetic.int_mul,
        'arithmetic_int_div': arithmetic.int_div,
        'arithmetic_int_add_sub': arithmetic.int_add_sub,
        'arithmetic_int_mul_div': arithmetic.int_mul_div,
        'arithmetic_int_summary': arithmetic.int_summary,
        'calculus_deriv_power': calculus.deriv_power,
        'algebra_eq_int_one_step': algebra.eq_int_one_step
    }.get(question['operation'])(config_table)