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
    log
)
from numpy.random import randint, choice
from sympy.abc import x, y, z
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
        invert = choice([True, False])
        if invert:
            a *= -1
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

# Expand
def qpol_expand(config_table:dict):
    n, c_1, b_1, c_2, b_2 = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        5
    )

    mon_1 = c_1 * x + b_1
    mon_2 = c_2 * x + b_2

    statement = n * mon_1 * mon_2
    choices = []
    answer = statement.expand()

    return latexify((statement, choices, answer))
# Factor
def qpol_factor(config_table:dict):
    f_1, f_2 = get_numbers_in_range(
        config_table['minimum_factor'],
        config_table['maximum_factor'],
        [0],
        2
    )

    mon_1 = x + f_1
    mon_2 = x + f_2

    statement = string_to_tex(latex((mon_1 * mon_2).expand()))
    choices = []
    answer = string_to_tex(f'\\left({mon_1}\\right)\\left({mon_2}\\right)')

    return (statement, choices, answer)
# Complete the square
def qpol_square(config_table:dict):
    factor, coefficient, a, b = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        4
    )

    is_add = choice([True, False])

    if is_add:
        equation = factor * (coefficient * x + a)**2 + b
    else:
        equation = factor * (coefficient * x - a)**2 + b

    statement = string_to_tex(latex(equation.expand()))
    choices = []
    answer = string_to_tex(latex(equation))

    return (statement, choices, answer)
# Summary
def qpol_summary(config_table:dict):
    operator_array = [
        qpol_expand,
        qpol_factor,
        qpol_square
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - Equation Solving -

# - Integers -

# One step equations
def eq_int_one(config_table:dict):
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
def eq_int_two(config_table:dict):
    a, b, c = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        3
    )

    statement = Eq(a * x + b, c)
    choices = []
    answer = solve(statement, x)[0]
    
    return latexify((statement, choices, answer))
# Summary
def eq_int_summary(config_table:dict):
    operator_array = [
        eq_int_one,
        eq_int_two
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - Rationals -

# One step equations
def eq_rat_one(config_table:dict):
    n_1, n_2 = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )
    d_1, d_2 = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1],
        2
    )

    r_1 = Rational(n_1, d_1)
    r_2 = Rational(n_2, d_2)

    statement = Eq(r_1 * x, r_2)
    choices = []
    answer = solve(statement, x)[0]
    return latexify((statement, choices, answer))
# Two step equations
def eq_rat_two(config_table:dict):
    n_1, n_2, n_3 = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        3
    )
    d_1, d_2, d_3 = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1],
        3
    )

    r_1 = Rational(n_1, d_1)
    r_2 = Rational(n_2, d_2)
    r_3 = Rational(n_3, d_3)

    statement = Eq(r_1 * x + r_2, r_3)
    choices = []
    answer = solve(statement, x)[0]

    return latexify((statement, choices, answer))
# Multi-step equations
def eq_rat_multi(config_table:dict):
    degree = get_numbers_in_range(
        config_table['minimum_degree'],
        config_table['maximum_degree'],
        [0]
    )

    root_count = 2 * degree - 2

    roots = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        root_count,
        False
    )

    numerator = (x + roots[0])
    denominator = (x + roots[0])

    for n in range(1, degree):
        numerator *= (x + roots[n])
    for n in range(degree, root_count):
        denominator *= (x + roots[n])
    
    numerator = numerator.expand()
    denominator = denominator.expand()

    statement = Eq(numerator/denominator, 0)
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))
# Summary
def eq_rat_summary(config_table:dict):
    operator_array = [
        eq_rat_one,
        eq_rat_two,
        eq_rat_multi
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - Radicals -

# One step equations
def eq_rad_one(config_table:dict):
    primes = prime_number_list(config_table['minimum_prime'], config_table['maximum_prime'])
    prime = choice(primes)

    n = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1]
    )

    statement = Eq(n * x, sqrt(prime))
    choices = []
    answer = solve(statement, x)[0]

    return latexify((statement, choices, answer))
