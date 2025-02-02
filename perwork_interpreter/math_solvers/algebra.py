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
    solve
)
from numpy.random import randint, choice
from sympy.abc import x, y
from utils import (
    get_numbers_in_range,
    latexify,
    prime_number_list,
    string_to_tex
)

# - Radicals -

# Utils

def related_sqrts(config_table:dict):
    c_1, c_2 = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    square = get_numbers_in_range(
        config_table['minimum_square'],
        config_table['maximum_square'],
        [0]
    ) ** 2

    primes = prime_number_list(config_table['minimum_prime'], config_table['maximum_prime'])

    prime = choice(primes)

    return c_1,c_2,square,prime

# Add
def rad_add(config_table:dict):
    c_1, c_2, square, prime = related_sqrts(config_table)

    term_1 = c_1 * sqrt(prime)
    term_2 = c_2 * sqrt(prime * square)

    statement = string_to_tex(f'{c_1} \\sqrt{{{prime}}} + {c_2} \\sqrt{{{prime * square}}}')
    choices = []
    answer = latex(term_1 + term_2, mode='equation*', order='none')

    return (statement, choices, answer)
# Substract
def rad_sub(config_table:dict):
    c_1, c_2, square, prime = related_sqrts(config_table)

    term_1 = c_1 * sqrt(prime)
    term_2 = c_2 * sqrt(prime * square)

    statement = string_to_tex(f'{c_1} \\sqrt{{{prime}}} - {c_2} \\sqrt{{{prime * square}}}')
    choices = []
    answer = latex(term_1 - term_2, mode='equation*', order='none')

    return (statement, choices, answer)
# Multiply
def rad_mul(config_table:dict):
    c_1, c_2 = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    primes = prime_number_list(config_table['minimum_prime'], config_table['maximum_prime'])

    p_1, p_2 = choice(primes, 2, False)

    term_1 = c_1 * sqrt(p_1)
    term_2 = c_2 * sqrt(p_2)

    statement = string_to_tex(f'{latex(term_1)} \\cdot {latex(term_2)}')
    choices = []
    answer = latex(term_1 * term_2, mode='equation*', order='none')

    return (statement, choices, answer)
# Distribute
def rad_dis(config_table:dict):
    c_1, c_2, c_3 = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        3
    )
    primes = prime_number_list(config_table['minimum_prime'], config_table['maximum_prime'])

    p_1, p_2, p_3 = choice(primes, 3, False)

    term_1 = c_1 * sqrt(p_1)
    term_2 = c_2 * sqrt(p_2)
    term_3 = c_3 * sqrt(p_3)

    is_positive = choice([True, False])

    if is_positive:
        symbol = '+'
        answer = term_1 * (term_2 + term_3)
    else:
        symbol = '-'
        answer = term_1 * (term_2 - term_3)

    statement = string_to_tex(f'{latex(term_1)} \\left( {latex(term_2)} {symbol} {latex(term_3)} \\right)')
    choices = []
    answer = latex(expand(answer), mode='equation*', order='none')

    return (statement, choices, answer)
# Rationalize
def rad_rat(config_table:dict):
    n = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0]
    )

    primes = prime_number_list(config_table['minimum_prime'], config_table['maximum_prime'])
    prime = choice(primes)

    square_latex = f'\\sqrt{{{prime}}}'
    statement = string_to_tex(f'\\frac{{{n}}}{{{square_latex}}}')
    choices = []
    answer = latex(n / sqrt(prime), mode='equation*', order='none')

    return (statement, choices, answer)
# Simplify
def rad_simplify(config_table:dict):
    factor_count = get_numbers_in_range(
        config_table['minimum_factor_count'],
        config_table['maximum_factor_count'],
        [0]
    )

    numbers = get_numbers_in_range(
        config_table['minimum_factor'],
        config_table['maximum_factor'],
        [0, 1],
        factor_count
    )

    total = 1

    for n in numbers:
        total *= n

    statement = string_to_tex(f'\\sqrt{{{total}}}')
    choices = []
    answer = latex(sqrt(total), mode='equation*', order='none')

    return (statement, choices, answer)
