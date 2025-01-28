from numpy.random import randint, choice
from json import load as json_load
from random import choice, random
from utils import (
    get_numbers_in_range,
    latexify,
    string_to_tex,
    format_number,
    coprime_number
)
from sympy import (
    Rational,
    Add,
    Mul,
    latex
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

# Utils
def match_operation(statement, expression, n, operation):
    match operation:
        case 'add':
            statement += f' + {n}'
            expression += f'+{n}'
        case 'substract':
            statement += f' - {n}'
            expression += f'-{n}'
        case 'multiply':
            statement += f' \\times {n}'
            expression += f'*{n}'
        case 'divide':
            statement += f' \\div {n}'
            expression += f'/{n}'
        case 'exponentiate':
            statement += f' ^ {n}'
            expression += f'**{n}'
    return (statement, expression)
def generic_order_equation(config_table:dict, has_parenthesis:bool, has_exponent:bool):
    numbers = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0],
        config_table['number_count']
    )

    statement = str(numbers[0])
    expression = str(numbers[0])

    next_number_close_parenthesis = False
    
    for index, n in enumerate(numbers):
        operations = ['add', 'substract', 'multiply', 'divide']

        if has_parenthesis: 
            parenthesis = choice([True, False])
        else:
            parenthesis = False

        if has_exponent:
            exponent = random() < 0.4
        else:
            exponent = False

        if exponent:
            power = get_numbers_in_range(
                config_table['minimum_exponent'],
                config_table['maximum_exponent']
            )
            statement, expression = match_operation(statement, expression, power, 'exponentiate')

        operation = choice(operations)

        if next_number_close_parenthesis:
            n = f'{n})'
            next_number_close_parenthesis = False
        elif parenthesis and index != len(numbers) - 1:
            n = f'({n}'
            next_number_close_parenthesis = True
        
        statement, expression = match_operation(statement, expression, n, operation)
    
    try:
        answer = eval(expression)
        answer = format_number(answer)
    except Exception:
        answer = "Sin respuesta"
    
    statement = string_to_tex(statement)
    choices = []
    answer = string_to_tex(str(answer))

    return (statement, choices, answer)
# Basic operations
def order_basic(config_table:dict):
    return generic_order_equation(config_table, False, False)
# Include exponents
def order_include_exp(config_table:dict):
    return generic_order_equation(config_table, False, True)
# Include parentheses
def order_include_paren(config_table:dict):
    return generic_order_equation(config_table, True, False)
# Include exponents and parentheses
def order_include_exp_paren(config_table:dict):
    return generic_order_equation(config_table, True, True)

# - Fractions -

# Util
def frac_common_base(config_table, is_substracting, is_common):
    l_den, r_den = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1],
        2,
        False
    )

    if is_common:
        r_den = l_den

    maximum_integer = config_table['maximum_integer']

    l = Rational(coprime_number(l_den, maximum_integer), l_den, gcd=1)
    r = Rational(coprime_number(r_den, maximum_integer), r_den, gcd=1)

    if is_substracting:
        r *= -1

    statement = Add(l, r, evaluate=False)
    choices = []
    answer = statement.simplify()

    return latexify((statement, choices, answer))
def get_fraction(config_table):
    maximum_integer = config_table['maximum_integer']
    den = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1]
    )
    return Rational(coprime_number(den, maximum_integer), den)
# Add with common denominators
def frac_add_common(config_table:dict):
    return frac_common_base(config_table, False, True)
# Subtract with common denominators
def frac_sub_common(config_table:dict):
    return frac_common_base(config_table, True, True)
# Add with uncommon denominators
def frac_add_uncommon(config_table:dict):
    return frac_common_base(config_table, False, False)
# Subtract with uncommon denominators
def frac_sub_uncommon(config_table:dict):
    return frac_common_base(config_table, True, False)
# Multiply
def frac_multiply(config_table:dict):
    l = get_fraction(config_table)
    r = get_fraction(config_table)

    statement = Mul(l, r, evaluate=False)
    choices = []
    answer = statement.simplify()

    return latexify((statement, choices, answer))
# Divide
def frac_div(config_table:dict):
    l = get_fraction(config_table)
    r = get_fraction(config_table)

    statement = string_to_tex(f'{latex(l)} \\div {latex(r)}')
    choices = []
    answer = string_to_tex(latex(l / r))

    return (statement, choices, answer)
# Simplify
def frac_simplify(config_table:dict):
    frac = get_fraction(config_table)

    factor = get_numbers_in_range(
        config_table['minimum_factor'],
        config_table['maximum_factor'],
        [0, 1]
    )

    num = frac.numerator * factor
    den = frac.denominator * factor

    statement = string_to_tex(f'\\frac{{{num}}}{{{den}}}')
    choices = []
    answer = string_to_tex(latex(frac))

    return (statement, choices, answer)
# Add and subtract
def frac_add_sub(config_table:dict):
    operator_array = [
        frac_add_uncommon,
        frac_sub_uncommon
    ]
    operation = choice(operator_array)
    return operation(config_table)
# Multiply and divide
def frac_mul_div(config_table:dict):
    operator_array = [
        frac_multiply,
        frac_div
    ]
    operation = choice(operator_array)
    return operation(config_table)
# Summary
def frac_summary(config_table:dict):
    operator_array = [
        frac_add_common,
        frac_sub_common,
        frac_add_uncommon,
        frac_sub_uncommon,
        frac_multiply,
        frac_div,
        frac_simplify
    ]
    operation = choice(operator_array)
    return operation(config_table)
# - Summary -

# Arithmetic summary
def summary(config_table:dict):
    operator_array = [
        int_add,
        int_sub,
        int_mul,
        int_div,
        order_basic,
        order_include_exp,
        order_include_paren,
        order_include_exp_paren,
        frac_add_common,
        frac_sub_common,
        frac_add_uncommon,
        frac_sub_uncommon,
        frac_multiply,
        frac_div,
        frac_simplify
    ]
    operation = choice(operator_array)
    return operation(config_table)