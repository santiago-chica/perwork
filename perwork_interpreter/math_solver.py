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
        'number_theory_divisibility': number_theory.divisibility, # Number theory
        'number_theory_prime': number_theory.prime,
        'number_theory_prime_fac': number_theory.prime_fac,
        'number_theory_divisors': number_theory.divisors,
        'number_theory_gcd': number_theory.gcd,
        'number_theory_lcm': number_theory.lcm,
        'number_theory_gcd_lcm': number_theory.gcd_lcm,
        'number_theory_rel_prime': number_theory.rel_prime,
        'number_theory_summary': number_theory.summary,
        'algebra_rad_add': algebra.rad_add, # Algebra
        'algebra_rad_sub': algebra.rad_sub,
        'algebra_rad_mul': algebra.rad_mul,
        'algebra_rad_dis': algebra.rad_dis,
        'algebra_rad_rat': algebra.rad_rat,
        'algebra_rad_simplify': algebra.rad_simplify,
        'algebra_rad_summary': algebra.rad_summary,
        'algebra_com_add': algebra.com_add,
        'algebra_com_sub': algebra.com_sub,
        'algebra_com_mul': algebra.com_mul,
        'algebra_com_div': algebra.com_div,
        'algebra_com_norm': algebra.com_norm,
        'algebra_com_summary': algebra.com_summary,
        'algebra_pol_eval': algebra.pol_eval,
        'algebra_pol_add': algebra.pol_add,
        'algebra_pol_sub': algebra.pol_sub,
        'algebra_pol_expand': algebra.pol_expand,
        'algebra_pol_factor': algebra.pol_factor,
        'algebra_pol_mul_mon_pol': algebra.pol_mul_mon_pol,
        'algebra_pol_mul_pol_pol': algebra.pol_mul_pol_pol,
        'algebra_pol_bin_expansion': algebra.pol_bin_expansion,
        'algebra_pol_hor_axis': algebra.pol_hor_axis,
        'algebra_pol_summary': algebra.pol_summary,
        'algebra_eq_int_one_step': algebra.eq_int_one_step, 
        'calculus_int_basic': calculus.int_basic, # Calculus
        'calculus_int_parts': calculus.int_parts,
        'calculus_int_u_sub': calculus.int_u_sub,
        'calculus_deriv_power': calculus.deriv_power
    }.get(question['operation'])(config_table)