# Summary
def rad_summary(config_table:dict):
    operator_array = [
        rad_add,
        rad_sub,
        rad_mul,
        rad_dis,
        rad_rat,
        rad_simplify
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - Complex Numbers -

# Utils
def get_complex(config_table:dict):
    a, b = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    return a + b * I
# Add
def com_add(config_table:dict):
    z_1 = get_complex(config_table)
    z_2 = get_complex(config_table)

    statemet = string_to_tex(f'({latex(z_1)}) + ({latex(z_2)})')
    choices = []
    answer = string_to_tex(latex(z_1 + z_2))

    return statemet, choices, answer
# Subtract
def com_sub(config_table:dict):
    z_1 = get_complex(config_table)
    z_2 = get_complex(config_table)

    statemet = string_to_tex(f'({latex(z_1)}) - ({latex(z_2)})')
    choices = []
    answer = string_to_tex(latex(z_1 - z_2))

    return statemet, choices, answer
# Multiply
def com_mul(config_table:dict):
    z_1 = get_complex(config_table)
    z_2 = get_complex(config_table)

    statemet = string_to_tex(f'({latex(z_1)}) \\times ({latex(z_2)})')
    choices = []
    answer = string_to_tex(latex((z_1 * z_2).expand()))

    return statemet, choices, answer
# Divide
def com_div(config_table:dict):
    z_1 = get_complex(config_table)
    z_2 = get_complex(config_table)

    statemet = string_to_tex(f'({latex(z_1)}) \\div ({latex(z_2)})')
    choices = []
    answer = string_to_tex(latex((z_1 / z_2).expand()))

    return statemet, choices, answer
# Find the norm
def com_norm(config_table:dict):
    a, b = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    statement = string_to_tex(f'{a} + {b}i')
    choices = []
    answer = string_to_tex(latex(sqrt(a ** 2 + b ** 2)))

    return statement, choices, answer
# Summary
def com_summary(config_table:dict):
    operator_array = [
        com_add,
        com_sub,
        com_mul,
        com_div,
        com_norm,
        com_summary
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - Polynomials -

# Utils
def get_pol(config_table:dict, degree:int):
    pol = 0
    for e in range(0, degree + 1):
        n = get_numbers_in_range(
            config_table['minimum_integer'],
            config_table['maximum_integer'],
            [0]
        )
        pol += n * x ** e
    return pol

# Evaluate at a point
def pol_eval(config_table:dict):
    n = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0]
    )
    d = get_numbers_in_range(
        config_table['minimum_degree'],
        config_table['maximum_degree'],
        [0]
    )

    pol = get_pol(config_table, d)

    statement = string_to_tex(f'f\\left({n}\\right) = {latex(pol)}')
    choices = []
    answer = string_to_tex(latex(pol.subs(x, n)))

    return (statement, choices, answer)
# Add
def pol_add(config_table:dict):
    d_1, d_2 = get_numbers_in_range(
        config_table['minimum_degree'],
        config_table['maximum_degree'],
        [0],
        2
    )
    
    pol_1 = get_pol(config_table, d_1)
    pol_2 = get_pol(config_table, d_2)

    statement = string_to_tex(f'({latex(pol_1)}) + ({latex(pol_2)})')
    choices = []
    answer = string_to_tex(latex(pol_1 + pol_2))

    return (statement, choices, answer)
# Subtract
def pol_sub(config_table:dict):
    d_1, d_2 = get_numbers_in_range(
        config_table['minimum_degree'],
        config_table['maximum_degree'],
        [0],
        2
    )
    
    pol_1 = get_pol(config_table, d_1)
    pol_2 = get_pol(config_table, d_2)

    statement = string_to_tex(f'({latex(pol_1)}) - ({latex(pol_2)})')
    choices = []
    answer = string_to_tex(latex(pol_1 - pol_2))

    return (statement, choices, answer)
