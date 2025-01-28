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
        'arithmetic_order_basic': arithmetic.order_basic,
        'arithmetic_order_include_exp': arithmetic.order_include_exp,
        'arithmetic_order_include_paren': arithmetic.order_include_paren,
        'arithmetic_order_include_exp_paren': arithmetic.order_include_exp_paren,
        'arithmetic_frac_add_common': arithmetic.frac_add_common,
        'arithmetic_frac_sub_common': arithmetic.frac_sub_common,
        'arithmetic_frac_add_uncommon': arithmetic.frac_add_uncommon,
        'arithmetic_frac_sub_uncommon': arithmetic.frac_sub_uncommon,
        'arithmetic_frac_multiply': arithmetic.frac_multiply,
        'arithmetic_frac_div': arithmetic.frac_div,
        'arithmetic_frac_simplify': arithmetic.frac_simplify,
        'arithmetic_frac_add_sub': arithmetic.frac_add_sub,
        'arithmetic_frac_mul_div': arithmetic.frac_mul_div,
        'arithmetic_frac_summary': arithmetic.frac_summary,
        'arithmetic_summary': arithmetic.summary,
        'calculus_deriv_power': calculus.deriv_power,
        'algebra_eq_int_one_step': algebra.eq_int_one_step
    }.get(question['operation'])(config_table)