# Two step equations
def eq_rad_two(config_table:dict):
    primes = prime_number_list(config_table['minimum_prime'], config_table['maximum_prime'])
    prime = choice(primes)

    a, b, c = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1],
        3
    )

    statement = Eq(a * x + sqrt(prime), b * x + c)

    if statement == False:
        return eq_rad_two(config_table)

    choices = []
    answer = solve(statement, x)[0]

    return latexify((statement, choices, answer))
# Multi-step equations
def eq_rad_multi(config_table:dict):
    primes = prime_number_list(config_table['minimum_prime'], config_table['maximum_prime'])
    prime = choice(primes)

    a, b, c = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1],
        3
    )

    statement = Eq(sqrt(a * x + b), c + sqrt(prime))
    choices = []
    answer = solve(statement, x)[0]

    return latexify((statement, choices, answer))
# Summary
def eq_rad_summary(config_table:dict):
    operator_array = [
        eq_rad_one,
        eq_rad_two,
        eq_rad_multi
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - Absolute Values -

# Integer equations
def eq_abs_int(config_table:dict):
    x = Symbol('x', real = True)

    a, b, c = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        3
    )

    c = abs(c)

    statement = Eq(abs(a * x + b), c)
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))
# Rational equations
def eq_abs_rat(config_table:dict):
    x = Symbol('x', real = True)

    n_1, n_2, n_3 = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        3
    )
    d_1, d_2, d_3 = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1],
        3
    )

    r_1 = Rational(n_1, d_1)
    r_2 = Rational(n_2, d_2)
    r_3 = Rational(n_3, d_3)

    r_3 = abs(r_3)

    statement = Eq(abs(r_1 * x + r_2), r_3)
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))
# Radical equations
def eq_abs_rad(config_table:dict):
    primes = prime_number_list(config_table['minimum_prime'], config_table['maximum_prime'])
    prime = choice(primes)

    x = Symbol('x', real = True)

    a, b = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    b = abs(b)

    statement = Eq(abs(sqrt(prime) * x + a), b)
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))

# - Quadratic Equations -

# Completed squares
def eq_quad_comp_sqr(config_table:dict):
    a, b = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    statement = Eq((x + a) ** 2, b ** 2)
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))
# Integer solutions
def eq_quad_int(config_table:dict):
    a, b = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    if choice([True, False]):
        a *= -1
    if choice([True, False]):
        b *= -1

    mon_1 = x + a
    mon_2 = x + b

    statement = Eq((mon_1 * mon_2).expand(), 0)
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))
# Difference of squares
def eq_quad_diff_sqr(config_table:dict):
    a, b = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    a **= 2
    b **= 2

    statement = Eq(a * x ** 2 - b, 0)
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))
# Complex number solutions
def eq_quad_comp(config_table:dict):
    x = Symbol('x', complex=True)

    a, b = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    mon_1 = a + b * I
    mon_2 = a - b * I

    mon_1 *= -1
    mon_2 *= -1

    equation = (x + mon_1) * (x + mon_2)

    statement = Eq(equation.expand(), 0)
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))
# Radical solutions
def eq_quad_rad(config_table:dict):
    primes = prime_number_list(config_table['minimum_prime'], config_table['maximum_prime'])
    prime = choice(primes)

    a, b = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        2
    )

    mon_1 = a * sqrt(prime)
    mon_2 = b * sqrt(prime)
    
    mon_1 *= -1
    mon_2 *= -1

    equation = (x + mon_1) * (x + mon_2)

    statement = Eq(equation.expand(), 0)
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))
# Summary
def eq_quad_summary(config_table:dict):
    operator_array = [
        eq_quad_comp_sqr,
        eq_quad_int,
        eq_quad_diff_sqr,
        eq_quad_comp,
        eq_quad_rad
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - General -

# Factored equations
def eq_gen_factored(config_table:dict):
    factor_count = get_numbers_in_range(
        config_table['minimum_factor_count'],
        config_table['maximum_factor_count'],
        [0]
    )

    equation = 1
    for _ in range(factor_count):
        n = get_numbers_in_range(
            config_table['minimum_integer'],
            config_table['maximum_integer'],
        )
        equation *= (x + n)
    
    statement = Eq(equation, 0)
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))
# Polynomial equations
def eq_gen_pol(config_table:dict):
    degree = get_numbers_in_range(
        config_table['minimum_degree'],
        config_table['maximum_degree'],
        [0]
    )
    equation = 1
    for _ in range(degree):
        n = get_numbers_in_range(
            config_table['minimum_integer'],
            config_table['maximum_integer'],
        )
        equation *= (x + n)
    
    statement = Eq(equation.expand(), 0)
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))
# Multi-variate equations
def eq_gen_multi(config_table:dict):
    a, b, c = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        3
    )
    
    statement = Eq(a*x + b*y + c, 0)
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))
# Summary
def eq_gen_summary(config_table:dict):
    operator_array = [
        eq_gen_factored,
        eq_gen_pol,
        eq_gen_multi
    ]
    operation = choice(operator_array)
    return operation(config_table)

