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
    log
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
# - Lists -

# Utils

def generate_set(config_table:dict):
    count = get_numbers_in_range(
        config_table['minimum_count'],
        config_table['maximum_count'],
        [0]
    )

    std_dev = config_table['minimum_std'] + (config_table['maximum_std'] - config_table['minimum_std']) * random()
    mean_value = config_table['minimum_integer'] + (config_table['maximum_integer'] - config_table['minimum_integer']) * random()

    values = normal(
        mean_value,
        std_dev,
        count
    )

    clipped_values = clip(values, config_table['minimum_integer'], config_table['maximum_integer'])

    return clipped_values.astype(int)
# Mean
def mean(config_table:dict):
    statement = generate_set(config_table)
    choices = []
    answer = format_number(sum(statement) / len(statement))

    return latexify((statement, choices, answer))
# Median
def median(config_table:dict):
    statement = generate_set(config_table)
    choices = []
    answer = format_number(med(statement))

    return latexify((statement, choices, answer))
# Mode
def mode(config_table:dict):
    statement = generate_set(config_table)
    choices = []

    frequency = Counter(statement)
    max_frequency = max(frequency.values())

    answer = [i for i, c in frequency.items() if c == max_frequency]

    return latexify((statement, choices, answer))
# Range
def range(config_table:dict):
    statement = generate_set(config_table)
    choices = []
    answer = format_number(max(statement) - min(statement))

    return latexify((statement, choices, answer))
# Geometric Mean
def geo_mean(config_table:dict):
    statement = generate_set(config_table)
    choices = []

    log_data = log(statement)
    gmean = exp(log_data.mean())

    answer = format_number(gmean)

    return latexify((statement, choices, answer))
# Variance
def variance(config_table:dict):
    statement = generate_set(config_table)
    choices = []
    answer = format_number(var(statement, axis=0))

    return latexify((statement, choices, answer))
# Standard Deviation
def std_dev(config_table:dict):
    statement = generate_set(config_table)
    choices = []
    answer = format_number(std(statement, axis=0))

    return latexify((statement, choices, answer))
# Quartiles
def quartiles(config_table:dict):
    quartile_choose = choice([1, 2, 3])

    match quartile_choose:
        case 1:
            statement_text = 'primer cuartil'
        case 2:
            statement_text = 'segundo cuartil'
        case 3:
            statement_text = 'tercer cuartil'

    quartile = quartile_choose / 4

    set = generate_set(config_table)

    statement = f'Calcule el {statement_text} de: {string_to_tex(latex(set))}'
    choices = []
    answer = string_to_tex(str(format_number(quantile(set, quartile))))

    return (statement, choices, answer)