# Expand
def pol_expand(config_table:dict):
    d_1, d_2 = get_numbers_in_range(
        config_table['minimum_degree'],
        config_table['maximum_degree'],
        [0],
        2
    )
    
    pol_1 = get_pol(config_table, d_1)
    pol_2 = get_pol(config_table, d_2)

    statement = string_to_tex(f'({latex(pol_1)})({latex(pol_2)})')
    choices = []
    answer = string_to_tex(latex((pol_1 * pol_2).expand()))

    return (statement, choices, answer)
# Factor
def pol_factor(config_table:dict):
    a, b = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )
    
    pol_1 = x + a
    pol_2 = x + b

    statement = string_to_tex(latex((pol_1 * pol_2).expand()))
    choices = []
    answer = string_to_tex(f'({latex(pol_1)})({latex(pol_2)})')

    return (statement, choices, answer)
# Multiply monomial and polynomial
def pol_mul_mon_pol(config_table:dict):
    d_1, d_2 = get_numbers_in_range(
        config_table['minimum_degree'],
        config_table['maximum_degree'],
        [0],
        2
    )

    n = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0]
    )

    mon = n * x ** d_1
    pol = get_pol(config_table, d_2)

    statement = string_to_tex(f'({latex(mon)})({latex(pol)})')
    choices = []
    answer = string_to_tex(latex((mon * pol).expand()))

    return (statement, choices, answer)
# Multiply two polynomials
def pol_mul_pol_pol(config_table:dict):
    d_1, d_2 = get_numbers_in_range(
        config_table['minimum_degree'],
        config_table['maximum_degree'],
        [0],
        2
    )
    pol_1 = get_pol(config_table, d_1)
    pol_2 = get_pol(config_table, d_2)

    statement = string_to_tex(f'({latex(pol_1)})({latex(pol_2)})')
    choices = []
    answer = string_to_tex(latex((pol_1 * pol_2).expand()))

    return (statement, choices, answer)
# Binomial expansion
def pol_bin_expansion(config_table:dict):
    d_1, d_2 = get_numbers_in_range(
        config_table['minimum_degree'],
        config_table['maximum_degree'],
        [0],
        2
    )

    d_3 = get_numbers_in_range(
        config_table['minimum_degree'],
        config_table['maximum_degree'],
        [0, 1]
    )
    c_1, c_2 = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    is_add = choice([True, False])

    mon_1 = c_1 * x ** d_1
    mon_2 = c_2 * y ** d_2

    if is_add:
        statement = string_to_tex(f'\\left({latex(mon_1)} + {latex(mon_2)}\\right)^{{{d_3}}}')
        answer = ((mon_1 + mon_2) ** d_3).expand()
    else:
        statement = string_to_tex(f'\\left({latex(mon_1)} - {latex(mon_2)}\\right)^{{{d_3}}}')
        answer = ((mon_1 - mon_2) ** d_3).expand()

    choices = []
    answer = string_to_tex(latex(answer))
    return (statement, choices, answer)
# Horizontal axis intercepts
def pol_hor_axis(config_table:dict):
    d = get_numbers_in_range(
        config_table['minimum_degree'],
        config_table['maximum_degree'],
        [0]
    )

    f = 1

    for _ in range(d):
        a = get_numbers_in_range(
            config_table['minimum_integer'],
            config_table['maximum_integer'],
            [0]
        )
        f *= (x + a)
    
    f = f.expand()

    statement = string_to_tex(f'{latex(f)}')
    choices = []
    answer = string_to_tex(latex(solve(f, x)))

    return (statement, choices, answer)
# Summary
def pol_summary(config_table:dict):
    operator_array = [
        pol_eval,
        pol_add,
        pol_sub,
        pol_expand,
        pol_factor,
        pol_mul_mon_pol,
        pol_mul_pol_pol,
        pol_bin_expansion,
        pol_hor_axis
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - Quadratic polynomials -

# TODO
# Expand
# Factor
# Complete the square
# Summary

# - Equation Solving -

# - Integers -

# One step equations
def eq_int_one_step(config_table:dict):
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
    return latexify((statement, choices, answer))
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