# - Exponents and logarithms -

# Exponential equations
def eq_exp(config_table:dict):
    l_a, l_b = get_numbers_in_range(
        config_table['minimum_exponent'],
        config_table['maximum_exponent'],
        [0],
        2
    )
    l_c, r_a, r_b, r_c = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        4
    )
    base = get_numbers_in_range(
        config_table['minimum_base'],
        config_table['maximum_base'],
        [0, 1]
    )

    l_exp = l_b * x + l_c
    r_exp = r_b * x + r_c

    l_term = (base ** l_a) ** l_exp
    r_term = (base ** r_a) ** r_exp

    exponent_equation = Eq(l_a * l_exp, r_a * r_exp)

    statement = Eq(l_term, r_term)
    choices = []
    answer = solve(exponent_equation, x)

    return latexify((statement, choices, answer))
# Logarithmic equations
def eq_log(config_table:dict):
    a, b, c, d = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1],
        4
    )

    a = abs(a)
    d = abs(d)

    statement = Eq(a, log(b * x + c, d))
    choices = []
    answer = solve(statement, x)

    return latexify((statement, choices, answer))

# - Systems of Equations -

# Utils
def generic_system(config_table:dict, dimension:int):
    symbol_list = "xyzw"
    symbols = [Symbol(s) for s in symbol_list]

    statement = r'\begin{cases}'
    equations = []

    for i in range(dimension):
        equation = 0
        for j in range(dimension + 1):
            n = get_numbers_in_range(
                config_table['minimum_integer'],
                config_table['maximum_integer'],
                [0]
            )
            if j != dimension:
                equation += n * symbols[j]
            else:
                equation += n

        equations.append(equation)

        separator = ''
        if i != dimension - 1:
            separator = '\\\\'

        statement += latex(equation) + separator
    statement += r'\end{cases}'

    statement = string_to_tex(statement)
    choices = []
    answer = string_to_tex(
        latex(
            solve(equations, symbols)
        )
    )

    return (statement, choices, answer)
# Systems of two equations
def system_two(config_table:dict):
    return generic_system(config_table, 2)
# Systems of three equations
def system_three(config_table:dict):
    return generic_system(config_table, 3)
# Systems of four equations
def system_four(config_table:dict):
    return generic_system(config_table, 4)

# - Summary -

# Algebra summary
def summary(config_table:dict):
    operator_array = [
        rad_add,
        rad_sub,
        rad_mul,
        rad_dis,
        rad_rat,
        rad_simplify,
        com_add,
        com_sub,
        com_mul,
        com_div,
        com_norm,
        pol_add,
        pol_sub,
        pol_expand,
        pol_factor,
        pol_mul_mon_pol,
        pol_mul_pol_pol,
        pol_bin_expansion,
        pol_hor_axis,
        qpol_expand,
        qpol_factor,
        qpol_square,
        eq_int_one,
        eq_int_two,
        eq_rat_one,
        eq_rat_two,
        eq_rat_multi,
        eq_rad_one,
        eq_rad_two,
        eq_rad_multi,
        eq_abs_int,
        eq_abs_rat,
        eq_abs_rad,
        eq_quad_comp_sqr,
        eq_quad_int,
        eq_quad_diff_sqr,
        eq_quad_comp,
        eq_quad_rad,
        eq_gen_factored,
        eq_gen_pol,
        eq_gen_multi,
        eq_exp,
        eq_log,
        system_two,
        system_three,
        system_four
    ]
    operation = choice(operator_array)
    return operation(config_table)